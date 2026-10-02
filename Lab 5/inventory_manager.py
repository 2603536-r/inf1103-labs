import json

INVENTORY_FILE = "inventory.json"


def load_inventory():
    inventory = []

    try:
        with open(INVENTORY_FILE, "r") as file:
            inventory = json.load(file)
    except FileNotFoundError:
        print("Inventory file does not exist")

    return inventory


def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file, indent=4)


def search_product(inventory, product_id):
    for product in inventory:
        if product_id == product["id"]:
            return product

    return None


def add_product(inventory, product_id, name, price, stock):
    for product in inventory:
        if product_id == product["id"] or name == product["name"]:
            return False

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    inventory.append(product)
    save_inventory(inventory)

    return True


def update_stock(inventory, product_id, new_stock):
    product = search_product(inventory, product_id)

    if product is None:
        return False

    product["stock"] = new_stock
    save_inventory(inventory)

    return True


# Part of UI
def display_all(inventory):
    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    print("\n--- Inventory ---")

    for product in inventory:
        print(f"ID: {product['id']}")
        print(f"Name: {product['name']}")
        print(f"Price: ${product['price']:.2f}")
        print(f"Stock: {product['stock']}")
        print("-----------------")


# Manage UI Menu
def main():
    """
    Main function to run inventory manager.
    """

    inventory = load_inventory()
    exit_program = False

    while not exit_program:
        print("\n===== Inventory Manager =====")
        print("1. Display all products")
        print("2. Search product")
        print("3. Add product")
        print("4. Update stock")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_all(inventory)

        elif choice == "2":
            product_id = input("Enter product ID: ")

            product = search_product(inventory, product_id)

            if product is None:
                print("Product not found.")
            else:
                print("\nProduct found:")
                print(f"ID: {product['id']}")
                print(f"Name: {product['name']}")
                print(f"Price: ${product['price']:.2f}")
                print(f"Stock: {product['stock']}")

        elif choice == "3":
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))

            if add_product(inventory, product_id, name, price, stock):
                print("Product added successfully.")
            else:
                print("Product ID or name already exists.")

        elif choice == "4":
            product_id = input("Enter product ID: ")
            new_stock = int(input("Enter new stock: "))

            if update_stock(inventory, product_id, new_stock):
                print("Stock updated successfully.")
            else:
                print("Product not found.")

        elif choice == "5":
            exit_program = True
            print("Goodbye!")

        else:
            print("Invalid choice. Please try again.")


# __name__ (Program Entry Point)
if __name__ == "__main__":
    main()