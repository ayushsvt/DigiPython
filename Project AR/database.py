from email.mime import base
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, column
from datetime import datetime 

Base = declarative_base()

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, unique=True)
    op1 = Column(String(255), nullable=False)
    op2 = Column(String(255), nullable=False)
    op3 = Column(String(255), nullable=False)
    op4 = Column(String(255), nullable=False)
    ans = Column(String(255), nullable=False)
    category = Column(String(255), nullable=False)
    add_on= Column(DateTime, default=datetime.now)
    
    def __str__(self):
        return self.title
class User(Base):
    __tablename__= "Login" 
    id= Column(Integer, primary_key=True)
    email = Column(String(200), nullable=False, unique=True)
    name = Column(String(200), nullable=False, unique=False)
    passward = Column(String(200), nullable=False, unique=True)
    add_on= Column(DateTime,default=datetime.now)

class Score(Base):
    __tablename__ = "Score"
    id = Column(Integer, primary_key=True)
    user = ForeignKey
    






if __name__ == "__main__":
    engine = create_engine("sqlite:///db.sqlite",echo=True)
    Base.metadata.create_all(engine)