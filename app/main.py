from fastapi import FastAPI

from api import agent, health


app = FastAPI()

app.include_router(agent.router)
app.include_router(health.router)
