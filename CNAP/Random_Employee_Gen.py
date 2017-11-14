import random
import csv
from faker import Faker

fake = Faker('en_US')

def genUsers(filename, listLength, company):
    """Generate a set of fake users with sane-sounding fake data, and export them to a .CSV."""

    with open(filename, 'w') as filename:

        wr = csv.writer(filename, delimiter=",", quoting=csv.QUOTE_ALL)

        for i in range(listLength):

            row = [] * 6 # number of fields
            first = fake.first_name()
            last = fake.last_name()
            ssn = fake.ssn()
            username = first.lower() + '.' + last.lower()
            email = username + '@' + company + '.com'
            phone = fake.phone_number()

            row.append(first + ',' + last + ',' + ssn + ',' + username + ',' + email + ',' + phone)
            wr.writerow(row)

genUsers('test_list_pls_ignore.csv', 10, 'contoso')
