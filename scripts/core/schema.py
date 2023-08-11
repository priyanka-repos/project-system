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
    task_id: int
    project_id: int
    title: Optional[str] = None
    description: Optional[str] = None
    createDate: Optional[date] = None
    modifiedDate: Optional[date] = None
    status: Optional[str] = None
    class Config():
        orm_mode = True


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
    members: Optional[List[Member]] = []
    tasks: Optional[List[Task]] = []
    class Config():
        orm_mode = True
    class Config():
        orm_mode = True    

class ShowMember(BaseModel):
    id: int
    name : str
    createDate : date
    # project_id : int
    project: Project
    class Config():
        orm_mode = True

class ShowTask(BaseModel):
    task_id: int
    project_id: int
    title: Optional[str] = None
    description: Optional[str] = None
    createDate: Optional[date] = None
    modifiedDate: Optional[date] = None
    status: Optional[str] = None
    class Config():
        orm_mode = True

