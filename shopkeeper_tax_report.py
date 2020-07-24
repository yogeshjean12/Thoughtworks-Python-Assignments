
class Tax:
    '''Tax details'''
    normal_price_limit = 500
    dairy_price_limit = 1000
    tax = 0
    high_tax = 0.05
    normal_tax = 0.02
    dairy_tax = 0.03
    extra_tax = 0.01
    def __init__(self, id_no, name, price, category):
        self.id_no = id_no
        self.name = name
        self.price = price
        self.category = category

    def __basic_tax(self):
        if self.category == 'dairy' and self.price > self.dairy_price_limit:
            self.tax = self.price * self.dairy_tax
        elif self.category == 'dairy' and self.price < self.dairy_price_limit:
            self.tax = self.tax
        elif self.price > self.normal_price_limit:
            self.tax = self.price * self.high_tax
        elif self.price < self.normal_price_limit:
            self.tax = self.price * self.normal_tax
        else:
            return self.tax
        return self.tax

    def __extra_tax(self):
        return self.price * self.extra_tax

    def grand_tax(self):
        if self.category == 'textile':
            self.total_tax = Tax.__basic_tax(self) + Tax.__extra_tax(self)
        else:
            self.total_tax = Tax.__basic_tax(self)
        return self.total_tax

class Product:
    '''Product details'''
    def __init__(self, id_no, name, price, category):
        self.id_no = id_no
        self.name = name
        self.price = price
        self.category = category
        self.obj_tax = Tax(id_no, name, price, category)

def get_all_tax_amount(product_obj_list):
    for product in product_obj_list:
        print('product {} has tax amount of: {} rupees'.format(product.name, product.obj_tax.grand_tax()))

product1 = Product(1, 'butter', 1200, 'dairy')
product2 = Product(2, 'cheese', 750, 'dairy')
product3 = Product(3, 'shirt', 900, 'textile')
product4 = Product(4, 'saree', 2000, 'textile')
product5 = Product(5, 'potatoes', 100, 'produce')
product6 = Product(6, 'tomatoes', 300, 'produce')
product7 = Product(7, 'towel', 600, 'home_needs')
product8 = Product(8, 'chair', 1500, 'home_needs')
product_obj_list = [product1, product2, product3, product4, product5, product6, product7, product8]

get_all_tax_amount(product_obj_list)