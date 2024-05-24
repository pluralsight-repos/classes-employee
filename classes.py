class Employee:
    __slots__ = ("name", "age", "salary")

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def has_slots(self):
        return hasattr(self, "__slots__")

class SlotsInspectorMixin:
    __slots__ = ()
    
    def has_slots(self):
        return hasattr(self, "__slots__")

class Developer(SlotsInspectorMixin, Employee):
    __slots__ = ("framework", )

    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        # Employee.increase_salary(self, percent)
        self.salary += bonus

# employee1 = Tester("Lauren", 44, 1000)
employee2 = Developer("Ji-Soo", 38, 1000, "Flask")

# print(employee2.has_slots())
# # Method Resolution Order
# print(Developer.__mro__)
print(employee2.__dict__)

