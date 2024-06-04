from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://postgres:postMM2goit@localhost:5432/postgres')
Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship("Group", back_populates="students")
    grades = relationship("Grade", back_populates="student")


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Student", back_populates="group")


class Lecturer(Base):
    __tablename__ = 'lecturers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subjects = relationship("Subject", back_populates="lecturer")


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lecturer_id = Column(Integer, ForeignKey('lecturers.id'))
    lecturer = relationship("Lecturer", back_populates="subjects")
    grades = relationship("Grade", back_populates="subject")


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade = Column(Integer)
    date = Column(Date)
    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")


Base.metadata.create_all(engine)
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)
session = Session()