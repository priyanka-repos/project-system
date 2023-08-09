from pydantic import BaseModel
from pydantic.schema import Optional
from datetime import datetime, date
from typing import List

class Member(BaseModel):
    id: int
    name : str
    createDate : date
    project_id : int
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
    class Config():
        orm_mode = True

class ShowTask(BaseModel):
    taskid: int
    projectid: int
    title: str
    description: str
    createDate: date
    modifiedDate: date
    status: str

class Project(BaseModel):
    id: int
    name: str
    createDate: date
    class Config():
        orm_mode = True

    


class ShowProject(BaseModel):
    id: int
    name: str
    createDate: Optional[date] = None
    members: List[Member]
    tasks: Optional[List[Task]] = None
    class Config():
        orm_mode = True

class ShowMember(BaseModel):
    id: int
    name : str
    createDate : date
    project_id : int
    project: Project
    class Config():
        orm_mode = True

