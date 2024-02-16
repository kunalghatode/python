class Employee:
    __count = 0
    def __init__(self):
        Employee.__count = Employee.__count + 1
    def display(self):
        print("The number of Employees", Employee.__count)

emp = Employee()
emp1 = Employee()

try:
    print(emp.__count)
except:
    print("you can't access")
finally:
    emp.display()