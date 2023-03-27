class Seseorang:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)

# Single Inheritance
class Mahasiswa(Seseorang):

    def __init__(self, student_id):
        self.student_id = student_id

    def get_info(self):
        super().get_info()
        print("Student ID:", self.student_id)
        
        
# Single Inheritance
class Employee(Seseorang):

    def __init__(self, name, age, address, employee_id, salary):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.salary = salary

    def get_info(self):
        super().get_info()
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


# Multiple Inheritance
class Penulis(Mahasiswa, Employee):
    
    def __init__(self, published_books, name, age, address, employee_id, salary, student_id):
        Employee.__init__(self, name, age, address, employee_id, salary)
        Mahasiswa.__init__(self, student_id)
        self.published_books = published_books

    def get_info(self):
        super().get_info()
        print("Published Books:", self.published_books)


penulis = Penulis('My Own Self', 'Nisa Maharani', '25th', 'Cirebon', '123', 'Rp. 100jt', '456')
penulis.get_info()