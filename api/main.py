from fastapi import FastAPI


from fastapi.middleware.cors import CORSMiddleware
from agents import sentiment_analysis_agent

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

    payload = {
        "text": "Im feeling depressed and Im not happy",
        "user": "Diana",
        "days": "12 days",
    }

    result = sentiment_analysis_agent.kickoff(inputs=payload)

    return {"result": result}


# if __name__ == "__main__":
#     payload = {
#         "text": "Im feeling depressed and Im not happy",
#         "user": "Diana",
#         "days": "12 days",
#     }
#
#     result = sentiment_analysis_agent.kickoff(inputs=payload)
#     print(result)
