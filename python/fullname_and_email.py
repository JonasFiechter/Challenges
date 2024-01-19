'''
Create the instance attributes fullname and email in the Employee class. Given 
a person's first and last names:

Form the fullname by simply joining the first and last name together, separated 
by a space.
Form the email by joining the first and last name together with a . in between, 
and follow it with @company.com at the end. Make sure the entire email is in 
lowercase.

Examples
emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")
emp_1.fullname ➞ "John Smith"

emp_2.email ➞ "mary.sue@company.com"

emp_3.firstname ➞ "Antony"
Notes
The attributes firstname and lastname are already made for you.
See the Resources tab for some helpful tutorials on Python classes!
'''

class Employee():
    def __init__(self, f_name:str, l_name:str):
        self.firstname = f_name
        self.lastname = l_name
        self.fullname = f_name.capitalize() + ' ' + l_name.capitalize()
        self.domain = 'company.com'
        self.email = f_name.lower() + '.' + l_name.lower() + '@' + self.domain

emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")

print(
    emp_1.fullname,
    emp_2.email,
    emp_3.firstname
)