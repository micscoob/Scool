dic_1 = {'A':1,'B':2,'C':3}

user = input('Enter A B or C and see the value for it\n').upper()

print('\nheres your value:',dic_1.get(user, 'N/A'))

dic_2 = {'D': 3, 'E': 4, 'F': 5}

print('\ntry our new and imporoved dictionary! with twice as many values!\n')
user = input('Enter A, B, C, D, E, or F and see the value!\n').upper()

dic_1.update(dic_2)

print('\nheres your new and improved value:',dic_1.pop(user, 'N/A'))

print('\nand heres the dictionary without your value:\n', dic_1)



