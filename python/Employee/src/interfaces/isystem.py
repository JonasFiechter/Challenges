from abc import ABC, abstractmethod
from src.components.employee import Employee

class ISystem(ABC):
    @abstractmethod
    def add_employee(self, emp_id, name, position, salary) -> Employee:
        ...
        
    @abstractmethod
    def remove_employee(self, emp_id) -> Employee:
        ...

    @abstractmethod
    def get_employee_info(self, emp_id) -> dict:
        ...

    @abstractmethod
    def update_salary(self, emp_id, new_salary) -> Employee:
        ...

    @abstractmethod
    def get_all_employees(self) -> list:
        ...