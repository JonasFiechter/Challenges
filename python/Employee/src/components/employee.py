class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
    
    def info(self) -> dict:
        return {k: v for k, v in self.__dict__.items()}