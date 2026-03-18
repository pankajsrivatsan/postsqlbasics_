from dataclasses import dataclass

@dataclass
class Employee:
    id: int
    name: str
    department: str
    salary: float
    years_experience: int
    full_time: bool

employees: list[Employee] = [
    Employee(1, "Alice", "Engineering", 95000, 5, True),
    Employee(2, "Bob", "Sales", 65000, 3, True),
    Employee(3, "Charlie", "Engineering", 110000, 8, True),
    Employee(4, "Dana", "Marketing", 70000, 4, False),
    Employee(5, "Eve", "Sales", 58000, 2, False),
    Employee(6, "Frank", "Engineering", 105000, 7, True),
    Employee(7, "Grace", "Marketing", 75000, 5, True),
    Employee(8, "Henry", "Sales", 72000, 6, True),
    Employee(9, "Ivy", "Engineering", 98000, 4, True),
    Employee(10, "Jack", "Marketing", 68000, 3, False)
]

def get_employee_calculations():
   total_employees= len(employees)

   #overall:
   average_salary=round(sum(s.salary for s in employees)/len(employees),2)if employees else 0
   highest_salary=max(s.salary for s in employees)
   lowest_salary=min(s.salary for s in employees)
   average_years_exp=round(sum(s.years_experience for s in employees)/len(employees),2) if employees else 0

   #by_department
   eng_avg=[s for s in employees if s.department=="Engineering"]
   sales_avg=[s for s in employees if s.department=="Sales"]
   marketing_avg=[s for s in employees if s.department =="Marketing"]

   #actual avg for the above one. 
   eng_avg_salary=round(sum(s.salary for s in eng_avg)/len(eng_avg),2)if eng_avg else 0
   sales_avg_salary=round(sum(s.salary for s in sales_avg)/len(sales_avg),2) if sales_avg else 0
   marketing_avg_salary=round(sum(s.salary for s in marketing_avg)/len(marketing_avg),2) if marketing_avg else 0

   #by_employment type
   full_time_avg=[s for s in employees if s.full_time]
   part_time_avg=[s for s in employees if not s.full_time]

   #actual avg
   full_time_avg_salary=round(sum(s.salary for s in full_time_avg)/len(full_time_avg),2) if full_time_avg else 0 
   part_time_avg_salary=round(sum(s.salary for s in part_time_avg)/len(part_time_avg),2) if part_time_avg else 0

   #by_experience
   most_experienced=max(s.years_experience for s in employees)
   least_experienced=min(s.years_experience for s in employees)

   return {
       "overall":{
           "total_employees":total_employees,
           "average_salary":average_salary,
           "highest_salary":highest_salary,
           "lowest_salary":lowest_salary,
           "average_years_of_experience": average_years_exp
       },
       "by_department":{
           "eng_avg_salary":eng_avg_salary,
           "sales_avg_salary:": sales_avg_salary,
           "marketing_avg_salary": marketing_avg_salary
       },
       "by_employment_type":{
           "full_time_avg_salary":full_time_avg_salary,
           "part_time_avg_salary":part_time_avg_salary
       },
       "experience":{
           "most_experienced":most_experienced,
           "least_experienced":least_experienced
       }
   }

calc=get_employee_calculations()
print(calc)


