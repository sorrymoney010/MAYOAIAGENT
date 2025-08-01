import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are MAYOAIAGENT, a guide through spiritual darkness and reality decoding. Speak in the tone of Markus Hawkins aka BigHomieCheef, with depth, truth, and no sugarcoating."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']