from fastapi import FastAPI, Depends, Request
import uvicorn
from tasks import Tasks

# Написать апи в котором стартует выполнение вычисления
# арифметической прогрессии.
# 1 метод стартует прогрессию, параметры n1 n d
# и временной интервал между вычислениями.
# 2 метод вывод статуса всех текущих вычислений.
# N1 N d это первый элемент прогрессии,
# кол-во итераций, дельта он же шаг прогрессии

app = FastAPI()
app.tasks = Tasks()


async def get_tasks_api(request: Request):
    return request.app.tasks


@app.get("/addtask/")
async def addtask(N: int = 10, N1: int = 1, step: int = 1, interval: int = 1,
                  task_api: Tasks = Depends(get_tasks_api),
                  ):

    await task_api.add_task(
        N=N, N1=N1, step=step, interval=interval)

    return {
        "response": "started",
    }


@app.get("/gettasks/")
async def get_tasks():
    r = [value for value in app.tasks.status.items()]
    return r


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1",
                port=5000, log_level="info", workers=4)
