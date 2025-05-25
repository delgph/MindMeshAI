from fastapi import FastAPI

from agents.crew_format.crew import Sentiment
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/api/greet")
def greet(name: str = "World"):
    print(f"Greeting request received with name: {name}")
    return {"message": f"Hello, {name}!"}


@app.post("/run/")
async def run(inputs: dict):

    payload ={"text": "Im feeling depressed and Im not happy",
            "user":"Diana",
             "days":"12 days"
            }

    result = Sentiment().crew().kickoff(inputs=payload)

    return {"result": result}
    # return "test"