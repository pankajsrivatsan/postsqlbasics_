from dataclasses import dataclass
from typing import Optional

@dataclass
class Student:
    student_id: int
    name: str
    email: str
    major: str
    gpa: float

@dataclass
class Course:
    course_id: int
    name: str
    credits: int
    department: str

@dataclass
class Teacher:
    teacher_id: int
    name: str
    department: str
    years_exp: int

@dataclass
class Enrollment:
    enrollment_id: int
    student_id: int    # ← FOREIGN KEY 1
    course_id: int     # ← FOREIGN KEY 2
    teacher_id: int    # ← FOREIGN KEY 3
    semester: str
    grade: str  # "A", "B", "C", etc. or "In Progress"

# DATA
students = [
    Student(1, "Alice Chen", "alice@uni.edu", "Computer Science", 3.8),
    Student(2, "Bob Smith", "bob@uni.edu", "Mathematics", 3.5),
    Student(3, "Charlie Lee", "charlie@uni.edu", "Physics", 3.9),
]

courses = [
    Course(101, "Data Structures", 4, "Computer Science"),
    Course(102, "Calculus II", 4, "Mathematics"),
    Course(103, "Quantum Physics", 3, "Physics"),
    Course(104, "Web Development", 3, "Computer Science"),
]

teachers = [
    Teacher(1, "Dr. Johnson", "Computer Science", 15),
    Teacher(2, "Prof. Williams", "Mathematics", 20),
    Teacher(3, "Dr. Brown", "Physics", 12),
]

enrollments = [
    Enrollment(1, 1, 101, 1, "Fall 2024", "A"),
    Enrollment(2, 1, 104, 1, "Fall 2024", "B+"),
    Enrollment(3, 2, 102, 2, "Fall 2024", "A-"),
    Enrollment(4, 3, 103, 3, "Fall 2024", "A"),
    Enrollment(5, 1, 102, 2, "Spring 2025", "In Progress"),
]

def get_student_by_id(student_id: int) -> Optional[Student]:
    for student in students:
        if student.student_id== student_id:
            return student
    return None
   

def get_course_by_id(course_id: int) -> Optional[Course]:
    for course in courses:
        if course.course_id==course_id:
            return course
    return None
  

def get_teacher_by_id(teacher_id: int) -> Optional[Teacher]:
    for teacher in teachers:
        if teacher.teacher_id==teacher_id:
            return teacher
    return None

    

def get_enrollment_by_id(enrollment_id: int) -> Optional[Enrollment]:
    for enrollment in enrollments:
        if enrollment.enrollment_id==enrollment_id:
            return enrollment
    return None

  

def get_enrollment_details(enrollment_id: int):
    enrollment=get_enrollment_by_id(enrollment_id)
    if not enrollment:
        return None
    
    student=get_student_by_id(enrollment.student_id)
    course=get_course_by_id(enrollment.course_id)
    teacher=get_teacher_by_id(enrollment.teacher_id)

    #calculations part mtf!
    gpa_map={
        "a":4.0,
        "a-":3.7,
        "b":3.0,
        "b-":2.7,
        "c+":2.3,
        "c":2.0,
        "in_progress":None

    }
    gpa_impact=gpa_map.get(enrollment.grade.lower(),None)

    #workload:
    if course.credits >=4:
        workload="heavy"
    elif course.credits==3:
        workload="moderate"
    else:
        workload="light"

    return {
        "enrollment":enrollment,
        "student":student,
        "course":course,
        "teacher":teacher,
        "details":{
            "gpa_impact":gpa_impact,
            "workload":workload
        }
    }
   

# TEST IT
result = get_enrollment_details(1)
if result:
    print(f"=== ENROLLMENT #{result['enrollment'].enrollment_id} ===")
    print(f"\nStudent:")
    print(f"  Name: {result['student'].name}")
    print(f"  Email: {result['student'].email}")
    print(f"  Major: {result['student'].major}")
    print(f"  Current GPA: {result['student'].gpa:.2f}")
    
    print(f"\nCourse:")
    print(f"  Name: {result['course'].name}")
    print(f"  Credits: {result['course'].credits}")
    print(f"  Department: {result['course'].department}")
    
    print(f"\nTeacher:")
    print(f"  Name: {result['teacher'].name}")
    print(f"  Department: {result['teacher'].department}")
    print(f"  Experience: {result['teacher'].years_exp} years")
    
    print(f"\nEnrollment Details:")
    print(f"  Semester: {result['enrollment'].semester}")
    print(f"  Grade: {result['enrollment'].grade}")
    print(f"  GPA Impact: {result['details']['gpa_impact']}")
    print(f"  Workload: {result['details']['workload']}")
