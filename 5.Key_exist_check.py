#Find the number of ways to find whether a key exists in a dictionary or not
#Method 1
def key_check_Approach1(dict, key):
    if key in dict.keys():
        print("key is exist")
    else:
        print("Not exist")
#Method 2
def key_check_Approach2(dict, key):
    if key in dict:
        print("key is exist")
    else:
        print("Not exist")

dict = {'a': 100, 'b': 200, 'c': 300}
key = 'b'
key_check_Approach1(dict, key)
key = 'd'
key_check_Approach2(dict, key)