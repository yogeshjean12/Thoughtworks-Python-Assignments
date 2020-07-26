
class Range:
    def __init__(self, min_range, max_range):
        self.min_range = min_range
        self.max_range = max_range

class Vehicle:
    def __init__(self, vehicle_type, max_people_limit, min_range, max_range, select_ac, price_per_km):
        self.vehicle_type = vehicle_type
        self.max_people_limit = max_people_limit
        self.range = Range(min_range, max_range)
        self.ac = select_ac
        self.price_per_km = price_per_km

def display_category():
    print('We have different categories of vehicle:')
    vehicle_type_list = []
    for vehicle in vehicle_obj_list:
        if vehicle.vehicle_type not in vehicle_type_list:
            print('{} (Maximum upto {} people)'.format(vehicle.vehicle_type, vehicle.max_people_limit))
            vehicle_type_list.append(vehicle.vehicle_type)

def display_price_menu():

    if vehicle_select in auto1.vehicle_type:
        print('We have only Ac auto\'s')
        for vehicle in auto_obj_list:
            print('{} {} upto {}km price is : {} per km'.format('Ac', vehicle.vehicle_type, vehicle.range.max_range, vehicle.price_per_km))
        print('\nRide booked successfully')
    elif vehicle_select in micro1.vehicle_type:
        if ac_select == 'y':
            for vehicle in micro_obj_list:
                if vehicle.ac == 'yes':
                    print('{} {} upto {}km price is : {} per km'.format('Ac', vehicle.vehicle_type, vehicle.range.max_range, vehicle.price_per_km))
            print('\nRide booked successfully')
        elif ac_select == 'n':
            for vehicle in micro_obj_list:
                if vehicle.ac == 'no':
                    print('{} {} upto {}km price is : {} per km'.format('Non-Ac', vehicle.vehicle_type, vehicle.range.max_range, vehicle.price_per_km))
            print('\nRide booked successfully')
    elif vehicle_select in xl1.vehicle_type:
        if ac_select == 'y':
            for vehicle in xl_obj_list:
                if vehicle.ac == 'yes':
                    print('{} {} upto {}km price is : {} per km'.format('Ac', vehicle.vehicle_type, vehicle.range.max_range, vehicle.price_per_km))
            print('\nRide booked successfully')
        elif ac_select == 'n':
            for vehicle in xl_obj_list:
                if vehicle.ac == 'no':
                    print('{} {} upto {}km price is : {} per km'.format('Non-Ac', vehicle.vehicle_type, vehicle.range.max_range, vehicle.price_per_km))
            print('\nRide booked successfully')
    else:
        print('Invalid input')

auto1 = Vehicle('auto', 3, 0, 15, 'yes', 10)
auto2 = Vehicle('auto', 3, 15, 30, 'yes', 8)
auto3 = Vehicle('auto', 3, 30, 1500, 'yes', 15)
auto_obj_list = [auto1, auto2, auto3]
micro1 = Vehicle('micro', 4, 0, 15, 'yes', 12)
micro2 = Vehicle('micro', 4, 15, 1500, 'yes', 10)
micro3 = Vehicle('micro', 4, 0, 15, 'no', 14)
micro4 = Vehicle('micro', 4, 15, 1500, 'no', 12)
micro_obj_list = [micro1, micro2, micro3, micro4]
xl1 = Vehicle('xl', 10, 0, 15, 'yes', 14)
xl2 = Vehicle('xl', 10, 15, 1500, 'yes', 14)
xl3 = Vehicle('xl', 10, 0, 15, 'no', 15)
xl4 = Vehicle('xl', 10, 15, 1500, 'no', 15)
xl_obj_list = [xl1, xl2, xl3, xl4]

vehicle_obj_list = [auto1, auto2, auto3, micro1, micro2, micro3, micro4, xl1, xl2, xl3, xl4]

display_category()
vehicle_select = input('\nSelect the category (Eg.micro) : ').lower().strip()
ac_select = input('Do you want Ac? (yes-y/no-n): ').strip().lower()
display_price_menu()
