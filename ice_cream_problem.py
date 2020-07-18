
flavours = {'chocolate': 250, 'vanilla': 150, 'strawberry': 350}
toppings = {'choco chips': 30, 'caramel': 50, 'nuts': 40}
types = {'cup': 100, 'cone': 120, 'stick': 50}

def menu():
    print('\n                         MENU CARD                                    \n')
    for type in types:
        for flavour in flavours:
            print('        {} {} ice cream price: {} rupees'.format(flavour, type, types[type] + flavours[flavour]))
    print('                         _ _ _ _ _                                       ')
def take_order():
    ice_cream_flavour, ice_cream_type = input('\nWhich ice cream you want? (Eg.chocolate cup): ').lower().strip().split()
    quantity = int(input('How many {} {} ice cream you want? (Eg.2) : '.format(ice_cream_flavour, ice_cream_type)))
    if ice_cream_flavour == 'chocolate':
        option = input('Do you want toppings? (yes-y,no-n) print y or n : ').lower().strip()
        if option == 'y':
            print('Available toppings are: \n')
            for item in toppings:
                print('{} price is: {} rupees'.format(item, toppings[item]))
            topping = input('\nwhich one do you want? (Eg.caramel) : ').lower().strip()
            return '\n{} {} {} ice cream with {} toppings price is: {} rupees'.format(quantity, ice_cream_flavour, ice_cream_type, topping, (flavours[ice_cream_flavour] + types[ice_cream_type] + toppings[topping]) * quantity)
        else:
            return '\n{} {} {} ice cream price is: {} rupees'.format(quantity, ice_cream_flavour, ice_cream_type, (flavours[ice_cream_flavour] + types[ice_cream_type]) * quantity)

    else:
        return '\n{} {} {} ice cream price is: {} rupees'.format(quantity, ice_cream_flavour, ice_cream_type, (flavours[ice_cream_flavour] + types[ice_cream_type]) * quantity)

menu()
bill = take_order()
print(bill)
print('\n                   Thank you, come again!')