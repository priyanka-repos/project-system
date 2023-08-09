from fastapi import APIRouter
from typing import List,Dict
from . import models
from sqlalchemy.orm import Session
from scripts.core.schema import Project,ShowProject

from scripts.core.db_connection import engine,Session,Base

projectRouter = APIRouter(
    tags=['project'],
    prefix='/project'
)
models.Base.metadata.create_all(engine)

session = Session()

@projectRouter.post("/create")
def create_project(project: Project):
    new_project = models.Projects(id = project.id, name=project.name, createDate = project.createDate)
    session.add(new_project)
    session.commit()
    session.refresh(new_project)
    return new_project

@projectRouter.get("/get",response_model=List[ShowProject])
def show_user():
    projects = session.query(models.Projects).all()
    for doc in projects:
        print(doc)
    print(projects)        
    # return projects

