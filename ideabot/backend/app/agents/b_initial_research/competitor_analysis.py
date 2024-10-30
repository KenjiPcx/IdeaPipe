from textwrap import dedent
from typing import List, Tuple

from app.engine.tools import ToolFactory
from app.workflows.single import FunctionCallingAgent
from llama_index.core.chat_engine.types import ChatMessage
from llama_index.core.tools import FunctionTool

def _get_competitor_analysis_params() -> Tuple[List[FunctionTool], str, str]:
    tools = []
    
    prompt_instructions = dedent(
        """
        You are an expert Competitive Intelligence Analyst. Using the provided problem description and proposed solution, analyze the competitive landscape.

        Key Research Sources:
        - ProductHunt (producthunt.com) => for SaaS products
        - AppSumo (appsumo.com) => for SaaS products
        - FutureTools.io => for SaaS products
        - Google Search results => for both SaaS and non-SaaS products
        
        For each relevant competitor found (aim for 3-5 top competitors):

        1. Core Solution Analysis
           - Main features and functionality
           - Key differentiators
           - Target audience and use cases
           - Pricing structure
        
        2. Market Reception
           - User reviews and sentiment
           - Major strengths/complaints
           - Recent updates or changes
           - Social proof (users, ratings)
        
        3. Strategic Insights
           - Potential gaps or opportunities
           - Unique approaches worth noting
           - Pricing strategy insights
           - Distribution channels used

        ### Tools usage
        1. Use the search tool to discover competitors. A tip is to suffix the search query with "startup", for example instead of just searching for "robot vacuum cleaner" you should search for "robot vacuum cleaner startup"
        2. Use the web scraper tool to scrape information from the product websites. Only scrape pages that will have the full product information. This would be the product's main page, its entry in Product Hunt, AppSumo, FutureTools, etc.

        ### Output
        Conclude a report with:
        - the top 3 competitors and their key differences with the proposed solution.
        - 2-3 key opportunities or gaps in the market that could be exploited.
        """
    )
    
    description = "Expert in competitive analysis and market positioning"

    configured_tools = ToolFactory.from_env(map_result=True)
    # Check if the tavily search tool is configured
    if "tavily" in configured_tools.keys():
        tools.extend(configured_tools["tavily"])
        prompt_instructions += dedent("""
            You are able to search the web for information using the Tavily search tool.
        """)
        description += (
            ", able to search the web for information using the Tavily search tool."
        )
    
    if "web_reader" in configured_tools.keys():
        tools.extend(configured_tools["web_reader"])
        prompt_instructions += dedent("""
            You are able to scrape the web for information using the web scraper tool.
        """)
        description += (
            ", able to scrape the web for information using the web scraper tool."
        )
    
    return tools, prompt_instructions, description


def create_competitor_analysis(chat_history: List[ChatMessage]):
    tools, prompt_instructions, description = _get_competitor_analysis_params()

    return FunctionCallingAgent(
        name="competitor_analysis",
        tools=tools,
        description=description,
        system_prompt=dedent(prompt_instructions),
        chat_history=chat_history,
    )
