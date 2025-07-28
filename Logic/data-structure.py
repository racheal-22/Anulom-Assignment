from array import array

# Step 1: Define a class (like a struct)
class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def to_dict(self):
        return {
            "id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "salary": self.salary
        }

# Step 2: Create an empty list to store employees
employee_list = []

# Step 3: Take input from the user in loop
while True:
    print("\nEnter Employee Details:")
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    # Create Employee object and add to list
    emp = Employee(emp_id, name, department, salary)
    employee_list.append(emp)

    more = input("Do you want to add more employees? (yes/no): ").lower()
    if more != "yes":
        break

# Step 4: Convert employee objects to list of dicts
employee_dict_list = [emp.to_dict() for emp in employee_list]

# Step 5: Use set to get unique departments
unique_departments = set(emp["department"] for emp in employee_dict_list)

# Step 6: Use array to store all salaries
salaries = array('f', [emp["salary"] for emp in employee_dict_list])

# Step 7: Create a string with all employee names
all_names_string = ", ".join(emp["name"] for emp in employee_dict_list)

# Step 8: Display results
print("\nAll Employee Records:")
for emp in employee_dict_list:
    print(emp)

print("\nUnique Departments (Set):", unique_departments)
print("All Salaries (Array):", list(salaries))
print("All Names (String):", all_names_string)
