from fastapi import FastAPI
from main import run
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/run/")
async def run(inputs: dict):
    result = run(inputs)
    print(result)
    return {"result": result}