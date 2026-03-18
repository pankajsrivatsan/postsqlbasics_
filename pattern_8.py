from dataclasses import dataclass

@dataclass
class Student:
    id: int
    name: str
    major: str
    grade: float
    active: bool

students: list[Student] = [
    Student(1, "Alice", "CS", 92.5, True),
    Student(2, "Bob", "Math", 78.3, True),
    Student(3, "Charlie", "CS", 85.7, False),
    Student(4, "Dana", "Physics", 95.2, True),
    Student(5, "Eve", "CS", 88.9, True),
    Student(6, "Frank", "Math", 91.4, True),
    Student(7, "Grace", "Physics", 76.8, False),
    Student(8, "Henry", "CS", 89.6, True),
    Student(9, "Ivy", "Math", 93.7, True),
    Student(10, "Jack", "Physics", 81.2, True),
    Student(11, "Kate", "CS", 87.5, True),
    Student(12, "Leo", "Math", 94.8, True),
    Student(13, "Mia", "Physics", 79.3, False),
    Student(14, "Noah", "CS", 90.1, True),
    Student(15, "Olivia", "Math", 86.4, True),
    Student(16, "Paul", "Physics", 92.9, True),
    Student(17, "Quinn", "CS", 77.6, False),
    Student(18, "Ryan", "Math", 88.2, True),
    Student(19, "Sara", "Physics", 91.8, True),
    Student(20, "Tom", "CS", 83.5, True)
]

def get_student_stats():
    #get comprehensive student statistics..
    total=len(students)
    active_count=len([s for s in students if s.active])
    inactive_count=len([s for s in students if not s.active])

    #step: 3 count by major
    cs_count= len([s for s in students if s.major == "CS"])
    math_count=len([s for s in students if s.major =="Math"])
    physics_count=len([s for s in students if s.major == "Physics"])

    #step:4 count by grade ranges
    high_performers=len([s for s in students if s.grade <=90])
    good_students=len([s for s in students if 80 <= s.grade <90])
    struggling_students=len([s for s in students if s.grade <80])

    #step: 5 calculate percentages (safe division)
    active_percent=(cs_count/ total*100) if total >0 else 0 
    inactive_percent=(inactive_count/total*100) if total>0 else 0

    cs_present=(cs_count/total*100) if total >0 else 0
    math_present=(math_count/ total * 100 ) if total >0 else 0 
    physics_present=(physics_count/total * 100) if total > 0 else 0 

    high_percent=(high_performers/total*100) if total >0 else 0 


    #step : 6 return everything that u did
    return {
        "total_students":total,
        "by_status":{
            "active":active_count,
            "inactive":inactive_count,
            "active_percent":round(active_percent,1),
            "inactive_percent":round(inactive_percent,1),

        },
        "by_major":{
            "CS": cs_count,
            "Math":math_count,
            "physics":physics_count,
            "cs_percent": round(cs_present,1),
            "math_percent" :round(math_present,1),
            "physics_percent": round(physics_present,1)

        },
        "by_performance":{
            "high_performers":high_performers,
            "good_students":good_students,
            "struggling":struggling_students,
            "high_percent":round(high_percent, 1)
        }
    }

stats= get_student_stats()

print("test1")
print(f"total_students: {stats['total_students']}")

print("by status")
print(f"active: {stats['by_status']['active']} ({stats['by_status']['active_percent']})")
print(f"{stats['by_status']['inactive']} ({stats['by_status']['inactive_percent']})")


print(f"\n🎓 BY MAJOR:")
print(f"   CS:      {stats['by_major']['CS']} ({stats['by_major']['cs_percent']}%)")
print(f"   Math:    {stats['by_major']['Math']} ({stats['by_major']['math_percent']}%)")
print(f"   Physics: {stats['by_major']['physics']} ({stats['by_major']['physics_percent']}%)")

print(f"\n⭐ BY PERFORMANCE:")
print(f"   High Performers (≥90): {stats['by_performance']['high_performers']} ({stats['by_performance']['high_percent']}%)")
print(f"   Good Students (80-89): {stats['by_performance']['good_students']}")
print(f"   Struggling (<80):      {stats['by_performance']['struggling']}")