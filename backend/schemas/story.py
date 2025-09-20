# Schemas define the shape of data coming into your API (request body) and going out from your API (response).

# They also give you automatic validation and documentation.

# Based on these schemas, FastAPI:

# Checks if the incoming request data is valid.

# Automatically converts database objects into clean JSON responses.
from typing import List, Optional, Dict
from datetime import datetime
from pydantic import BaseModel

class StoryOptionsSchema(BaseModel):
    text:str 
    node_id: Optional[int] = None

class StoryNodeBase(BaseModel):
    content:str 
    is_ending:bool = False 
    is_winning_ending: bool = False 

class CompleteStoryNodeResponse(StoryNodeBase):
    id: int 
    options: List[StoryOptionsSchema] = []

    class Config: 
        from_attributes = True

class StoryBase(BaseModel):
    title:str 
    session_id: Optional[str] = None

    class Config: 
        from_attributes = True

class CreateStoryRequest(BaseModel):
    theme:str 

class CompleteStoryResponse(StoryBase):
    id: int 
    created_at: datetime
    root_node: CompleteStoryNodeResponse
    all_nodes: Dict[int, CompleteStoryNodeResponse]

    class Config: 
        from_attributes = True