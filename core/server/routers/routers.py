from fastapi import APIRouter
from core.server.models.get_info import InfoResponse
from core.server.buffer import buffer, lock
get_info_router: APIRouter = APIRouter()

@get_info_router.post("/get_lexical")
async def get_info(info: InfoResponse):
    print(f"Received match: {info.match}")
    async with lock:
        buffer.append(info.match)
    return {"Rezult": "lexical info collected"}