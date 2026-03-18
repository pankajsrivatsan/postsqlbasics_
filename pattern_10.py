students = [
    {"name": "alice",   "grade": "A", "subject": "math",    "score": 95, "age": 20},
    {"name": "bob",     "grade": "B", "subject": "science", "score": 72, "age": 21},
    {"name": "carol",   "grade": "A", "subject": "math",    "score": 88, "age": 20},
    {"name": "david",   "grade": "C", "subject": "english", "score": 61, "age": 22},
    {"name": "eve",     "grade": "B", "subject": "math",    "score": 65, "age": 21},
    {"name": "frank",   "grade": "C", "subject": "science", "score": 58, "age": 22},
    {"name": "grace",   "grade": "A", "subject": "english", "score": 91, "age": 20},
    {"name": "henry",   "grade": "B", "subject": "english", "score": 78, "age": 23},
    {"name": "isla",    "grade": "C", "subject": "math",    "score": 63, "age": 21},
    {"name": "jake",    "grade": "A", "subject": "science", "score": 89, "age": 22},
]

#examples: 1 basic group by
def group_by_students(students):
    result={}
    for student in students:
        grade=student["grade"]

        if grade not in result:
            result[grade]=[]
        result[grade].append(student)
    return result

  
count=group_by_students(students)
for grade, student_stuff in count.items():
    name=[s["name"] for s in student_stuff]
    print(f"{grade}: {name}")



def count_per_grade(students):
    groups = group_by_students(students)  # line 1: reuse example 1 to get buckets
                                       #         groups = {"A": [...], "B": [...], "C": [...]}

    result = {}                        # line 2: new dict to hold counts

    for grade, members in groups.items():   # line 3: walk through each bucket
        result[grade] = len(members)        # line 4: count how many students are in it

    return result                      # line 5: return {"A": 4, "B": 3, "C": 3}

# ── TRACE ──────────────────────────────────────────────────────
#
#  groups = {"A": [alice,carol,grace,jake],
#            "B": [bob,eve,henry],
#            "C": [david,frank,isla]}
#
#  grade="A", members=[alice,carol,grace,jake] → len = 4
#  grade="B", members=[bob,eve,henry]          → len = 3
#  grade="C", members=[david,frank,isla]       → len = 3
#
#  result = {"A": 4, "B": 3, "C": 3}
#
# ───────────────────────────────────────────────────────────────

counts = count_per_grade(students)
for grade, count in counts.items():
    print(f"  Grade {grade}: {count} students")



