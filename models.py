from typing import Optional
from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel

Base=declarative_base()
class Task(Base):
    __tablename__="tasks"
    task_id=Column(Integer,primary_key=True,autoincrement=True)
    title=Column(String,nullable=False)
    status=Column(Boolean,default=False)

