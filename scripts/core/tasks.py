from fastapi import APIRouter
from typing import List,Dict
from . import models
from sqlalchemy.orm import Session
from scripts.core.schema import Task

from scripts.core.db_connection import engine,Session,Base

taskRouter = APIRouter(
    tags=['task'],
    prefix='/task'
)
models.Base.metadata.create_all(engine)

session = Session()

@taskRouter.post("/create")
def create_project(task: Task):
    new_task = models.Tasks(task_id = task.taskid, title=task.title, description=task.description, createDate = task.createDate, modifiedDate=task.modifiedDate, status=task.status)
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    return new_task

@taskRouter.get("/get",response_model=List[Task])
def show_user():
    tasks = session.query(models.Tasks).all()
    for doc in tasks:
        print(doc)
    print(tasks)        
    # return projects

