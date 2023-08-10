from sqlalchemy import Column, Integer, String, ForeignKey,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Members(Base):
    __tablename__ = 'Members'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    createDate = Column(Date)
    project_id = Column(Integer, ForeignKey('Projects.id'))  #remove
    project = relationship("Projects", back_populates="members")  #

class Tasks(Base):
    __tablename__ = 'Tasks'
    
    task_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('Projects.id')) #member_id
    title = Column(String)
    description = Column(String)
    createDate = Column(Date)
    modifiedDate = Column(Date)
    status = Column(String)
    project = relationship("Projects", back_populates="tasks")

class Projects(Base):
    __tablename__ = 'Projects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    createDate = Column(Date)
    members = relationship("Members", back_populates="project")
    tasks = relationship("Tasks", back_populates="project")  #remove
    #member list
