import asyncio
from singleton import singleton
from fastapi import BackgroundTasks


async def task(self, iters, start_from, step, interval):
    print("Начали задачу")
    current = start_from
    for i in range(iters):
        current += step
        print('task step:', i)
        await asyncio.sleep(interval)
        yield current


@singleton
class Tasks:

    def __init__(self) -> None:
        self.counter = 0
        self.status = {}
        self.loop = asyncio.get_event_loop()

    async def add_task(self, iters, start_from, step, interval):
        BackgroundTasks.add_task(task, iters, start_from, step, interval)
        await asyncio.sleep(1)
        return {"status": "ok"}

    def update_status(self, iters, start_from, step):

        pass

    def get_active(self):
        pass
