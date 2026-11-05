from product import Product


class Inventory:
    """Aggregation: holds references to Products it does not create or own."""

    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def remove_product(self, product_id: str) -> bool:
        """Drop the reference only; the Product object itself is untouched."""
        product = self.find_product(product_id)
        if product is None:
            return False
        self.__products.remove(product)
        return True

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def search_product(self, inventory_data: list[dict], product_id: str):
        """Lab 7 search: in-memory Products first, then the JSON dicts."""
        product = self.find_product(product_id)
        if product is not None:
            return product.display_information()

        for item in inventory_data:
            if item["product_id"] == product_id:
                return item
        return None

    def display_products(self) -> list[Product]:
        return self.__products