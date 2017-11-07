lists = [1,5,3,4,7,6,2,8,9,10]


sorted_list = sorted(lists)
max_in_list = max(lists)
min_in_list = min(lists)



print('This is the list:\n',lists)
print('This is the list sorted:\n',sorted_list)
print('This is the max of the list %d' %max_in_list)
print('This is the min of the list %d\n' % min_in_list)
appends = int(input('This is an example of appending a number\nEnter a number:\n'))
lists.append(appends)
print('Heres your new list:\n',lists)
