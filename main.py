from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from service import Service

app = FastAPI()
service = Service()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static", html=True), name="static")


class Item(BaseModel):
    text: str


@app.post("/summarize/bert")
async def summarize(item: Item):
    return service.get_summery_bart(item.text)


@app.post("/summarize/destilbert")
async def summarize(item: Item):
    return service.get_summery_destilbert(item.text)


@app.post("/summarize/t5")
async def summarize(item: Item):
    return service.get_summery_t5_small(item.text)
