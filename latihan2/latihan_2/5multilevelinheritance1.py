class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name\t\t: {self.name}")
        print(f"Age\t\t: {self.age}")


class Employee(Person):

    def __init__(self, name, age, id, salary):
        super().__init__(name, age)
        self.id = id
        self.salary = salary

    def get_details(self):
        super().get_details()
        print(f"ID\t\t: {self.id}")
        print(f"Salary\t\t: {self.salary}")


class Manager(Employee):

    def __init__(self, name, age, id, salary, department):
        super().__init__(name, age, id, salary)
        self.department = department

    def get_details(self):
        super().get_details()
        print(f"Department\t: {self.department}")


manager = Manager('Nisa Maharani', '25th', '123', 'Rp. 50jt', 'Information & Technology')
manager.get_details()