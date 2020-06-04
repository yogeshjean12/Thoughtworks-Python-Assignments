#Finding the index of the number in the list
def find_index(target_no=None,list_of_numbers=None):
    if list_of_numbers==None:
        list_of_numbers= [1,2,4,5,1,1,4,1,56]
    if target_no==None:
        target_no=1
    index=0
    for i in list_of_numbers:
        if i==target_no:
            print('{} present in the index: {}'.format(target_no,index))
        index+=1

'''Enter the target number and list of numbers seperated by comma inside the paranthesis respectively 
or leave it blank for the default value'''
find_index()