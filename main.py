import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from my_first_agent.agent import root_agent

# Request model
class PromptRequest(BaseModel):
    prompt: str

# FastAPI app
app = FastAPI(
    title="My First AI Agent API",
    description="A FastAPI wrapper around Google Gemini ADK Agent",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Your AI Agent API is live!"}

@app.post("/run")
def run_agent(request: PromptRequest):
    response = root_agent.run(request.prompt)
    return {"response": response}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Use Render's port if available
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
