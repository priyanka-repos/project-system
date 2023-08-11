from fastapi import APIRouter
from typing import List
from .models import Base,Members,Projects
from sqlalchemy.orm import Session
from scripts.core.schema import Member,Project,ShowProject,ShowMember

from scripts.core.db_connection import engine,Session,Base

userRouter = APIRouter(
    tags=['member'],
    prefix='/member'
)
Base.metadata.create_all(engine)

session = Session()
@userRouter.post("/")
def create_user(member: Member):
    try:
        new_user = Members(id = member.id, name=member.name, createDate = member.createDate, project_id = member.project_id)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user
    except Exception as e:
        return "Unable to add data"

@userRouter.get("/",response_model=List[ShowMember])
def show_user():
    try:
        users = session.query(Members).all()
        return users

    except Exception as e:
        return "Unable to fetch data"

@userRouter.delete("/delete/{id}")
def delete_task(id:int):
    try:
        session.query(Members).filter(Members.id == id).delete()
        session.commit()
        return "Deleted"
    except Exception as e:
        session.rollback()
        print("Error in deleting task")
        return "Unable to delete"
    