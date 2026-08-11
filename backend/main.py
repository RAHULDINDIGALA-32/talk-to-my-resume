from fastapi import FastAPI 
from pydantic import BaseModel
from pathlib import Path
from resume_reader import read_resume
from resume_parser import parse_resume
from candidate import ask_candidate

BASE_DIR = Path(__file__).resolve().parent
resume_path = BASE_DIR / "data" / "Rahul_Web3_Engineer_Resume.pdf"

class ChatRequest(BaseModel):
    question: str


app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to Talk To My Resume API"
    }

@app.post("/chat")
def chat(request: ChatRequest):
    resume_text = read_resume(resume_path)
    parsed_resume = parse_resume(resume_text)
    candidate_answer = ask_candidate(request.question, parsed_resume)
    return {
        "answer": candidate_answer
    }


