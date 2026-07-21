from typing import TypedDict

class CustomState(TypedDict):
     user_qs : str
     schema_context:str
     query: str
     should_visualize : bool
     graph_type : str
     result: list
     final_response: str