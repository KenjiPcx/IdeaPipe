from textwrap import dedent
from typing import List, Tuple, Optional
from llama_index.core.chat_engine.types import ChatMessage
from llama_index.core.tools import FunctionTool
from app.engine.tools import ToolFactory
from app.workflows.single import FunctionCallingAgent


def _get_analyst_params() -> Tuple[List[type[FunctionTool]], str, str]:
    tools = []
    prompt_instructions = dedent(
        """
        You are an expert in analyzing financial data.
        You are given a task and a set of financial data to analyze. Your task is to analyze the financial data and return a report.
        Your response should include a detailed analysis of the financial data, including any trends, patterns, or insights that you find.
        Construct the analysis in a textual format like tables would be great!
        Don't need to synthesize the data, just analyze and provide your findings.
        Always use the provided information, don't make up any information yourself.
        """
    )
    description = "Expert in analyzing financial data"
    configured_tools = ToolFactory.from_env(map_result=True)
    # Check if the interpreter tool is configured
    if "interpreter" in configured_tools.keys():
        tools.extend(configured_tools["interpreter"])
        prompt_instructions += dedent("""
            You are able to visualize the financial data using code interpreter tool.
            It's very useful to create and include visualizations to the report (make sure you include the right code and data for the visualization).
            Never include any code into the report, just the visualization.
        """)
        description += (
            ", able to visualize the financial data using code interpreter tool."
        )
    return tools, prompt_instructions, description


def create_analyst(chat_history: Optional[List[ChatMessage]] = None):
    markets_research = create_markets_research_agent(chat_history)
    competitor_analysis = create_competitor_analysis_agent(chat_history)
    customer_insights = create_customer_insights_agent(chat_history)
    trends_research = create_trends_research_agent(chat_history)

    return AnalystTeam(
        markets_research=markets_research,
        competitor_analysis=competitor_analysis,
        customer_insights=customer_insights,
        trends_research=trends_research,
        chat_history=chat_history,
    )

class AnalystTeam:
    def __init__(self, markets_research, competitor_analysis, customer_insights, trends_research, chat_history):
        self.markets_research = markets_research
        self.competitor_analysis = competitor_analysis
        self.customer_insights = customer_insights
        self.trends_research = trends_research
        self.chat_history = chat_history

    async def analyze(self, query: str) -> str:
        # Implement the logic to coordinate between the different agents
        # This is a simplified example
        markets_result = await self.markets_research.chat(query)
        competitor_result = await self.competitor_analysis.chat(query)
        customer_result = await self.customer_insights.chat(query)
        trends_result = await self.trends_research.chat(query)

        # Combine the results (this is a simple concatenation, you might want a more sophisticated approach)
        combined_result = f"""
        Markets Research: {markets_result}
        Competitor Analysis: {competitor_result}
        Customer Insights: {customer_result}
        Trends Research: {trends_result}
        """

        return combined_result

# Helper functions to get parameters for each agent
def _get_markets_research_params() -> Tuple[List[FunctionTool], str]:
    tools = []
    prompt_instructions = dedent(
        """
        You are an expert in analyzing market trends and conditions.
        Your task is to provide insights on market size, growth rates, and key drivers.
        Use available data to support your analysis.
        """
    )
    return tools, prompt_instructions

def _get_competitor_analysis_params() -> Tuple[List[FunctionTool], str]:
    tools = []
    prompt_instructions = dedent(
        """
        You are an expert in analyzing competitor strategies and performance.
        Your task is to provide insights on key competitors, their market share, and strategies.
        Use available data to support your analysis.
        """
    )
    return tools, prompt_instructions

def _get_customer_insights_params() -> Tuple[List[FunctionTool], str]:
    tools = []
    prompt_instructions = dedent(
        """
        You are an expert in analyzing customer behavior and preferences.
        Your task is to provide insights on customer segments, buying patterns, and satisfaction levels.
        Use available data to support your analysis.
        """
    )
    return tools, prompt_instructions

def _get_trends_research_params() -> Tuple[List[FunctionTool], str]:
    tools = []
    prompt_instructions = dedent(
        """
        You are an expert in identifying and analyzing industry trends.
        Your task is to provide insights on emerging technologies, regulatory changes, and shifts in consumer behavior.
        Use available data to support your analysis.
        """
    )
    return tools, prompt_instructions

def create_markets_research_agent(chat_history: Optional[List[ChatMessage]] = None) -> FunctionCallingAgent:
    tools, prompt_instructions = _get_markets_research_params()
    return FunctionCallingAgent(
        name="markets_research",
        tools=tools,
        description="Expert in analyzing market trends and conditions",
        system_prompt=prompt_instructions,
        chat_history=chat_history,
    )

def create_competitor_analysis_agent(chat_history: Optional[List[ChatMessage]] = None) -> FunctionCallingAgent:
    tools, prompt_instructions = _get_competitor_analysis_params()
    return FunctionCallingAgent(
        name="competitor_analysis",
        tools=tools,
        description="Expert in analyzing competitor strategies and performance",
        system_prompt=prompt_instructions,
        chat_history=chat_history,
    )

def create_customer_insights_agent(chat_history: Optional[List[ChatMessage]] = None) -> FunctionCallingAgent:
    tools, prompt_instructions = _get_customer_insights_params()
    return FunctionCallingAgent(
        name="customer_insights",
        tools=tools,
        description="Expert in analyzing customer behavior and preferences",
        system_prompt=prompt_instructions,
        chat_history=chat_history,
    )

def create_trends_research_agent(chat_history: Optional[List[ChatMessage]] = None) -> FunctionCallingAgent:
    tools, prompt_instructions = _get_trends_research_params()
    return FunctionCallingAgent(
        name="trends_research",
        tools=tools,
        description="Expert in identifying and analyzing industry trends",
        system_prompt=prompt_instructions,
        chat_history=chat_history,
    )
