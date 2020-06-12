#Print all numbers that are completely divisible by 75 and 100 in a range from 200 to 1500 (both numbers are inclusive)
starting_no=int(input('Enter the starting number'))
ending_no=int(input('Enter the ending number'))

for i in range(starting_no,ending_no+1):
    if i%75==0 and i%100==0:
        print(i)
