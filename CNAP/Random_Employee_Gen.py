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

class Users:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

def exportUsers(filename):
    with open(filename, 'w') as filename:
        fields = [
                "first_name",
                "last_name",
                "ssn_list",
                "email_list",
                "username_list",
                ]
        wr = csv.DictWriter(filename, delimiter=",", quoting=csv.QUOTE_ALL, fieldnames=fields)
        wr.writerow({
            "first_name": first_nam,
            "last_name": last_nam,
            "ssn_list": ssn_list,
            "email_list": email_list,
            "username_list": email_list,
            })

exportUsers('test_list_pls_ignore.csv')
