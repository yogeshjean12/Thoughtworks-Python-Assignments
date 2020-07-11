num=int(input('Enter the number: '))
cube=int(input('Enter its cube: '))
lambda_func = lambda x: True if x**3 == cube else False
print(lambda_func(num))
