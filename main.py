import sys
from pathlib import Path
from langgraph.graph import StateGraph, END
from src import CustomState
from src import retrieval_node
from src import generate_query
from src import executor_node
from src import check_visualize
from src import visualize
# Naya node import karein
from src.response_node import generate_final_response 

base_dir = Path(__file__).resolve().parent
sys.path.append(base_dir.as_posix())

def build_graph():
    graph = StateGraph(CustomState)

    graph.add_node("retrieve_schema", retrieval_node)
    graph.add_node("generate_query", generate_query)
    graph.add_node("execute_query", executor_node)
    graph.add_node("generate_response", generate_final_response)
    graph.add_node("visualize", visualize)

    graph.set_entry_point("retrieve_schema")
    graph.add_edge("retrieve_schema", "generate_query")
    graph.add_edge("generate_query", "execute_query")
    
    graph.add_edge("execute_query", "generate_response")
    
    graph.add_conditional_edges(
        "generate_response",
        check_visualize,
        {"Yes": "visualize", "No": END}
    )
    graph.add_edge("visualize", END)

    return graph.compile()


app_graph = build_graph()

if __name__ == "__main__":
    user_question = "Show me total sales by payment method"
    
    result = app_graph.invoke({"user_qs": user_question})
    
    print(f" Chatbot: {result.get('final_response', 'No response generated.')}")

    if result.get("should_visualize"):
        print(" [System Info]: Chart has been generated and saved to your directory.")
