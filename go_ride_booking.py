from abc import ABC, abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def get_range(self):
        pass
    @abstractmethod
    def get_select_ac(self):
        pass
    @abstractmethod
    def get_price_per_km(self):
        pass
    @abstractmethod
    def get_max_people_limit(self):
        pass

class Micro(Vehicle):
    def __init__(self, vehicle_type, max_people_limit, min_range, max_range, select_ac, price_per_km):
         self.vehicle_type = vehicle_type
         self.__max_people_limit = max_people_limit
         self.__select_ac = select_ac
         self.__price_per_km = price_per_km
         self.__min_range = min_range
         self.__max_range = max_range

    def get_range(self):
        return '{}-{} km'.format(self.__min_range, self.__max_range)

    def get_select_ac(self):
        return self.__select_ac

    def get_price_per_km(self):
        return self.__price_per_km

    def get_max_people_limit(self):
        return self.__max_people_limit

class Auto(Vehicle):
    def __init__(self, vehicle_type, max_people_limit, min_range, max_range, select_ac, price_per_km):
        self.vehicle_type = vehicle_type
        self.__max_people_limit = max_people_limit
        self.__select_ac = select_ac
        self.__price_per_km = price_per_km
        self.__min_range = min_range
        self.__max_range = max_range

    def get_range(self):
        return '{}-{} km'.format(self.__min_range, self.__max_range)

    def get_select_ac(self):
        return self.__select_ac

    def get_price_per_km(self):
        return self.__price_per_km

    def get_max_people_limit(self):
        return self.__max_people_limit

class Xl(Vehicle):
    def __init__(self, vehicle_type, max_people_limit, min_range, max_range, select_ac, price_per_km):
        self.vehicle_type = vehicle_type
        self.__max_people_limit = max_people_limit
        self.__select_ac = select_ac
        self.__price_per_km = price_per_km
        self.__min_range = min_range
        self.__max_range = max_range

    def get_range(self):
        return '{}-{} km'.format(self.__min_range, self.__max_range)

    def get_select_ac(self):
        return self.__select_ac

    def get_price_per_km(self):
        return self.__price_per_km

    def get_max_people_limit(self):
        return self.__max_people_limit

def display_category():
    print('We have different categories of vehicle:')
    vehicle_type_list = []
    for vehicle in vehicle_obj_list:
        if vehicle.vehicle_type not in vehicle_type_list:
            print('{} (Maximum upto {} people)'.format(vehicle.vehicle_type, vehicle.get_max_people_limit()))
            vehicle_type_list.append(vehicle.vehicle_type)

def customer_selection():
    vehicle_select = input('\nSelect the category from the above list(Eg.micro) : ').lower().strip()
    for vehicle in vehicle_obj_list:
        if vehicle_select == vehicle.vehicle_type:
                if vehicle_select == 'auto':
                    print('We have only Ac Auto\'s, suggest you to go with Ac auto\n')
                    ac_select = 'yes'
                    price_menu(vehicle_select, ac_select)
                    break
                else:
                    ac_select = input('Do you want Ac vehicle? (yes/no): ').strip().lower()
                price_menu(vehicle_select, ac_select)
                break
    else:
        print('Wrong input, try again')

def price_menu(vehicle_select, ac_select):
    for vehicle in vehicle_obj_list:
        if vehicle_select == vehicle.vehicle_type:
            if vehicle.get_select_ac() == 'yes':
                if ac_select == 'yes':
                    print('Ac {} vehicle range: {} price is : {}rupees/km'.format(vehicle.vehicle_type, vehicle.get_range(), vehicle.get_price_per_km()))
            elif vehicle.get_select_ac() == 'no':
                if ac_select == 'no':
                    print('Non-Ac {} vehicle range: {} price is : {}rupees/km'.format(vehicle.vehicle_type, vehicle.get_range(), vehicle.get_price_per_km()))
    print('\nYour ride is booked successfully')

auto1 = Auto('auto', 3, 0, 15, 'yes', 10)
auto2 = Auto('auto', 3, 15, 30, 'yes', 8)
auto3 = Auto('auto', 3, 30, 1500, 'yes', 15)
micro1 = Micro('micro', 4, 0, 15, 'yes', 12)
micro2 = Micro('micro', 4, 15, 1500, 'yes', 10)
micro3 = Micro('micro', 4, 0, 15, 'no', 14)
micro4 = Micro('micro', 4, 15, 1500, 'no', 12)
xl1 = Xl('xl', 10, 0, 15, 'yes', 14)
xl2 = Xl('xl', 10, 15, 1500, 'yes', 14)
xl3 = Xl('xl', 10, 0, 15, 'no', 15)
xl4 = Xl('xl', 10, 15, 1500, 'no', 15)
vehicle_obj_list = [auto1, auto2, auto3, micro1, micro2, micro3, micro4, xl1, xl2, xl3, xl4]

display_category()
customer_selection()