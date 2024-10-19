from bs4 import BeautifulSoup

html = """""" # Desperate times, desperate measures. Just pasted the html here

soup = BeautifulSoup(html, 'html.parser')

products = []
product_cards = soup.select('div[class*="rounded bg-white md:border md:border-gray-300 md:shadow-md"]')

for card in product_cards:
    product = {}
    
    # Extract name
    name_elem = card.select_one("span.overflow-hidden.text-ellipsis.whitespace-nowrap.font-bold")
    product['name'] = name_elem.text.strip() if name_elem else None

    # Extract category
    category_elem = card.select_one("span.max-md\\:text-xs a")
    product['category'] = category_elem.text.strip() if category_elem else None

    # Extract short description
    desc_elem = card.select_one("div.my-1.line-clamp-3")
    product['shortDescription'] = desc_elem.text.strip() if desc_elem else None

    # Extract rating
    rating_elem = card.select_one("img[alt$='stars']")
    product['rating'] = rating_elem['alt'].split()[0] if rating_elem else None

    # Extract number of ratings
    ratings_count_elem = card.select_one("a[href$='#reviews'] span")
    product['noOfRatings'] = ratings_count_elem.text.split()[0] if ratings_count_elem else None

    # Extract price
    price_elem = card.select_one("div.font-medium.md\\:text-2xl span")
    product['price'] = price_elem.text.split('/')[0].strip() if price_elem else None

    products.append(product)

import json

filename = "appsumo-products.json"

try:
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)
    print(f"Data successfully written to {filename}")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")