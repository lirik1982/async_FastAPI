"""Tasks supply module."""

import asyncio


class Tasks():
    """Tasks supply class."""

    def __init__(self) -> None:
        """Constructor."""
        self.counter = 0
        self.status = {}

    async def add_task(self, iters=10, start_from=1, step=1, interval=1):
        """Shorts."""

        self.counter += 1
        return asyncio.create_task(
            self._mytask(self.counter, iters, start_from, step, interval),
        )

    async def _mytask(
        self, task_id: int, iters, start_from, step, interval
    ):
        """ Async task.

        Args:
            task_id: task id.
            step: task step.
            iters: iters count.
            start_from: count starts from.
            interval: time interval between steps.
        Returns:
            none.
        """
        current = start_from
        for i in range(iters):
            await asyncio.sleep(interval)
            current += step
            self._update_status(str(id), i, current)
        del self.status[str(task_id)]

    def _update_status(self, task_id, step, current):
        """Update selected task status.

        Args:
            task_id: task id.
            step: task current step.
            current: current summ.
        Returns:
            none.
        """
        out = f"Процесс:{task_id}, текущий шаг:{step}, текущая сумма:{current}"
        self.status[str(task_id)] = out
