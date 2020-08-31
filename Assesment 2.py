

inpu = list(map(int,input('Enter an array:').split(',')))
sample = inpu
sum = int(input('Enter the sum: '))
count =0
pair = []
for i in inpu:
    sample.remove(i)
    for j in sample:
        if j + i == sum:

            count += 1
            p= '({},{})'.format(i, j)
            if p not in pair:
                pair.append(p)
    sample.append(i)
print(count//2)
print(pair)