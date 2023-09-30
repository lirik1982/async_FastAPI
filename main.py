
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

import uvicorn
from fastapi import FastAPI

from routers import router
from tasks import Tasks

app = FastAPI()
app.tasks = Tasks()

app.include_router(router, prefix='/api/v1/tasks')


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='127.0.0.1',
        log_level='info',
        port=5000,
        workers=1,
    )
