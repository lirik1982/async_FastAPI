from fastapi import FastAPI
import uvicorn
import asyncio
from aioredis import Redis
import aioredis

app = FastAPI()


async def createRedisPool():
    pool = await Redis.create_pool(
        '127.0.0.1',
        decode_responses=True,
        max_connections=10
    )
    return pool


async def task(iters, start_from, step, interval):
    r_connection = await rp.acq
    current = start_from
    for i in range(iters):
        current += step
        await asyncio.sleep(interval)
        yield current


@app.get("/addtask")
async def addtask(N: int, N1: int, step: int, interval: int):
    # N = int(request.headers.get("N"))
    # N1 = int(request.headers.get("N1"))
    # step = int(request.headers.get("d"))
    # interval = int(request.headers.get("interval"))

    state = await task(iters=N, start_from=N1, step=step, interval=interval)


@app.get("/gettasks")
async def gettasks():
    pass


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
