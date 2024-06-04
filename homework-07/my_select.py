from sqlalchemy import func
from models import Student, Group, Lecturer, Subject, Grade, session

def select_1():
    answer_1 = session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .join(Grade) \
        .group_by(Student.name) \
        .order_by(func.avg(Grade.grade) \
        .desc()) \
        .limit(5) \
        .all()
    return answer_1

def select_2(subject_name):
    answer_2 = session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
    .join(Grade) \
    .join(Subject) \
    .filter(Subject.name == subject_name) \
    .group_by(Student.name) \
    .order_by(func.avg(Grade.grade) \
    .desc()) \
    .first()
    return answer_2

def select_3(group_name, subject_name):
    answer_3 = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
    .join(Student) \
    .join(Group) \
    .join(Subject) \
    .filter(Group.name == group_name, Subject.name == subject_name) \
    .scalar()
    return answer_3

def select_4(group_name):
    answer_4 = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
    .join(Student) \
    .join(Group) \
    .filter(Group.name == group_name) \
    .scalar()
    return answer_4

def select_5(lecturer_name):
    answer_5 = session.query(Subject.name) \
    .join(Lecturer) \
    .filter(Lecturer.name == lecturer_name) \
    .all()
    return answer_5

def select_6(group_name):
    answer_6 = session.query(Student.name) \
    .join(Group) \
    .filter(Group.name == group_name) \
    .all()
    return answer_6

def select_7(group_name, subject_name):
    answer_7 = session.query(Student.name, Grade.grade) \
    .join(Grade) \
    .join(Group) \
    .join(Subject) \
    .filter(Group.name == group_name, Subject.name == subject_name) \
    .all()
    return answer_7

def select_8(lecturer_name):
    answer_8 = session.query(Subject.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
    .join(Grade) \
    .join(Lecturer) \
    .filter(Lecturer.name == lecturer_name) \
    .group_by(Subject.name) \
    .all()
    return answer_8

def select_9(student_name):
    answer_9 = session.query(Subject.name) \
    .join(Grade) \
    .join(Student) \
    .filter(Student.name == student_name) \
    .group_by(Subject.name) \
    .having(func.avg(Grade.grade) >= 3) \
    .all()
 
    return answer_9

def select_10(student_name, lecturer_name):
    answer_10 = session.query(Subject.name) \
    .join(Grade) \
    .join(Student) \
    .join(Lecturer) \
    .filter(Student.name == student_name, Lecturer.name == lecturer_name) \
    .all()
    return answer_10

# Checking the correctness of data download:

# print("Question number 1")
# s1 = select_1()
# print(s1)
# print()

# print("Question number 2")
# s2 = select_2('Mathematics')
# print(s2)
# print()

# print("Question number 3")
# s3 = select_3('Group A', 'Mathematics')
# print(s3)
# print()

# print("Question number 4")
# s4 = select_4('Group A')
# print(s4)
# print()

# print("Question number 5")
# s5 = select_5('Amanda Reed')
# print(s5)
# print()

# print("Question number 6")
# s6 = select_6('Group A')
# print(s6)
# print()

# print("Question number 7")
# s7 = select_7('Group A', 'Mathematics')
# print(s7)
# print()

# print("Question number 8")
# s8 = select_8('Amanda Reed')
# print(s8)
# print()

# print("Question number 9")
# s9 = select_9('James Cook')
# print(s9)
# print()

# print("Question number 10")
# s10 = select_10('James Cook', 'Amanda Reed')
# print(s10)
# print()