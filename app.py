import os
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel

from main import app_graph
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Text-to-SQL Chatbot API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: ChatRequest):
    final_state = app_graph.invoke({"user_qs": request.message})

    return {
        "query": final_state.get("query", ""),
        "result": final_state.get("result", []),
        "should_visualize": final_state.get("should_visualize", False),
    }


@app.get("/chart")
def get_chart():
    if os.path.exists("latest_chart.png"):
        return FileResponse("latest_chart.png", media_type="image/png")
    return JSONResponse({"error": "No chart available yet"}, status_code=404)


@app.get("/")
def root():
    return {"status": "Text-to-SQL chatbot API is running"}