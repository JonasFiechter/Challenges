from src.interfaces.isystem import ISystem
from src.components.employee import Employee
from src.mixins.output import VerboseMixin


class VerboseEmployeeManagementSystem(ISystem, VerboseMixin):
    def __init__(self, *args, **kwargs):
        self.temp_data = set()
        self.verbosity = kwargs['verbosity']

    def get_employee(self, emp_id) -> Employee:
        for employee in self.temp_data:
            self.print_output(self.verbosity, employee.__repr__(), employee.__str__())
            if employee.emp_id == emp_id:
                return employee

        self.print_output(self.verbosity, ValueError)
        raise ValueError

    def add_employee(self, emp_id, name, position, salary) -> Employee:
        emp = Employee(emp_id, name, position, salary)
        self.temp_data.add(emp)
        self.print_output(self.verbosity, self.__repr__())
        return self.get_employee(emp.emp_id)

    def remove_employee(self, emp_id) -> Employee:
        emp = self.get_employee(emp_id)
        self.temp_data.remove(emp)
        self.print_output(self.verbosity)
        return emp

    def get_employee_info(self, emp_id) -> dict:
        emp = self.get_employee(emp_id)
        self.print_output(self.verbosity)
        return emp.info()

    def update_salary(self, emp_id, new_salary) -> Employee:
        emp = self.get_employee(emp_id)
        emp.salary = new_salary
        self.print_output(self.verbosity)
        return emp
        
    def get_all_employees(self) -> list:
        self.print_output(self.verbosity)
        return [employee.info() for employee in self.temp_data]