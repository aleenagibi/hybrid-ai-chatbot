from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv
from rag.rag import search
from api.tools import get_user_data
from router import route_query
from fastapi.middleware.cors import CORSMiddleware

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
        route = route_query(query.question)

        if route == "api":
            data = get_user_data()
            return {"response": data, "source": "API"}

        elif route == "rag":
            context = search(query.question)

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": f"""
You are a helpful assistant.

Use ONLY the provided context to answer the question.
Do NOT add extra information.
If the answer is not in the context, say "Not found in document".

Context:
{context}
""",
                    },
                    {"role": "user", "content": query.question},
                ],
            )

            return {"response": response.choices[0].message.content, "source": "RAG"}

        else:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": query.question},
                ],
            )

            return {"response": response.choices[0].message.content, "source": "LLM"}

    except Exception as e:
        return {"error": str(e)}
