name=input("Enter your name: ")
age=int(input("Enter your age: "))
file=open('my_info.txt','w')
file.write('My name is {}\n'.format(name))
file.write('I\'m {} years old\n'.format(age))
degree=input('Enter your degree')
file=open('my_info.txt','a')
file.write('I have done my B.E in {}'.format(degree))
file=open('my_info.txt','r')
for i in file.readlines():
    print(i)

file.close()
