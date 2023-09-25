from fastapi import FastAPI
import uvicorn
import asyncio
from tasks import Tasks

# Написать апи в котором стартует выполнение вычисления арифметической прогрессии.
# 1 метод стартует прогрессию, параметры n1 n d и временной интервал между вычислениями.
# 2 метод вывод статуса всех текущих вычислений.
# N1 N d это первый элемент прогрессии, кол-во итераций, дельта он же шаг прогрессии

# Тут не нужно глобальную, ты при создании сервера в инстанс приложения можно всунуть свой класс с тасками.
# app.yourclass=YourClacc()
# И потом в реквесте доставать из app либо через depends если это fastapi
# Либо можно сделать синглтоном


app = FastAPI()
app.tasks = Tasks()


# async def get_coroutines():
#     coroutines = []
#     for task in asyncio.all_tasks():
#         if task.done():
#             continue
#         coroutines.append(task)
#     return coroutines


async def progress(iters, start_from, step, interval):
    print("Начали задачу")
    current = start_from
    for i in range(iters):
        current += step
        print('task step:', i)
        await asyncio.sleep(interval)
        yield current


@app.get("/addtask")
async def addtask(N: int = 10, N1: int = 1, step: int = 1, interval: int = 1):
    print("command to add task")
    # asyncio.create_task(progress(N, N1, step, interval))
    return {
        "response": "started",
        "N": N, "N1": N1, "step": step, "interval": interval
    }


@app.get("/gettasks")
async def gettasks():
    # print(get_coroutines())
    pass


if __name__ == "__main__":

    uvicorn.run("main:app", host="127.0.0.1",
                port=5000, log_level="info", workers=4)
