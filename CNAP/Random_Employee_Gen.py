import random
import csv
from faker import Faker

first_list = 'Sophia','Jackson','Flimingo'
last_list = 'THOMPSON', 'ANDERSON'
pay_list = 20000,40000,5000,6000,7000

class Users:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

def exportUsers(filename, listname):
    with open(filename, 'w') as filename:
        wr = csv.writer(filename, delimiter=",", quoting=csv.QUOTE_ALL)
        wr.writerow(listname)

exportUsers('test_list_pls_ignore.csv', first_list)
