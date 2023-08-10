from fastapi import APIRouter
from typing import List,Dict
from . import models
from sqlalchemy.orm import Session
from scripts.core.schema import Task,ShowTask

from scripts.core.db_connection import engine,Session,Base

taskRouter = APIRouter(
    tags=['task'],
    prefix='/task'
)
models.Base.metadata.create_all(engine)

session = Session()

@taskRouter.post("/create")
def create_task(task: Task):
    new_task = models.Tasks(task_id = task.task_id, project_id=task.project_id, title=task.title, description=task.description, createDate = task.createDate, modifiedDate=task.modifiedDate, status=task.status)
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    return new_task

@taskRouter.get("/get",response_model=List[ShowTask])
def show_task():
    tasks = session.query(models.Tasks).all()
    # for doc in tasks:
    #     print(doc)
    # print(tasks) 
    return tasks       

@taskRouter.delete("/delete/{id}")
def delete_task(id:int):
    try:
        session.query(models.Tasks).filter(models.Tasks.task_id == id).delete()
        return "Deleted"
    except Exception as e:
        print("Error in deleting task")
        return "Unable to delete "
    


