from product import Product


class OrderLine:
    """Part of an Order (composition). Only Order should create these."""

    def __init__(self, product: Product, quantity: int) -> None:
        self.__product: Product = product      # association: OrderLine -> Product
        self.__quantity: int = quantity

    def get_product(self) -> Product:
        return self.__product

    def get_quantity(self) -> int:
        return self.__quantity

    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity

    def display_information(self) -> str:
        name = self.__product.get_name()
        price = self.__product.get_price()
        return (f"{name} x{self.__quantity} @ ${price:.2f} "
                f"= ${self.calculate_subtotal():.2f}")