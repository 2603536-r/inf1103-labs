from product import Product
from Supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 size: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__size: float = size

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