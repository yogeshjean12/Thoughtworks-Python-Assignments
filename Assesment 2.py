

inpu = list(map(int,input('Enter an array:').split(',')))
sample = inpu
sum = int(input('Enter the sum: '))
count =0
for i in inpu:
    sample.remove(i)
    for j in sample:
        if j + i == sum:
            count += 1
    sample.append(i)
print(count//2)