from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):

    BASE_SHIPPING_COST = 5.0
    COST_PER_KG = 2.0

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self)->float:
        return self.__weight

    def display_information(self):
        return super().display_information()

    def get_fulfilment_info(self)->str:
        return "Requires physical shipping"

    def calculate_shipping_cost(self) -> float:
        return self.BASE_SHIPPING_COST + self.COST_PER_KG * self.__weight

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data