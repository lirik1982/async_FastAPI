import asyncio
from singleton import singleton
from fastapi import BackgroundTasks


@singleton
class Tasks:

    def __init__(self) -> None:
        self.counter = 0
        self.status = {}

    async def _mytask(self, iters, start_from, step, interval):
        print("Начали задачу")
        current = start_from
        for i in range(iters):
            current += step
            print(f'task step={i}  progress={current}')
            await asyncio.sleep(interval)

    async def add_task(self,
                       back_ground_tasks: BackgroundTasks,
                       N: int = 10, N1: int = 1, step: int = 1, interval: int = 1,
                       ):
        print("class starting")
        await back_ground_tasks.add_task(self.mytask, N, N1, step, interval)
        return {
            "response": "started",
        }

    def __update_status(self, iters, start_from, step):

        pass

    def get_active(self):
        pass
