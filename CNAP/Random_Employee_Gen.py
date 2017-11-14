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

def exportUsers(filename, listLength):
    with open(filename, 'w') as filename:
        wr = csv.writer(filename, delimiter=",", quoting=csv.QUOTE_ALL)
        for i in range(listLength):
            row = [] * listLength
            first = fake.first_name()
            last = fake.last_name()
            ssn = fake.ssn()
            email = first + '.' + last + company
            username = fake.user_name()

            row.append(first + ", " + last + ", " + ssn + ", " + email + ", " + username)
            wr.writerow(row)

exportUsers('test_list_pls_ignore.csv', 10)
