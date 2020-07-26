import re
import datetime

class Driver:
    def __init__(self, name, age, driving_license_number, driving_license_validity_period):
        self.name = name
        self.age =age
        self.driving_license_number = driving_license_number
        self.driving_license_validity_period = driving_license_validity_period

    def check_driver_details(self):
        if self.__is_license_number_valid():
            if self.__is_license_date_valid():
                if self.__is_license_validity_period_active():
                    return True
                return '\nDriving license validity period expired.'
            return '\nInvalid format of license validity period.'
        return '\nInvalid license number.'

    def __is_license_date_valid(self):
        if re.search('[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}', self.driving_license_validity_period):
            return True
        return False

    def __is_license_validity_period_active(self):
        if str(datetime.date.today()) < self.driving_license_validity_period:
            return True
        return False

    def __is_license_number_valid(self):
        if re.search('[A-z]{2}[0-9]{13}', self.driving_license_number):
            return True
        return False

class Car:
    def __init__(self, car_category, car_number, colour, company, model):
        self.car_category = car_category
        self.car_number = car_number
        self.colour = colour
        self.company = company
        self.model = model

    def check_car_details(self):
        if self.car_category == 'micro' or self.car_category == 'xl':
            if self.__is_car_number_valid():
                return True
            return '\nInvalid car number.'
        return '\nInvalid car category.'

    def __is_car_number_valid(self):
        if re.search('^[A-Z]{2}\s[0-9]{2}\s[A-Z]{2}\s[0-9]{1,4}', self.car_number):
            return True
        return False

def driver_registration():
    driver_name = input('Enter the driver name (Eg.yogesh): ').title().strip()
    driver_age = int(input('Enter the driver age (Eg.21): ').strip())
    driver_license_no = input('Enter the driver license no (Eg. MH1420110062821): ').strip()
    driving_license_validity_period = input('Enter the driving license validity period (Eg: 2021-04-02)(year-month-date): ').strip()

    driver = Driver(driver_name, driver_age, driver_license_no, driving_license_validity_period)
    if driver.check_driver_details() == True:
        print('\nDriver details registered successfully.')
        return
    print(driver.check_driver_details(), '\nEnter the valid details again\n')
    driver_registration()

def car_registration():
    car_category = input('We have two category :[micro, xl]\nEnter the car category from the above list(Eg. micro) :').strip().lower()
    car_number = input('Enter the car number (Eg.TN 01 PA 4554) : ').strip()
    car_colour = input('Enter the car colour (Eg.White) : ').strip().title()
    car_company_name = input('Enter the car company name (Eg.Honda) : ').strip().title()
    car_model_name = input('Enter the model name (Eg.City) : ').strip().title()

    car = Car(car_category, car_number, car_colour, car_company_name, car_model_name)

    if car.check_car_details() == True:
        print('\nCar details registered successfully.')
        return
    print(car.check_car_details(), '\nEnter the valid car details\n')
    car_registration()

driver_registration()
car_registration()

