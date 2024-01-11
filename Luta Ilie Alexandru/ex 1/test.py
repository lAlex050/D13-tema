class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__(self):
        Employee.empCount -= 1

    def update_salary(self, new_salary):
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Tasks with status '{status}':")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)


class Manager(Employee):
    """Class representing a manager, inheriting from Employee"""
    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = f"YourTeam_{department}"
        Manager.mgr_count += 1

    def display_employee(self):
        if Manager.mgr_count % 3 == 0:
            print(f"Name: {self.name}")
        elif Manager.mgr_count % 3 == 1:
            print(f"Salary: {self.salary}")
        else:
            print(f"Department: {self.department}")


# Exemplu de utilizare:

# X = 4, Y = 13
X = 4
Y = 13

# Creare Y/3 obiecte ale clasei Manager
managers = [Manager(f"Manager{i}", 50000 + i * 10000, f"Department{i}") for i in range(Y // 3)]

# Apelare metoda 'display_employee' pentru obiectele din clasa Manager
for manager in managers:
    manager.display_employee()

# Creare X obiecte ale clasei Employee
employees = [Employee(f"Employee{i}", 40000 + i * 10000) for i in range(X)]

# Apelare metoda 'display_employee' pentru obiectele din clasa Employee
for employee in employees:
    employee.display_employee()

# Afișare valoarea atributului empCount pentru o instanță a clasei Employee și pentru una a clasei Manager
employees[0].display_emp_count()
managers[0].display_emp_count()