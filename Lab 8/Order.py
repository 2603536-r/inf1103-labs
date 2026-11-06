from OrderLine import OrderLine
from product import Product


class Order:
    """Whole in a composition: creates, manages and owns its OrderLines."""

    def __init__(self, order_id: str) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    def get_order_id(self) -> str:
        return self.__order_id

    def add_order_line(self, product: Product, quantity: int) -> None:
        # The Order creates the line itself - never passed in from outside.
        self.__order_lines.append(OrderLine(product, quantity))

    def remove_order_line(self, product_id: str) -> bool:
        """Removing a line destroys it with the order's record; it isn't reused."""
        for line in self.__order_lines:
            if line.get_product().get_product_id() == product_id:
                self.__order_lines.remove(line)
                return True
        return False

    def get_order_lines(self) -> list[OrderLine]:
        return list(self.__order_lines)

    def calculate_total(self) -> float:
        return sum(line.calculate_subtotal() for line in self.__order_lines)