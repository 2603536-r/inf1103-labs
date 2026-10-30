from physical import PhysicalProduct
from digital import DigitalProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory
from file import File


class InventoryApp:
    """Console UI. Delegates storage to Inventory and saving/loading to File."""

    def __init__(self):
        self.__file = File()
        self.__inventory_data = self.__file.load_inventory()  # dicts from the JSON file
        self.__inventory = Inventory()                        # Product objects added this session
        self.__running = False
        self.__actions = {
            "1": self.__display_inventory,
            "2": self.__search_product,
            "3": self.__add_product,
            "4": self.__update_stock,
            "5": self.__exit,
        }

    def run(self):
        self.__running = True
        while self.__running:
            self.__show_menu()
            action = self.__actions.get(input("Enter your choice: "))
            if action is None:
                print("Please enter a choice between 1 and 5.")
            else:
                action()

    # ---------- helpers ----------
    def __show_menu(self):
        print("\n===== Inventory Manager =====")
        print("1. Display inventory database")
        print("2. Search product")
        print("3. Add product")
        print("4. Update stock")
        print("5. Exit")

    def __read_number(self, prompt, number_type):
        while True:
            try:
                value = number_type(input(prompt))
                if value < 0:
                    print("Value cannot be negative.")
                    continue
                return value
            except ValueError:
                print("Invalid number, try again.")

    def __find_object(self, product_id):
        for product in self.__inventory.display_products():
            if product.get_product_id() == product_id:
                return product
        return None

    def __show_product(self, product):
        name, price, stock = product.display_information()
        line = f"ID: {product.get_product_id()} | Name: {name} | Price: ${price:.2f} | Stock: {stock}"
        if isinstance(product, PhysicalProduct):
            line += f" | Weight: {product.get_weight()} kg"
        elif isinstance(product, DigitalProduct):
            line += f" | Download size: {product.get_size()} MB"
        print(line)
        print(product.get_fulfilment_info())
        if isinstance(product, CanBeShipped):
            print(f"Shipping cost: ${product.calculate_shipping_cost():.2f}")

    # ---------- menu actions ----------
    def __display_inventory(self):
        print("--- Saved inventory (JSON file) ---")
        for item in self.__inventory_data:
            print(item)
        print("--- Added this session ---")
        products = self.__inventory.display_products()
        if not products:
            print("(none)")
        for product in products:
            self.__show_product(product)

    def __search_product(self):
        prod_id = input("Please enter product id (e.g. P001): ")
        result = self.__inventory.search_product(self.__inventory_data, prod_id)
        if result is None:
            print("Product not found")
        elif isinstance(result, dict):
            print(result)
        else:  # tuple -> the product lives in memory; show the full object
            self.__show_product(self.__find_object(prod_id))

    def __add_product(self):
        print("Product type: 1. Physical  2. Digital")
        kind = input("Enter type: ")
        if kind not in ("1", "2"):
            print("Invalid product type.")
            return
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = self.__read_number("Enter product price: ", float)
        stock = self.__read_number("Enter product stock: ", int)
        if kind == "1":
            weight = self.__read_number("Enter weight (kg): ", float)
            product = PhysicalProduct(product_id, name, price, stock, weight)
        else:
            size = self.__read_number("Enter download size (MB): ", float)
            product = DigitalProduct(product_id, name, price, stock, size)
        self.__inventory.add_product(product)
        print("Product added.")

    def __update_stock(self):
        prod_id = input("Please enter product id (e.g. P001): ")
        result = self.__inventory.search_product(self.__inventory_data, prod_id)
        if result is None:
            print("Product not found")
            return
        quantity = self.__read_number("Please enter the updated quantity: ", int)
        if isinstance(result, dict):
            result["stock"] = quantity
            print("Stock updated in dictionary data successfully!")
        else:
            self.__find_object(prod_id).update_stock(quantity)
            print("Stock updated successfully!")

    def __exit(self):
        self.__file.save_inventory(self.__inventory)
        self.__running = False


def main():
    InventoryApp().run()


if __name__ == "__main__":
    main()