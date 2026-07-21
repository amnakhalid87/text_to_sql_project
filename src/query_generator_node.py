import json
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.custom_state import CustomState
from config import GROQ_API_KEY 

def generate_query(state: CustomState) -> CustomState:
    
    llm = ChatGroq(model_name="llama-3.1-8b-instant", temperature=0.3, groq_api_key=GROQ_API_KEY)
    
    system_instruction = """You are an expert PostgreSQL developer and data analyst.

TARGET LIVE DATABASE SCHEMAS PROVIDED BELOW:
{schema_context}

STRICT PIPELINE COMPLIANCE INSTRUCTIONS:
1. Read the user input question and write a syntactically correct PostgreSQL query string.
2. Check if the user is explicitly or implicitly asking for a graph, chart, trend, plot, or visual representation. Set 'visualize' to true or false.
3. Determine what type of chart fits best (e.g., 'bar', 'line', 'pie', or 'none').
4. Return your final answer ONLY as a standardized valid JSON object with exactly three keys: 'query', 'visualize', and 'graph_type'.
5. ABSOLUTELY DO NOT include markdown blocks, text wrappers, or backticks like ```json.

EXPECTED STRUCTURE:
{{"query": "SELECT name, price FROM menu_items;", "visualize": true, "graph_type": "bar"}}"""

    prompt = ChatPromptTemplate.from_messages([
        ('system', system_instruction),
        ('human', "{user_question}")
    ])
    
    chain = prompt | llm | StrOutputParser()
    
    response = chain.invoke({
        "schema_context": state['schema_context'],
        "user_question": state['user_qs']
    })
    
    clean_json_text = response.strip()
    
    try:
        parsed_json = json.loads(clean_json_text)
        state['query'] = parsed_json.get("query", "")
        state['should_visualize'] = parsed_json.get("visualize", False)
        state['graph_type'] = parsed_json.get("graph_type", "none")
        
    except Exception as e:
        print(f"Failed to parse LLM structured output. Error is {e}")
        
    return state
