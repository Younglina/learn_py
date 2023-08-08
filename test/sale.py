from abc import ABCMeta, abstractmethod

class Employee(metaclass = ABCMeta):
    def __init__(super, name):
        super.name = name

    @abstractmethod
    def get_salary(self):
        pass
    
class Programmer(Employee):
    
    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self.working_hour = working_hour

    def get_salary(self):
        return self.working_hour * 200
    
class Manager(Employee):
    def get_salary(self):
        return 15000.0

class Salesman(Employee):
    def __init__(self, name, sales=0):
        super().__init__(name)
        self.sales = sales
    
    def get_salary(self):
        return self.sales * 0.05 + 1800
    
emps = [
    Programmer('张三'), Manager('李四'), Salesman('王五'), Salesman('赵六'), Manager('钱七')
]

for emp in emps:
    if isinstance(emp, Programmer):
        emp.working_hour = int(input(f'{emp.name}本月工作时间：'))
    if isinstance(emp, Salesman):
        emp.sales = int(input(f'{emp.name}本月销售额：'))
    print(f'{emp.name}本月工资为:{emp.get_salary():.2f}元')