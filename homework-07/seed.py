from faker import Faker
import random
from models import Student, Group, Lecturer, Subject, Grade, session

fake = Faker()

groups = ['Group A', 'Group B', 'Group C']
for group_name in groups:
    group = Group(name=group_name)
    session.add(group)

for _ in range(5):
    lecturer = Lecturer(name=fake.name())
    session.add(lecturer)

subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History', 'English']
for subject_name in subjects:
    subject = Subject(name=subject_name, lecturer_id=random.randint(1, 5))
    session.add(subject)

for _ in range(40):
    student = Student(name=fake.name(), group_id=random.randint(1, 3))
    session.add(student)

session.commit()

for student_id in range(1, 41):
    for subject_id in range(1, 7):
        for _ in range(random.randint(10, 20)):
            grade = Grade(student_id=student_id, subject_id=subject_id, grade=random.randint(1, 6), date=fake.date_this_year(before_today=True, after_today=False))
            session.add(grade)

session.commit()
