import random
import csv

first_list = 'Sophia','Jackson','Flimingo'
last_list = 'THOMPSON', 'ANDERSON'
pay_list = 20000,40000,5000,6000,7000
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

#emp_1 = Employee('Corey', 'Schafer', 50000)
#emp_2 = Employee('Micah', 'Kryzer', 70000)

emp_1 = Employee(random.choice(first_list), random.choice(last_list), random.choice(pay_list))
emp_2 = Employee(random.choice(first_list), random.choice(last_list), random.choice(pay_list))

print(emp_1.email)
print(emp_2.email)
