
class Product:

    ''' Product details '''

    def __init__(self, id_no, name, price, category, tax):
        self.id_no = id_no
        self.name = name
        self.price = price
        self.category = category
        self.tax = tax

class Tax:

    ''' Product tax report '''

    def __init__(self, id_no, name, price, category):
        self.id_no = id_no
        self.name = name
        self.price = price
        self.category = category


    def basic_tax(self):
        if self.category == 'dairy' and self.price > 1000:
            self.tax = self.price * 0.03
        elif self.category == 'dairy' and self.price < 1000:
            self.tax = 0
        elif self.price > 500:
            self.tax = self.price * 0.05
        elif self.price < 500:
            self.tax = self.price * 0.02
        else:
            self.tax = 0

        return self.tax

    def extra_tax(self):
        return self.price * 0.01

    def grand_tax(self):
        if self.category == 'textile':
            self.total_tax = Tax.basic_tax(self) + Tax.extra_tax(self)
        else:
            self.total_tax = Tax.basic_tax(self)

        return self.total_tax


def product_details():
    dairy = {'butter': 1200, 'cheese': 750,'milk': 750,'ice cream': 2500}
    textile = {'t-shirt': 450,'shirt': 900,'pant': 2000,'saree': 1200}
    produce = {'potatoes': 100, 'tomatoes': 300,'carrots': 600,'cucumbers':250}
    home_needs = {'towel': 600,'chair': 1500,'blanket': 1000,'air conditioner': 40000}
    categories = [dairy, textile, produce, home_needs]
    list_of_products = []
    product_with_id = {}

    def all_tax():
        print('Printing all items tax amount...')
        id_no = 1
        for category in categories:
            for item in category:
                product_with_id.update({item: id_no})
                id_no += 1
                list_of_products.append(item)
                get_tax_amount(item)

    def get_tax_amount(item):
        if item in dairy:
            product = Tax(product_with_id[item], item, dairy[item], 'dairy')
        elif item in textile:
            product = Tax(product_with_id[item], item, textile[item], 'textile')
        elif item in produce:
            product = Tax(product_with_id[item], item, produce[item], 'produce')
        elif item in home_needs:
            product = Tax(product_with_id[item], item, home_needs[item], 'home needs')
        else:
            print('sry, product not available')
            return

        print('Id no:{}.{} tax amount is {} rupees '.format(product_with_id[item], item, product.grand_tax()) )

    all_tax()

    user_input1 = input('\nDo you want to know any specific product tax? (y-yes,n-no) type - y/n: ')
    if user_input1 == 'y':
        user_input2 = input('Do you want me to display the available items? (y-yes,n-no) type - y/n: ')
        if user_input2 == 'y':
            print(list_of_products)
            name = input('Enter the name of the product: ')
            get_tax_amount(name)
            print('Thank you')
        else:
            name = input('Enter the name of the product: ')
            get_tax_amount(name)
            print('Thank you')
    else:
        print('Thank you')

product_details()