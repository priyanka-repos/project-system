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
    try:
        new_project = models.Projects(id = project.id, name=project.name, createDate = project.createDate)
        session.add(new_project)
        session.commit()
        session.refresh(new_project)
        return new_project
    except Exception as e:
        return "Unable to add project"

@projectRouter.get("/get",response_model=List[ShowProject])
def show_project():
    try:
        projects = session.query(models.Projects).all()
        return projects
    except Exception as e:
        return "Error in fetching data"
    
@projectRouter.delete("/delete/{id}")
def delete_project(id:int):
    try:
        project = session.query(models.Projects).filter(models.Projects.id == id).first()
        print(project)
        # if project is None:
        #     return  
        print("member--", project.members)
        members_to_update = project.members
        for member in members_to_update:
            member['project_id'] = None
        session.commit()
        session.delete(project)
        session.commit()
        return "Deleted project"
    except Exception as e:
        session.rollback()
        print(e)
        return "Error in deleting"        


