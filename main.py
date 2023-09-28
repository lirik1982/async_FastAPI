from fastapi import FastAPI, Depends, BackgroundTasks

import uvicorn

from tasks import Tasks
# Написать апи в котором стартует выполнение вычисления арифметической прогрессии.
# 1 метод стартует прогрессию, параметры n1 n d и временной интервал между вычислениями.
# 2 метод вывод статуса всех текущих вычислений.
# N1 N d это первый элемент прогрессии, кол-во итераций, дельта он же шаг прогрессии

app = FastAPI()
app.tasks = Tasks()


@app.get("/addtask/")
async def addtask(
    N=10, N1=1, step=1, interval=1,
    task_api: Tasks = Depends(),
):
    print(N, N1, step, interval)
    task_api.add_task(
        N=N, N1=N1, step=step, interval=interval)
    return {
        "response": "started",
    }

# @app.get("/gettasks")
# async def get_tasks_api(request: Request):
#     return request.app.tasks


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1",
                port=5000, log_level="info", workers=4)
