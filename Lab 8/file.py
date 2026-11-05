import json

class File:
    def __init__(self, filename="inventory.json"):
        self.__filename = filename


    def load_inventory(self):
        try:
            with open(self.__filename, "r") as file:
                inventory = json.load(file)
                return inventory
        except FileNotFoundError:
            print("Inventory file does not exist")
            return []

    
    def save_inventory(self, inventory):
        inventory_data = self.load_inventory()
 
        for product in inventory.display_products():
            product_dict = product.to_dict()
 
            for existing_product in inventory_data:
                if existing_product["product_id"] == product.get_product_id():
                    existing_product.update(product_dict)
                    break
            else:
                inventory_data.append(product_dict)
 
        with open(self.__filename, "w") as file:
            json.dump(inventory_data, file, indent=4)
 
        print("Inventory saved successfully.")
