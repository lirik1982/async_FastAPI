import asyncio
from singleton import singleton


@singleton
class Tasks:

    def __init__(self) -> None:
        self.counter = 0
        self.status = {}

    async def task(self, iters, start_from, step, interval):
        print("Начали задачу")
        current = start_from
        for i in range(iters):
            current += step
            print('task step:', i)
            await asyncio.sleep(interval)
            yield current

    def update_status(self, iters, start_from, step):

        pass
