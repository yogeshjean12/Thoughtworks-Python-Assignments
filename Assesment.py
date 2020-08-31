

input = input('Enter the color: ').upper()
print(input)
lst = list(input)
sample = lst
count =0



for i in lst:
    sample.remove(i)
    for j in sample:
        if j in i:
            count += 1
print(count)

