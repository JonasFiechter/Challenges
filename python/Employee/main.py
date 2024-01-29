'''
Problem Statement: Employee Management System

Create a simple Employee Management System using Python classes. Each employee 
should have the following attributes:

    Employee ID (unique identifier)
    Name
    Position
    Salary

Implement the following functionalities:

    Add Employee: Create a method to add a new employee to the system. Ensure 
    that the Employee ID is unique.

    Remove Employee: Create a method to remove an employee from the system based 
    on their Employee ID.

    View Employee Information: Create a method to view the information of a 
    specific employee based on their Employee ID.

    Update Salary: Create a method to update the salary of an employee based on 
    their Employee ID.

    View All Employees: Create a method to view the information of all employees 
    in the system.

python
'''
from src.components.system import EmployeeManagementSystem
from src.components.vsystem import VerboseEmployeeManagementSystem


def main(verbosity=None):
    if verbosity:
        ems = VerboseEmployeeManagementSystem(verbosity=verbosity)
    else:
        ems = EmployeeManagementSystem()
    commands = [
        ems.add_employee(1, "John Doe", "Developer", 60000),
        ems.add_employee(2, "Jane Smith", "Manager", 80000),
        ems.get_all_employees(),
        ems.remove_employee(2),
        ems.get_all_employees(),
        ems.update_salary(1, 65000),
        ems.get_employee_info(1)
    ]
    for command in commands:
        ...

if __name__ == '__main__':
    main(verbosity='INFO')