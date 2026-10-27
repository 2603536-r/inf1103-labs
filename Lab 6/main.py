from product import Product
from inventory import Inventory
from file import File

def main():
    exit_program = False
    file = File()
    inventory_data = file.load_inventory()
    inventory = Inventory()
    
    while not exit_program:
        print("\n===== Inventory Manager =====")
        print("1. Display inventory database")
        print("2. Search product")
        print("3. Add product")
        print("4. Update stock")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(inventory_data)

        elif choice == "2":
            prod_id = input("Please enter product id: (e.g. P001)")
            print(inventory.search_product(inventory_data, prod_id))

        elif choice == "3":
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))

            product = Product(product_id, name, price, stock)
            inventory.add_product(product)

        elif choice == "4":
           while True:
                prod_id = input("Please enter product id (e.g. P001): ")
                result = inventory.search_product(inventory_data, prod_id)
                
                if result is None:
                    print("Product not found")
                else:
                    quantity = int(input("Please enter the updated quantity: "))
                    
                    # Check if the found item came from the memory list (returns a tuple from display_information())
                    # or from inventory_data (returns a dictionary)
                    if isinstance(result, tuple):
                        # If it's a tuple, find the actual Product object in memory to update its stock
                        for p in inventory.display_products():
                            if p.get_product_id() == prod_id:
                                p.update_stock(quantity)
                                print("Stock updated successfully!")
                                break
                    elif isinstance(result, dict):
                        # If it's from inventory_data dictionary
                        result["stock"] = quantity
                        print("Stock updated in dictionary data successfully!")
                    break

        elif choice == "5":
            file.save_inventory(inventory)
            exit_program = True

        else:
            print("Please enter your choice (1-6)")

if __name__ == "__main__":
    main()