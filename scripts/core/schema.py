from pydantic import BaseModel
from datetime import datetime, date
from typing import List

class Member(BaseModel):
    id: int
    name : str
    createDate : date
    class Config():
        orm_mode = True



class Task(BaseModel):
    taskid: int
    projectid: int
    title: str
    description: str
    createDate: date
    modifiedDate: date
    status: str
    # class Config():
    #     orm_mode = True


class Project(BaseModel):
    id: int
    name: str
    createDate: date
    class Config():
        orm_mode = True

    


class ShowProject(BaseModel):
    id: int
    name: str
    createDate: date
    members: List[Member]
    # tasks: List[Task]
    class Config():
        orm_mode = True

class ShowMember(BaseModel):
    id: int
    name : str
    createDate : date
    project_id : int
    project: List[Project]
    class Config():
        orm_mode = True

