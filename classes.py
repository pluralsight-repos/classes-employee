class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def __str__(self):
        return f"{self.name} is {self.age} year old. Employee is a {self.position} with the salary of ${self.salary}"
    
    def __repr__(self):
        return (
            f"Employee("
            f"{repr(self.name)},{repr(self.age)},{repr(self.position)},{repr(self.salary)})"
        )
    
        


employee1 = Employee("Jin-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)
# Employee.increase_salary(employee2, 20)
# Employee.info(employee2)
print(eval(repr(employee1)))
