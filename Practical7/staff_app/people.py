
# Import Department from the same package
from .department import Department


# Parent class
class Person:

    def __init__(self, name):
        if not name.strip():
            raise ValueError("Name cannot be blank")

        self.name = name

    def describe(self):
        return f"Person: {self.name}"


# Employee inherits from Person
class Employee(Person):

    def __init__(self, name, employee_id, department):
        # Initialize the parent class
        super().__init__(name)

        self.employee_id = employee_id

        # Employee HAS-A Department
        if not isinstance(department, Department):
            raise TypeError("department must be a Department object")

        self.department = department
        self._salary = 0.0

    # Read the salary
    @property
    def salary(self):
        return self._salary

    # Validate the salary before setting it
    @salary.setter
    def salary(self, amount):
        if amount < 0:
            raise ValueError("Salary cannot be negative")

        self._salary = float(amount)

    # Override the parent's describe method
    def describe(self):
        return (
            f"Employee: {self.name}, ID: {self.employee_id}, "
            f"Department: {self.department}"
        )


# Developer inherits from Employee
class Developer(Employee):

    def __init__(self, name, employee_id, department, language):
        # Initialize the Employee class
        super().__init__(name, employee_id, department)

        self.language = language

    # Override describe() again
    def describe(self):
        return (
            f"{super().describe()}, "
            f"Role: Developer, Language: {self.language}"
        )
