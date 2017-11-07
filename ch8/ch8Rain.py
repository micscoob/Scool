rainfalls = []
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']


def print_menu():
    print(30 * '-', 'MENU', 30 * '-')
    print('1. Enter data')
    print('2. Display the data you entered')
    print('3. Display the years total and avrage')
    print('4. Display the highest and lowest months')
    print('5. Exit')
    print(67 * '-')


def enter_data():
    loop1 = 1
    while loop1 != 13:
        tmp = float(input('Enter total amount of rainfall in inches for month %d:\n' % loop1))
        rainfalls.append(tmp)
        loop1 += 1


def total_avg():
    total = sum(rainfalls)
    year_avg = total / 12
    print('The years total is %d incehs' % total)
    print('The avrage for the year is %d inches' % year_avg)


def max_low():
    # Try len
    maxs = max(rainfalls)
    max_month = months[rainfalls.index(maxs)]
    lows = min(rainfalls)
    low_month = months[rainfalls.index(lows)]
    print('The highest amount of rainfall is in %s with %d inches.\
    \nThe lowest is in %s with %d incehes.' % (max_month, maxs, low_month, lows))


loop = True

while loop:
    print_menu()
    choice = int(input("Enter your choice [1-5]: "))

    if choice == 1:
        enter_data()
    elif choice == 2:
        print(rainfalls)

    elif choice == 3:
        total_avg()

    elif choice == 4:
        max_low()

    elif choice == 5:
        print("End")

        loop = False
    else:

        input("Wrong option selection. Enter any key to try again..")
