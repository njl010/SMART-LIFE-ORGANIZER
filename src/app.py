from fastapi import FastAPI
from supervisor_agent import SupervisorAgent
import json


app = FastAPI(title="Smart Life Organizer")
supervisor = SupervisorAgent()


@app.get("/")
def home():
return {"message": "Smart Life Organizer Running"}


@app.post("/demo")
def run(payload: dict):
text = payload.get("text", "Plan my meals for 7 days")
output = supervisor.handle_user_request(text)
return output