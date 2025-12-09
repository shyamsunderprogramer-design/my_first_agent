from fastapi import FastAPI
from pydantic import BaseModel
from my_first_agent.agent import root_agent  # Use the existing instance
import uvicorn

# Request model for the /run endpoint
class PromptRequest(BaseModel):
    prompt: str

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
    response = root_agent.run(request.prompt)  # Use root_agent
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
