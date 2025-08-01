from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
from supabase_client import store_message, fetch_memory

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

class UserMessage(BaseModel):
    user_id: str
    message: str

@app.post("/chat")
async def chat_with_gpt(data: UserMessage):
    memory = fetch_memory(data.user_id)

    prompt = f"""
You are MAYOAIAGENT — a master-level, spiritual, creative AI agent for power and transformation.
Talk like Cheef. Speak with clarity and insight.

Memory:
{memory}

User: {data.message}
AI:"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are MAYOAIAGENT. Respond with spiritual, creative, and practical power."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    reply = response.choices[0].message.content.strip()

    store_message(data.user_id, data.message, reply)

    return {"response": reply}from fastapi import FastAPI, Request
from pydantic import BaseModel
import openai
from supabase_client import store_message, fetch_memory
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

class UserMessage(BaseModel):
    user_id: str
    message: str

@app.post("/chat")
async def chat_with_gpt(data: UserMessage):
    # Retrieve memory from Supabase
    memory_context = fetch_memory(data.user_id)

    # Build prompt with memory
    prompt = f"""
You are MAYOAIAGENT — a master-level, spiritual, creative AI agent for power and transformation.
Use memory, talk like Cheef, and answer with clarity and depth.

Memory:
{memory_context}

User: {data.message}
AI:"""

    # Call OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are MAYOAIAGENT. Respond with spiritual, street-smart, creative power."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    reply = response.choices[0].message.content.strip()

    # Store to Supabase
    store_message(data.user_id, data.message, reply)

    return {"response": reply}
