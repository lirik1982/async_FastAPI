"""
Определение маршрутов.

summary

"""
from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel

from app.tasks import Tasks

router = APIRouter()


class TaskRequest(BaseModel):
    """ Tasks init values."""

    iters: int = 25
    start_from: int = 0
    step: int = 3
    interval: int = 1


async def get_tasks_api(request: Request) -> Tasks:
    """Depends supply.

    Args:
        request(Request): application.
    Returns:
        Tasks: tasks list.
    """
    return request.app.tasks


@router.post('/add/')
async def add_task(
    task_request: TaskRequest,
    task_api: Tasks = Depends(get_tasks_api),
):
    """Runs task.

    Args:
        task_request: task properties.
        task_api: depends Tasks.
    Returns:
        none.
    """
    await task_api.add_task(
        iters=task_request.iters,
        start_from=task_request.start_from,
        step=task_request.step,
        interval=task_request.interval,
    )


@router.get('/get/')
async def get_tasks(request: Request):
    """View for get active tasks.

    Args:
        request: need for getting app.tasks.
    Returns:
        dict: tasks status list.
    """
    return dict(request.app.tasks.status.items())
