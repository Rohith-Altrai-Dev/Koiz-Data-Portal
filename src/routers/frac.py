# FRAC - FACE RECOGNITION ACCESS CONTROL

from fastapi import APIRouter
from ..schemas.frac import AccessEvent
from .constants import *
from ..mqtt_client import client

router = APIRouter(prefix="/frac", tags=["FRAC"])

@router.post("/event")
async def post_access(event: AccessEvent):
    
    building_id = event.building_id
    
    client.publish(
        topic=GATE + "/" + building_id,
        payload=event.model_dump_json(),
        qos=1
        )

    return event