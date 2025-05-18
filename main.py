from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.ai_engine import generate_code

app = FastAPI(title="DavidAI")

class CodeRequest(BaseModel):
    prompt: str
    language: str

@app.post("/generate_code")
async def code_gen(request: CodeRequest):
    try:
        result = await generate_code(request.prompt, request.language)
        return {"code": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
