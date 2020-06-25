
input1=input("Enter the first string: ")
input2=input("Enter the second string: ")

lst=list(input2)
for i in input1:
    if i!=' ':
        if i in lst:
            lst.remove(i)
        else:
            print("False")
            break

else:
    print('True')