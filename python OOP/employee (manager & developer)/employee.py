import csv


class Employee:
    def __init__(self, name: str, salary: int) -> None:
        self.name = name
        self.salary = salary

    def __str__(self) -> str:
        return f'Name: {self.name}, salary: {self.salary}'

    @staticmethod
    def calculate_total_salary(employees):
        total_salary = sum(employee.salary for employee in employees)
        return total_salary

    @staticmethod
    def save_total_salary_to_csv(employees, filename):
        total_salary = Employee.calculate_total_salary(employees)
        with open(filename, 'a', newline='') as file:
            csv.writer(file).writerow(['', '', '', '', total_salary])

