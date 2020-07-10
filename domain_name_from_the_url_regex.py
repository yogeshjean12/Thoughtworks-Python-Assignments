# domain name from the URL using regex
import re
a=re.search(r'https?://([A-Za-z_0-9.-]+).*',input("Enter the URL: "))
print(a.group(1))
