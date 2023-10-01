
"""
summary.

Написать апи в котором стартует выполнение вычисления
арифметической прогрессии.
1 метод стартует прогрессию, параметры n1 n d
и временной интервал между вычислениями.
2 метод вывод статуса всех текущих вычислений.
N1 N d это первый элемент прогрессии,
кол-во итераций, дельта он же шаг прогрессии
"""

# import uvicorn
from fastapi import FastAPI

from app.routers import router
from app.tasks import Tasks

app = FastAPI()
app.tasks = Tasks()

app.include_router(router, prefix='/api/v1/tasks')


