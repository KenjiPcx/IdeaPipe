from textwrap import dedent
from typing import List, Tuple

from app.engine.tools import ToolFactory
from app.workflows.single import FunctionCallingAgent
from llama_index.core.chat_engine.types import ChatMessage
from llama_index.core.tools import FunctionTool


def _create_script_generator_tool():
    def generate_podcast_script(research_data: dict) -> dict:
        """Mock tool to generate engaging podcast script from research data"""
        return {
            "intro": "Engaging opening hook",
            "segments": ["Segment 1 content", "Segment 2 content"],
            "key_points": ["Point 1", "Point 2"],
            "closing": "Call to action and wrap-up"
        }
    
    return FunctionTool.from_defaults(fn=generate_podcast_script)

def _create_dialogue_generator_tool():
    def generate_dialogue(topic: str, style: str = "conversational") -> dict:
        """Mock tool to generate natural dialogue for podcast format"""
        return {
            "host_lines": ["Host line 1", "Host line 2"],
            "transitions": ["Transition 1", "Transition 2"],
            "emphasis_points": ["Point 1", "Point 2"],
            "questions": ["Question 1", "Question 2"]
        }
    
    return FunctionTool.from_defaults(fn=generate_dialogue)

def _get_podcaster_params() -> Tuple[List[type[FunctionTool]], str, str]:
    tools = [
        _create_script_generator_tool(),
        _create_dialogue_generator_tool(),
    ]
    
    prompt_instructions = dedent(
        """
        You are an expert Podcast Content Creator specializing in converting business research into engaging audio content.
        
        Your responsibilities:
        1. Transform research into engaging dialogue
        2. Create natural conversation flow
        3. Highlight key insights effectively
        4. Maintain audience engagement
        5. End with clear takeaways
        
        Content Framework:
        1. Opening Hook
           - Attention-grabbing intro
           - Problem statement
           - Episode promise
           - Relevance to audience
           
        2. Main Content Structure
           - Key findings narrative
           - Expert insights
           - Market implications
           - Real-world examples
           
        3. Engagement Elements
           - Conversational tone
           - Analogies and metaphors
           - Questions and answers
           - Story elements
           
        Format your response as:
        1. Episode Overview
           - Title and hook
           - Key segments
           - Target length
           - Core message
           
        2. Detailed Script
           - Introduction
           - Main segments
           - Transitions
           - Conclusion
           
        3. Key Takeaways
           - Main insights
           - Action items
           - Resources
           - Next steps
           
        4. Production Notes
           - Emphasis points
           - Pace changes
           - Tone variations
           - Sound cues
        
        Remember: Focus on creating a natural, engaging conversation that makes complex business insights accessible and interesting.
        """
    )
    
    description = "Expert in converting business research into engaging podcast content"
    
    return tools, prompt_instructions, description


def create_podcaster(chat_history: List[ChatMessage]):
    tools, prompt_instructions, description = _get_podcaster_params()

    return FunctionCallingAgent(
        name="market_research",
        tools=tools,
        description=description,
        system_prompt=dedent(prompt_instructions),
        chat_history=chat_history,
    )
