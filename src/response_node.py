from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.custom_state import CustomState
from config import GROQ_API_KEY 

def generate_final_response(state: CustomState) -> CustomState:
    llm = ChatGroq(model_name="llama-3.1-8b-instant", temperature=0.5, groq_api_key=GROQ_API_KEY)
    
    system_instruction = """You are a helpful and polite customer support and data assistant for a business chatbot.
Your job is to look at the User's Original Question and the Raw Database Results, then write a natural, clean, friendly, and easy-to-understand response for a NON-TECHNICAL user.

Guidelines:
1. Do not show raw tuples, brackets, or arrays (like [(4420.00,)]).
2. Format money values nicely (e.g., Rs. 4,420 or $4,420) if applicable.
3. Keep the response precise, professional, and clear.
4. Speak directly to the user.
5. If the database result is 'Done', mention that the operation was completed successfully."""

    prompt = ChatPromptTemplate.from_messages([
        ('system', system_instruction),
        ('human', "User Question: {user_question}\nRaw Database Result: {db_result}")
    ])
    
    chain = prompt | llm | StrOutputParser()
    
    final_message = chain.invoke({
        "user_question": state['user_qs'],
        "db_result": str(state.get('result', []))
    })
    
    state['final_response'] = final_message
    return state
