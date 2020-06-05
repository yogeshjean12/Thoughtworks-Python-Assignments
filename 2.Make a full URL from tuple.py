#Make a full URL from tuple
tup = ('www', 'hackerrank', 'com', 'domains', 'python')
index=0
for i in tup:#Using for loop fetching one by one and applying conditions
    if 'www'==i :
        print('/{}.'.format(i), end='')
    elif 'com'==i:
        print('.{}'.format(i), end='')
    elif 'www'==tup[index-1] and 'com'==tup[index+1]:
        print('{}'.format(i), end='')
    else:
        print('/{}'.format(i), end='')

    index+=1






