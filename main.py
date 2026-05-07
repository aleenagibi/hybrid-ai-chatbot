from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv
from rag.rag import search
from api.tools import get_user_data
# from router import route_query
from semantic_router import semantic_route
from fastapi.middleware.cors import CORSMiddleware
from modules.career import handle_career
from modules.wellbeing import handle_wellbeing
from modules.general import handle_general
from decision_engine import generate_decision

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# Request schema
class Query(BaseModel):
    question: str


# Root route
@app.get("/")
def home():
    return {"message": "Backend is running"}


# Chat endpoint
@app.post("/chat")
def chat(query: Query):

    try:

        # route = route_query(query.question)
        route = semantic_route(query.question)

        # Module selection
        if route == "career":
            result = handle_career(query.question)

        elif route == "wellbeing":
            result = handle_wellbeing(query.question)

        else:
            result = handle_general(query.question)

        # Decision engine
        print("ROUTE:", route)
        final_output = generate_decision(route, result)

        return final_output

    except Exception as e:

        return {
            "error": str(e)
        }