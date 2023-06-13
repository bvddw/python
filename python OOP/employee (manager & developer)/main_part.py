from employee import Employee
from manager import Manager
from developer import Developer
import csv


def load_data_from_csv(filename):
    employees = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            name, salary, role = row[:3]
            if role == 'Manager':
                bonus = int(row[3])
                manager = Manager(name, int(salary), bonus)
                employees.append(manager)
            elif role == 'Developer':
                programming_language = row[3]
                developer = Developer(name, int(salary), programming_language.split(', '))
                employees.append(developer)
    return employees


manager1: Manager = Manager('Bob', 2000, 500)
developer1: Developer = Developer('Jack', 2100, ['Python', 'C++', 'Java'])

employees = [manager1, developer1]

# Saving employee data in a CSV file
with open('data.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Salary', 'Role', 'Bonus/Programming Languages', 'TOTAL SALARY'])
    for employee in employees:
        if isinstance(employee, Manager):
            writer.writerow([employee.name, employee.total_salary, 'Manager', employee.bonus, employee.total_salary])
        elif isinstance(employee, Developer):
            writer.writerow([employee.name, employee.salary, 'Developer', ', '.join(employee.programming_languages), employee.salary])

# Loading employee data from a CSV file
loaded_employees = load_data_from_csv('data.csv')

# Output of information about loaded employees
for employee in loaded_employees:
    print(employee)

# Calculation and saving of the total amount of salaries of all employees in a CSV file
Employee.save_total_salary_to_csv(loaded_employees, 'data.csv')
