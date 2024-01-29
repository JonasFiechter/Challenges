from src.components.employee import Employee
from src.interfaces.isystem import ISystem
from src.services.data import Data


class EmployeeManagementSystem(ISystem):
    def __init__(self, *args, **kwargs):
        self.temp_data = set()

    def get_employee(self, emp_id) -> Employee:
        for employee in self.temp_data:
            if employee.emp_id == emp_id:
                return employee
        raise ValueError

    def add_employee(self, emp_id, name, position, salary) -> Employee:
        emp = Employee(emp_id, name, position, salary)
        self.temp_data.add(emp)
        return self.get_employee(emp.emp_id)

    def remove_employee(self, emp_id) -> Employee:
        emp = self.get_employee(emp_id)
        self.temp_data.remove(emp)
        return emp

    def get_employee_info(self, emp_id) -> dict:
        emp = self.get_employee(emp_id)
        return emp.info()

    def update_salary(self, emp_id, new_salary) -> Employee:
        emp = self.get_employee(emp_id)
        emp.salary = new_salary
        return emp
        
    def get_all_employees(self) -> list:
        return [employee.info() for employee in self.temp_data]