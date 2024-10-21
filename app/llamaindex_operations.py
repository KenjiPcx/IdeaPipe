from llama_index import VectorStoreIndex, Document
from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index.agent import OpenAIAgent
from ideagen.db.operations import supabase
import os

# Ensure you have set your OpenAI API key
os.environ['OPENAI_API_KEY'] = 'your-openai-api-key'

def create_problem_index():
    problems = supabase.table('problems').select('*').execute().data
    documents = [Document(doc_id=p['id'], text=f"{p['title']} {p['content']}") for p in problems]
    return VectorStoreIndex.from_documents(documents)

def create_solution_index():
    solutions = supabase.table('solutions').select('*').execute().data
    documents = [Document(doc_id=s['id'], text=f"{s['name']} {s['short_description']}") for s in solutions]
    return VectorStoreIndex.from_documents(documents)

def create_matching_agent():
    problem_index = create_problem_index()
    solution_index = create_solution_index()

    problem_engine = problem_index.as_query_engine()
    solution_engine = solution_index.as_query_engine()

    tools = [
        QueryEngineTool(
            query_engine=problem_engine,
            metadata=ToolMetadata(
                name="problem_search",
                description="Useful for searching and analyzing problems"
            )
        ),
        QueryEngineTool(
            query_engine=solution_engine,
            metadata=ToolMetadata(
                name="solution_search",
                description="Useful for finding and recommending solutions"
            )
        )
    ]

    return OpenAIAgent.from_tools(
        tools,
        system_prompt="""You are an AI assistant specialized in matching problems with appropriate solutions. 
        Your task is to analyze given problems and find the most relevant solutions from the available data. 
        Provide detailed explanations for your matches and recommendations."""
    )

def match_problem_to_solutions(agent, problem_id):
    problem = supabase.table('problems').select('*').eq('id', problem_id).execute().data[0]
    
    query = f"""Analyze this problem: '{problem['title']}. {problem['content']}'
    Find the most relevant solutions for this problem. Explain why each solution is appropriate."""
    
    response = agent.chat(query)
    return str(response)  # Convert the response to a string for easy JSON serialization
# Usage
matching_agent = create_matching_agent()

# Example usage
problem_id = "some_problem_id"
matches = match_problem_to_solutions(matching_agent, problem_id)
print(matches)
