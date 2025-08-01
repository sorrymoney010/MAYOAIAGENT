import os
from supabase import create_client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception("Missing Supabase credentials!")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def store_message(user_id, message, reply):
    supabase.table("chat_memory").insert({
        "user_id": user_id,
        "message": message,
        "reply": reply
    }).execute()

def fetch_memory(user_id):
    res = supabase.table("chat_memory").select("*").eq("user_id", user_id).order("created_at", desc=True).limit(5).execute()
    messages = res.data or []
    return "\n".join([f"User: {m['message']}\nAI: {m['reply']}" for m in messages])
