no_of_rows=int(input('Enter the number of rows and enter only even number: '))
no_of_stars=1
if no_of_rows%2!=0:
    for i in range(no_of_rows//2+1):
        for j in range(no_of_stars):
            print('*',end='')
        no_of_stars+=2
        print()

    no_of_stars-=4
    for i in range(no_of_rows//2):
        for j in range(no_of_stars):
            print('*',end='')
        no_of_stars-=2
        print()
else:
    print('Enter a valid Odd number')