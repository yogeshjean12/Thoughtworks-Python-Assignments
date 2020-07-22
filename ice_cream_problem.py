
class Type:
    def __init__(self, type, type_cost):
        self.type = type
        self.type_cost = type_cost

class Flavour:
    def __init__(self, flavour, flavour_cost):
        self.flavour = flavour
        self.flavour_cost = flavour_cost

class Topping:
    def __init__(self, topping, topping_cost):
        self.topping = topping
        self.topping_cost = topping_cost

    def get_topping_cost(self):
        return self.topping_cost

    def get_topping_name(self):
        return self.topping

class IceCream:
    '''Ice cream details'''

    def __init__(self, type, type_cost, flavour, flavour_cost):
        self.obj_type = Type(type, type_cost)
        self.obj_flavour = Flavour(flavour, flavour_cost)

    def get_ice_cream_name(self):
        return self.obj_flavour.flavour + self.obj_type.type

    def get_ice_cream_cost(self):
        return self.obj_type.type_cost + self.obj_flavour.flavour_cost

def display_menu_card(ice_cream_obj):
    print('                      MENU CARD\n')
    for ice_cream in ice_cream_obj:
        print('       {} {} ice cream price is : {} rupees'.format(ice_cream.obj_flavour.flavour, ice_cream.obj_type.type, ice_cream.get_ice_cream_cost()))
    print('\n                       _ _ _ _ _ _')

def take_order(ice_cream_obj, topping_obj_list):
    try:
        ice_cream_flavour, ice_cream_type = input('\nWhich ice cream you want? (Eg.chocolate cup): ').lower().strip().split()
        quantity = int(input('How many {} {} ice cream you want? (Eg.2) : '.format(ice_cream_flavour, ice_cream_type)))
        for ice_cream in ice_cream_obj:
            if ice_cream_flavour == 'chocolate':
                if ice_cream.get_ice_cream_name() == ice_cream_flavour+ice_cream_type:
                    option = input('Do you want toppings? (yes-y,no-n) print y or n : ').lower().strip()
                    if option == 'y':
                        print('\nAvailable toppings are: ')
                        for item in topping_obj_list:
                            print('{} price is: {} rupees'.format(item.topping, item.topping_cost))
                        topping = input('\nwhich one do you want? (Eg.caramel) : ').lower().strip()
                        for item1 in topping_obj_list:
                            if topping == item1.topping:
                                return quantity,  ice_cream_flavour, ice_cream_type, topping
                        else:
                            return 'Wrong input'
                    else:
                        return quantity,  ice_cream_flavour, ice_cream_type
            elif (ice_cream.obj_flavour.flavour + ice_cream.obj_type.type) == (ice_cream_flavour + ice_cream_type):
                return quantity,  ice_cream_flavour, ice_cream_type
        else:
            return 'Wrong input'
    except Exception as e:
        print('\nError occurred, the exception was: ', e)
        return 'Error'

def billing(order, ice_cream_obj_list, topping_obj_list):
    for ice_cream in ice_cream_obj_list:
        if len(order) == 4:
            if ice_cream.get_ice_cream_name() == order[1] + order[2]:
                for item1 in topping_obj_list:
                    if item1.topping == order[3]:
                        return '\n{} {} {} ice cream with {} topping price is: {} rupees'.format(order[0], order[1], order[2], order[3], (ice_cream.get_ice_cream_cost() + item1.topping_cost) * order[0])
        elif ice_cream.get_ice_cream_name() == order[1] + order[2]:
            return '\n{} {} {} ice cream price is: {} rupees'.format(order[0], order[1], order[2], ice_cream.get_ice_cream_cost() * order[0])

ice_cream1 = IceCream('cup', 100, 'chocolate', 250)
ice_cream2 = IceCream('cup', 100, 'vanilla', 150)
ice_cream3 = IceCream('cup', 100, 'strawberry', 350)
ice_cream4 = IceCream('cone', 120, 'chocolate', 250)
ice_cream5 = IceCream('cone', 120, 'vanilla', 150)
ice_cream6 = IceCream('cone', 120, 'strawberry', 350)
ice_cream7 = IceCream('stick', 50, 'chocolate', 250)
ice_cream8 = IceCream('stick', 50, 'vanilla', 150)
ice_cream9 = IceCream('stick', 50, 'strawberry', 350)
ice_cream_obj_list = [ice_cream1, ice_cream2, ice_cream3, ice_cream4, ice_cream5, ice_cream6, ice_cream7, ice_cream8, ice_cream9]

topping1 = Topping('choco chips', 30)
topping2 = Topping('caramel', 50)
topping3 = Topping('nuts', 40)
topping_obj_list = [topping1, topping2, topping3]

display_menu_card(ice_cream_obj_list)
order = take_order(ice_cream_obj_list, topping_obj_list)
if order == 'Wrong input' or order == 'Error':
    print(order)
else:
    bill = billing(order, ice_cream_obj_list, topping_obj_list)
    print(bill)
