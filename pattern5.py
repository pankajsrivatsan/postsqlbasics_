from dataclasses import dataclass

@dataclass
class Employee:
    id: int
    name: str
    department: str
    salary: int
    experience_years: int

employees: list[Employee] = [
    Employee(1, "pankaj", "hr", 50000, 3),
    Employee(2, "san", "hr", 60000, 5),
    Employee(3, "ids", "hr", 70000, 10),  # ✅ Fixed ID
    Employee(4, "hms", "sales", 55000, 4),
    Employee(5, "sha", "sales", 65000, 4),
    Employee(6, "pol", "sales", 75000, 8),
    Employee(7, "phan", "engi", 48848, 2),
    Employee(8, "uio", "engi", 43233, 8),
    Employee(9, "asd", "engi", 90000, 12),
    Employee(10, "asdd", "maket", 49999, 1),
    Employee(11, "asee", "maket", 49999, 3),
    Employee(12, "kkk", "maket", 99999, 8)
]

def get_employees_sorted(sort_by: str, order: str = "asc") -> list[Employee]:
    """Sort employees by any field."""
    reverse = order == "desc"
    return sorted(employees, key=lambda e: getattr(e, sort_by), reverse=reverse)

def get_top_n_earners(n: int) -> list[Employee]:  # ✅ Removed unnecessary parameter
    """Get top N earners by salary (highest first)."""
    sorted_employees = sorted(employees, key=lambda e: e.salary, reverse=True)
    return sorted_employees[:n]

def get_most_experienced(n: int) -> list[Employee]:  # ✅ Removed unnecessary parameter
    """Get top N most experienced employees."""
    sorted_employees = sorted(employees, key=lambda e: e.experience_years, reverse=True)
    return sorted_employees[:n]

# Tests
print("Test 1: By salary (highest first)")
print([f"{e.name} - ${e.salary}" for e in get_employees_sorted("salary", "desc")])

print("\nTest 2: By name (A-Z)")
print([e.name for e in get_employees_sorted("name", "asc")])

print("\nTest 3: Top 3 earners")
print([f"{e.name} - ${e.salary}" for e in get_top_n_earners(3)])

print("\nTest 4: Top 5 most experienced")
print([f"{e.name} - {e.experience_years} years" for e in get_most_experienced(5)])

print("\nTest 5: By experience (lowest first)")
print([f"{e.name} - {e.experience_years} years" for e in get_employees_sorted("experience_years", "asc")])