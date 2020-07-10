# detect floating point number using regex
import re
a=re.search(r"[+-]?[0-9]*\.[0-9]+",input("Enter the number: "))
if a:
    print("True")
else:
    print("False")