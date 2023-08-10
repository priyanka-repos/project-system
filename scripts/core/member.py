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
    new_user = Members(id = member.id, name=member.name, createDate = member.createDate, project_id = member.project_id)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

@userRouter.get("/",response_model=List[ShowMember])
def show_user():
    users = session.query(Members).all()
    return users

@userRouter.delete("/delete/{id}")
def delete_task(id:int):
    try:
        session.query(Members).filter(Members.id == id).delete()
        # session.query(Projects).filter(Projects.members[id])
        return "Deleted"
    except Exception as e:
        print("Error in deleting task")
        return "Unable to delete "
    