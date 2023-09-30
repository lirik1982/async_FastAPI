"""
Определение маршрутов.

summary

"""
from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel

from tasks import Tasks

router = APIRouter()


class TaskRequest(BaseModel):
    """Определяет параметры tast.add."""

    iters: int = 25
    start_from: int = 0
    step: int = 3
    interval: int = 1


async def get_tasks_api(request: Request) -> Tasks:
    """нужна для task depends.

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
    """нужна для task depends.

    Args:
        task_request: task properties
        task_api: depends Tasks.

    Returns:
        dict: ok response.
    """
    await task_api.add_task(
        N=task_request.iters,
        N1=task_request.start_from,
        step=task_request.step,
        interval=task_request.interval,
    )

    return {
        'response': 'started',
    }


@router.get('/get/')
async def get_tasks(request: Request):
    """View for get active tasks.

    Args:
        request: need for getting app.tasks.

    Returns:
        dict: tasks status list
    """
    return dict(request.app.tasks.status.items())
