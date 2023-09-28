import asyncio


class Tasks:

    def __init__(self) -> None:
        self.counter = 0
        self.status = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Tasks, cls).__new__(cls)
        return cls.instance

    def _update_status(self, id, step, current):
        out = f"Процесс:{id}, текущий шаг:{step}, текущая сумма:{current}"
        self.status[str(id)] = out

    async def _mytask(self, id: int, iters, start_from,
                      step, interval):
        current = start_from
        for i in range(iters):
            current += step
            self._update_status(str(id), i, current)
            await asyncio.sleep(interval)
        del self.status[str(id)]

    async def add_task(self, N=10, N1=1, step=1, interval=1,):
        self.counter += 1
        asyncio.create_task(self._mytask(self.counter, N, N1, step, interval))
        return {
            "response": "started",
        }
