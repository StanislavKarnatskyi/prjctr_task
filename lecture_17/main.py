from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    subjects = relationship('StudentSubject', back_populates='student')

class Subject(Base):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship('StudentSubject', back_populates='subject')

class StudentSubject(Base):
    __tablename__ = 'student_subject'
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)
    subject_id = Column(Integer, ForeignKey('subject.id'), primary_key=True)
    student = relationship('Student', back_populates='subjects')
    subject = relationship('Subject', back_populates='students')

engine = create_engine('postgresql://ltpck:password@localhost:5432/postgres')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

students = session.query(Student).all()
subjects = session.query(Subject).all()
student_subjects = session.query(StudentSubject).all()

print("'student':")
for student in students:
    print(student.id, student.name, student.age)

print("\n'subject':")
for subject in subjects:
    print(subject.id, subject.name)

print("\n'student_subject':")
for student_subject in student_subjects:
    print(student_subject.student_id, student_subject.subject_id)

english_students = session.query(Student.name).join(StudentSubject).join(Subject).filter(Subject.name == 'English').all()
print("\nstudents that visited 'English' classes.:")
for student in english_students:
    print(student.name)
