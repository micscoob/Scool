import random
import csv
from faker import Faker
fake = Faker()
#List for each catagory
first_nam = []
last_nam = []
ssn_list = []
email_list = []
username_list = []
######Company Email####
company = '@mycompany.com'

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

    for _ in range(100):
    first = fake.first_name()
    last = fake.last_name()
    ssn = fake.ssn()
    email = first + '.' + last + company
    username = fake.user_name()
    
    first_nam.append(first)
    last_nam.append(last)
    ssn_list.append(ssn)
    email_list.append(email)
    username_list.append(username)

    
