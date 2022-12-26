from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware




from http_endpoints.http_endpoints import HttpEndpointsClass
from managers.websocket_manager import WebsocketManagerClass

from websocket_endpoints.websocket_endpoints import WebsocketEndpointsClass



app = FastAPI()

manager = WebsocketManagerClass()

WebsocketEndpointsClass(app,manager)



HttpEndpointsClass(app)


origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    pass


@app.get("/")
async def root():
    return {"message": "Hello Scrapper Subs Server Applications!"}



