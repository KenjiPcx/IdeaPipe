import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))
print(project_root)

import asyncio
import json
from typing import Dict, Any, List
from pydantic import BaseModel, Field
from openai import OpenAI
from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
from db.client import supabase
from tqdm import tqdm  # Import tqdm for progress bar

# Pydantic model for refined product info
class RefinedProductInfo(BaseModel):
    name: str = Field(description="Name of the product")
    refined_description: str = Field(description="Combined key points from the description, key features, audience, integrations, and alternatives it is replacing")
    potential_usecases: List[str] = Field(description="A few potential use cases where this product would be extremely useful, especially when combined with other technologies")
    ideal_users: List[str] = Field(description="Refined list of ideal customers facing specific issues that will use this product")
    ideal_scenarios: List[str] = Field(description="Predicted scenarios where this tool stands out and solves specific problems")
    integration_potential: List[str] = Field(description="Predicted ways this tool can effectively integrate with other tools and platforms")
    tags: List[str] = Field(description="Key feature tags to categorize the product")

# Constants and configurations
REFINEMENT_PROMPT = """
Analyze the following product information and provide a refined output:

Product Information:
{product_info}

Please provide the following:
1. A refined description that combines key points from the description, key features, audience, integrations, and alternatives it is replacing.
2. Generate 3-5 potential use cases where this product would be extremely useful, especially when combined with other technologies.
3. Further refine the audience and generate 3-5 ideal customer profiles facing specific issues that will use this product.
4. Predict and list 3-5 scenarios where this tool will stand out and solve specific problems.
5. Predict and list 3-5 ways this tool can effectively integrate with other tools and platforms.
6. Add relevant feature tags to categorize the product.

Format your response as a JSON object with the following structure:
{{
    "name": "Product Name",
    "refined_description": "Refined description...",
    "potential_usecases": ["Use case 1", "Use case 2", "Use case 3"],
    "ideal_users": ["Ideal user 1", "Ideal user 2", "Ideal user 3"],
    "scenarios_where_tool_excels": ["Scenario 1", "Scenario 2", "Scenario 3"],
    "integration_potential": ["Integration 1", "Integration 2", "Integration 3"],
    "tags": ["Tag 1", "Tag 2", "Tag 3"],
}}
"""

# Initialize OpenAI client
client = OpenAI()

# Functions
async def scrape_appsumo_product_page(url: str) -> Dict[str, Any]:
    schema = {
        "name": "Butternut AI Product Info",
        "baseSelector": "body",
        "fields": [
            {"name": "name", "selector": "h1.font-header", "type": "text"},
            {"name": "summary", "selector": "div.flex.flex-col.rounded.bg-gray-100.px-4", "type": "text"},
            {"name": "description", "selector": "#overview .prose", "type": "text"},
            {
                "name": "key_features",
                "selector": "#pricePlans ul li",
                "type": "list",
                "fields": [{"name": "feature", "type": "text"}]
            },
            {
                "name": "audience-integrations-alternativeProducts",
                "selector": "div.grid.grid-cols-1.gap-x-2.gap-y-4 ul",
                "type": "nested_list",
                "fields": [
                    {
                        "name": "detail",
                        "selector": "ul.mt-2.list-inside.list-disc li",
                        "type": "list",
                        "fields": [{"name": "item", "type": "text"}]
                    },
                ]
            },
            {"name": "summaryOfReviews", "selector": ".bg-asksumo", "type": "text"},
        ],
    }

    extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)
    
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url=url,
            extraction_strategy=extraction_strategy,
            bypass_cache=True,
        )

        assert result.success, "Failed to crawl the page"
        product_info = json.loads(result.extracted_content)
        return product_info[0]

async def refine_product_info(product_info: Dict[str, Any]) -> RefinedProductInfo:
    print(f"Refining product info: {product_info['name']} with an llm")
    if "summaryOfReviews" in product_info:
        del product_info["summaryOfReviews"]
    prompt = REFINEMENT_PROMPT.format(product_info=json.dumps(product_info, indent=2))

    try:
        response = client.beta.chat.completions.parse(
            model="gpt-4o-mini",  # Replace with your preferred model
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant that analyzes product information and provides refined insights."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
            response_format=RefinedProductInfo,
        )

        return response.choices[0].message.parsed
    except Exception as e:
        print(f"Error refining product info: {e}")
        return None

async def scrape_pipeline(product: dict) -> dict:
    url = product["url"]
    scraped_product_info = await scrape_appsumo_product_page(url)
    if "summaryOfReviews" in scraped_product_info:
        product["reviews_summary"] = scraped_product_info["summaryOfReviews"]
    product["name"] = scraped_product_info["name"]

    refined_product_info = await refine_product_info(scraped_product_info)
    product.update(refined_product_info.model_dump())

    return product

async def main(products: List[Dict[str, Any]]):
    total_products = len(products)
    progress_bar = tqdm(total=total_products, desc="Processing products")
    
    async def process_product(product):
        if product["url"] is None:
            print(f"Skipping product {product['name']} because it has no URL")
            return None
        result = await scrape_pipeline(product)
        # Parse certain fields into int
        if result["no_of_ratings"] is not None: 
            result["no_of_ratings"] = int(result["no_of_ratings"].replace(",", ""))
        else:
            result["no_of_ratings"] = 0 
        if result["rating"] is not None:
            result["rating"] = float(result["rating"])
        else:
            result["rating"] = 0
        if result["price"] != "FREE":
            result["price"] = float(result["price"].replace("$", ""))
        else:
            result["price"] = 0

        # Insert into supabase
        try:
            response = supabase.table("appsumo_products").insert(result).execute()
            print(f"Inserted product into supabase: {response}")
        except Exception as e:
            print(f"Error inserting product into supabase: {e}")

        progress_bar.update(1)
        return result

    results = []
    batch_size = 5
    for i in range(0, total_products, batch_size):
        batch = products[i:i+batch_size]
        tasks = [process_product(product) for product in batch]
        batch_results = await asyncio.gather(*tasks)
        results.extend(batch_results)
    
    progress_bar.close()
    return results

if __name__ == "__main__":
    # Load products from JSON file
    with open(f"{project_root}/scrape_pipelines/appsumo/setup/appsumo-products.json", 'r') as file:
        all_products = json.load(file)

    print(f"Starting to process {len(all_products)} products...")
    results = asyncio.run(main(all_products))  # Process all products

    # Save results to a JSON file
    with open('refined_appsumo_products.json', 'w') as f:
        json.dump(results, f, indent=2)

    print(f"Scraping completed. Refined data saved to refined_appsumo_products.json")
