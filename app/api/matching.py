from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.llamaindex_operations import create_matching_agent, match_problem_to_solutions

router = APIRouter()

# Initialize the matching agent
matching_agent = create_matching_agent()

class MatchRequest(BaseModel):
    problem_id: str

class MatchResponse(BaseModel):
    matches: str

@router.post("/match", response_model=MatchResponse)
async def match_problem(request: MatchRequest):
    try:
        matches = match_problem_to_solutions(matching_agent, request.problem_id)
        return MatchResponse(matches=matches)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
