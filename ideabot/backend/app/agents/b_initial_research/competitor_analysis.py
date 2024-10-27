from textwrap import dedent
from typing import List, Tuple

from app.engine.tools import ToolFactory
from app.workflows.single import FunctionCallingAgent
from llama_index.core.chat_engine.types import ChatMessage
from llama_index.core.tools import FunctionTool


def _create_competitor_search_tool():
    def find_competitors(industry: str, market_segment: str) -> str:
        """Mock tool to find direct and indirect competitors"""
        return f"List of competitors in {industry} focusing on {market_segment}"
    
    return FunctionTool.from_defaults(fn=find_competitors)

def _create_competitor_strength_tool():
    def analyze_competitor_strength(competitor: str) -> dict:
        """Mock tool to analyze competitor strengths and weaknesses"""
        return {
            "strengths": ["Example strength 1", "Example strength 2"],
            "weaknesses": ["Example weakness 1", "Example weakness 2"],
            "market_share": "X%",
            "key_features": ["Feature 1", "Feature 2"]
        }
    
    return FunctionTool.from_defaults(fn=analyze_competitor_strength)

def _get_competitor_analysis_params() -> Tuple[List[type[FunctionTool]], str, str]:
    tools = [
        _create_competitor_search_tool(),
        _create_competitor_strength_tool(),
    ]
    
    prompt_instructions = dedent(
        """
        You are an expert Competitive Intelligence Analyst specializing in market competition analysis.
        
        Your responsibilities:
        1. Identify direct and indirect competitors
        2. Analyze competitor strengths and weaknesses
        3. Map competitive landscape
        4. Identify market gaps and opportunities
        5. Assess competitive advantages
        
        Analysis Framework:
        1. Direct Competitors
           - Main players in the same space
           - Their market share
           - Key features/offerings
           - Pricing strategies
           
        2. Indirect Competitors
           - Alternative solutions
           - Potential future competitors
           - Adjacent market players
           
        3. Competitive Landscape
           - Market positioning
           - Value propositions
           - Target audience overlap
           
        4. Gap Analysis
           - Unmet customer needs
           - Underserved segments
           - Feature gaps
           - Service quality gaps
           
        Format your response as:
        1. Competitor Overview
           - Direct competitors
           - Indirect competitors
           - Market leaders
           
        2. Competitive Analysis
           - Strengths/weaknesses matrix
           - Feature comparison
           - Pricing comparison
           
        3. Market Gaps
           - Unmet needs
           - Opportunities
           
        4. Competitive Advantage
           - Potential differentiators
           - Barriers to entry
           - Strategic recommendations
        
        Use available tools to gather and validate competitive intelligence data.
        """
    )
    
    description = "Expert in competitive analysis and market positioning"
    
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
