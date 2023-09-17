from fastapi import FastAPI
from fastapi import BackgroundTasks
import uvicorn

app = FastAPI()


def task(N, N1, d, pause):
    pass


@app.get("/addtask")
async def addtask():

    BackgroundTasks.add_task(task, N, N1, d, pause)
    pass


@app.get("/gettasks")
async def gettasks():
    pass


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
