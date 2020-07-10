# find tha average of marks and print the avg mark and student name using arguments in function.
def average(name,*marks):
    total=sum(list(marks))
    ave=total/len(marks)
    print(name,'-',ave)

average('yogesh',89,82,92,95,99)