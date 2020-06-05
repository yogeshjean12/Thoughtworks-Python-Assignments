#Obtain the domain (hackerrank.com) name from the URL
'''The URL parsing functions focus on splitting a URL string into its components'''
from urllib.parse import urlparse

t = urlparse('https://www.hackerrank.com/domains/python').netloc #fetch (www.hackerrank.com) from the URL
'''This line first split the t in the bases of . 
and slice it and finally join it with . with the help of join function'''
print('.'.join(t.split('.')[1:]))