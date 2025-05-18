import httpx
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

async def generate_code(prompt: str, language: str) -> str:
    full_prompt = f"Write a {language} code snippet that: {prompt}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    json_data = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": "You are an expert code generator."},
            {"role": "user", "content": full_prompt}
        ]
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.openai.com/v1/chat/completions", json=json_data, headers=headers
        )
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']
