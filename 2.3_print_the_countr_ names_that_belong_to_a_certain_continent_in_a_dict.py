#Print all the country names that belong to a certain continent from a given dictionary
def finding_country(desired_continent,dict= None):
    if dict==None:
        dict={'Spain':'Europe', 'Japan':'Asia', 'India':'Asia', 'Italy':'Europe', 'Thailand':'Asia', 'Sudan':'Africa'}

    if desired_continent.capitalize() in dict.values():
        for key,value in dict.items():
            if value == desired_continent.capitalize():
                print(key)
    else:
        print('continent doesn\'t exist, Enter the existing continent')

desired_continent=input('Enter the desired continent: ')
finding_country(desired_continent)