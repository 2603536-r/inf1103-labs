from product import Product

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, size):
        super().__init__(product_id, name, price, stock)
        self.__size = size

    def get_size(self):
        return self.__size

    def display_information(self):
        return super().display_information()

    def get_fulfilment_info(self)->str:
        return "Delivered digitally"

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__size
        return data