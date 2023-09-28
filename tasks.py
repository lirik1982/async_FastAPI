import asyncio
from fastapi import BackgroundTasks, Request


class Tasks:

    def __init__(self) -> None:
        self.counter = 0
        self.status = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Tasks, cls).__new__(cls)
        return cls.instance

    async def _mytask(self, iters, start_from, step, interval):
        print("Начали задачу")
        current = start_from
        for i in range(iters):
            current += step
            print(f'task step={i}  progress={current}')
            await asyncio.sleep(interval)

    async def add_task(
        self,
        back_ground_tasks=BackgroundTasks,
        N=10, N1=1, step=1, interval=1,
    ):
        print("class starting")
        await back_ground_tasks.add_task(self._mytask, N, N1, step, interval)
        return {
            "response": "started",
        }

    async def get_tasks_api(request: Request):
        return request.app.tasks

    def __update_status(self, iters, start_from, step):

        pass

    def get_active(self):
        pass
