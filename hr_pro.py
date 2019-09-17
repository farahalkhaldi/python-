
class Employee:
    def __init__(self,name,age,salary,employement_date):
        self.name = name
        self.age = age
        self.salary = salary
        self.employement_date = employement_date

    def get_working_years(self):
        working_year = 2019 - int(self.employement_date)
        return working_year

    def __str__(self):
        return "Name: " + self.name + " age: " + str(self.age) + " salary: " + str(self.salary) + " working years: " + str(self.get_working_years())

class Manager:
    def __init__(self,name,age,salary,manager_date,bonus_percentage):
        self.name = name
        self.age = age
        self.salary = salary
        self.manager_date = manager_date
        self.bonus_percentage = bonus_percentage

    def get_working_years(self):
        working_year = 2019 - int(self.manager_date)
        return working_year
    def get_bonus_percentage(self):
        percentage = int(self.salary) * float(self.bonus_percentage)
        return percentage

    def __str__(self):
        return "Name: " + self.name + " age: " + str(self.age) + " salary: " + str(self.salary) + " working years: " + str(self.get_working_years()) + " Bonus Percentage: " + str(self.get_bonus_percentage())


employee_list = []
managers_list = []
print("")
print("welcome to HR pro 2019")
print("")
options = ["Show Employees","Show Managers","Add An Employee","Add A MAnger","Exit"]

while(True):
    print("Options:")
    print("")
    print("1." + options[0])
    print("")
    print("2." + options[1])
    print("")
    print("3." + options[2])
    print("")
    print("4." + options[3])
    print("")
    print("5." + options[4])
    print("")

    print("-"*25)
    choice = int(input("What would you like to do? "))
    print("")
    print("-"*25)

    if choice == 1:
        for employee_object in employee_list:
            print(employee_object)
    elif choice == 2:
        for manager_object in managers_list:
            print(manager_object)

    elif choice == 3:
        name_employee            = input("Name: ")
        age_employee             = input("Age: ")
        salary_employee          = input("Salary: ")
        employment_date_employee = input("Employment Year: ")
        employee_object = Employee(name=name_employee,age=age_employee,salary=salary_employee,employement_date=employment_date_employee)
        employee_list.append(employee_object)
        print("Employee added succesfully")

    elif choice == 4:
        name_manager            = input("Name: ")
        age_manager             = input("Age: ")
        salary_manager          = input("Salary: ")
        employment_date_manager = input("Employment Year: ")
        manger_bonus_percentage = input("Bonus Percentage: ")
        manager_object = Manager(name=name_manager,age=age_manager,salary=salary_manager,manager_date=employment_date_manager,bonus_percentage=manger_bonus_percentage)
        managers_list.append(manager_object)
        print("Manager added succesfully")

    elif choice == 5:
        break
