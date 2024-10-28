class Product:
    def __init__(self, name):
        self.name = name

class Shop:
    def __init__(self, buyer):
        self.buyer = buyer
        self.products = []
    
    def add_product(self, product_name):
        product = Product(product_name)
        self.products.append(product)
    
    def buy_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product) 
                return f'Congratulations {self.buyer}! You have successfully bought {product_name}.'
        return f'Sorry, {product_name} is not available.'


shop = Shop('aala')
shop.add_product('calculator')
shop.add_product('keyboard')
shop.add_product('mouse')
shop.add_product('pen')
shop.add_product('monitor')

print(shop.buy_product('pen'))         
print(shop.buy_product('laptop'))      
