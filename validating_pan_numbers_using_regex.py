# Write a program for validating PAN numbers using re module
import re
a=re.search(r"[A-Z]{5}[0-9]{4}[A-Z]{1}",input('Enter the PAN number'))
if a:
    print('True')
else:
    print('False')
