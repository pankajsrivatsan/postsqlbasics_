from dataclasses import dataclass
from collections import defaultdict

@dataclass
class Student:
    student_id: int
    name: str
    major: str
    gpa: float
    credits: int
    scholarship: bool

students = [
    Student(1, "Alice", "Computer Science", 3.8, 90, True),
    Student(2, "Bob", "Mathematics", 3.5, 85, False),
    Student(3, "Charlie", "Computer Science", 3.9, 95, True),
    Student(4, "Diana", "Physics", 3.7, 88, True),
    Student(5, "Eve", "Mathematics", 3.6, 82, False),
    Student(6, "Frank", "Computer Science", 3.4, 78, False),
    Student(7, "Grace", "Physics", 3.9, 92, True),
    Student(8, "Henry", "Mathematics", 3.8, 90, True),
]
def analyze_by_major():
    groups=defaultdict(list)
    for student in students:
        groups[student.major].append(student)

    result={}
    for major, major_students in groups.items():
        scholar_students=len([o for o in major_students if o.scholarship])
        total_students=len(major_students)
        result[major]={
            "count":len(major_students),
            "avg_gpa":sum(o.gpa for o in major_students)/len(major_students),
            "total_credits":sum(o.credits for o in major_students),
            "scholarship_pct":(scholar_students/total_students)*100
        }
    return result



# TEST IT
result = analyze_by_major()
for major, stats in result.items():
    print(f"\n{major}:")
    print(f"  Students: {stats['count']}")
    print(f"  Avg GPA: {stats['avg_gpa']:.2f}")
    print(f"  Total Credits: {stats['total_credits']}")
    print(f"  Scholarship %: {stats['scholarship_pct']:.1f}%")