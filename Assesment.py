

input = input('Enter the color: ').upper()
original = ['R','B','G']
lst = list(input)
sample = lst
count = 0

for i in lst:
    lst.remove(i)
    for j in lst:
        if i in j:

            count += 1

if count == 3:
    print('True')

else:
    print('False')

