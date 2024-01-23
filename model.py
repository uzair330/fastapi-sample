from pydantic import BaseModel, Field, EmailStr


from sqlalchemy.orm import declarative_base, Mapped, column_property, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from database import Session, engine

Base = declarative_base()


class University(Base):
    __tablename__ = "university"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    programs = relationship("Program", back_populates="university")


class Program(Base):
    __tablename__ = "program"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    university_id = Column(Integer, ForeignKey("university.id"))
    university = relationship("University", back_populates="programs")
    courses = relationship("Course", back_populates="program")


class Course(Base):
    __tablename__ = "course"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    program_id = Column(Integer, ForeignKey("program.id"))
    program = relationship("Program", back_populates="courses")
