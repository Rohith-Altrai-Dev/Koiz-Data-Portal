from fastapi import FastAPI
from contextlib import asynccontextmanager
from .mqtt_client import client
from .routers import frac

@asynccontextmanager
async def lifespan(app: FastAPI):
    client.connect("koizzg.local", 1884, 60)
    client.loop_start()

    yield

    client.disconnect()
    client.loop_stop()
    

app = FastAPI(lifespan=lifespan)
app.include_router(frac.router)