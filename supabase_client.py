import os
from supabase import create_client, Client
from datetime import datetime

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def store_message(user_id: str, user_message: str, ai_reply: str):
    supabase.table("memory").insert({
        "user_id": user_id,
        "user_message": user_message,
        "ai_reply": ai_reply,
        "timestamp": datetime.utcnow().isoformat()
    }).execute()

def fetch_memory(user_id: str, limit: int = 10):
    response = supabase.table("memory")        .select("user_message, ai_reply")        .eq("user_id", user_id)        .order("timestamp", desc=True)        .limit(limit)        .execute()

    messages = response.data or []
    memory = ""
    for msg in reversed(messages):
        memory += f"User: {msg['user_message']}\nAI: {msg['ai_reply']}\n"
    return memory
