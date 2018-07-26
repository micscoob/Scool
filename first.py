#went pretty simple for the first part just straight input into variable
title = input('Enter a title for the data:\n')
print('You entered: %s\n' % title)

column1 = input('Enter the column 1 header:\n')
print('You entered: %s\n' % column1)

column2 = input('Enter the column 2 header:\n')
print('You entered: %s\n' % column2)

#this section needs to be done multiple times so while loop
while True:
    #FIXME: made empty lists to store in values in later however it overwrites the values each loop so need to change postition 
    datastring = []
    dataint = []
    data = input('Enter a data point (-1 to stop input):\n')
    
    #stop looping if -1
    if data == '-1':
        break
    
    #split everything by , and make the 2nd value an int
    else:
        datalist = data.split(',')
        print('Data string: %s' % datalist[0])
        print('Data integer: %s' % datalist[1])
        datastring = datastring.append(datalist[0])
dataint = dataint.append(int(datalist[1]))
