class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, inventory_data, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product.display_information()

        for product in inventory_data:
            if product["product_id"] == product_id:
                return product
        return None

    def display_products(self):
       return self.__products