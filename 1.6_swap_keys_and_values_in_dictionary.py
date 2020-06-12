# Make a new dictionary in which keys become values and values become keys
old_dict= {21: "FTP", 22: "SSH", 23: "telnet", 80:"http"}
new_dict = {}
for key, value in old_dict.items():
   if True:
       #Assining value to the key in new_dict
       new_dict[value]= key
print('old_dict: ',old_dict)
print('new_dict:',new_dict)
