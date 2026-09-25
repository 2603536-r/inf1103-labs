# GLOBAL CONSTANTS
max_capacity = 500
tax_rate = 0.1
inventory_file = "inventory.txt"


def get_valid_input():
    """Get and validate product name and quantity."""
    product_name = input("Enter Product Name: ")
    user_input = input("Enter Quantity: ")

    if user_input == "quit":
        return "quit"

    try:
        quantity = int(user_input)

        if quantity > 0:
            return {
                "product_name": product_name,
                "quantity": quantity
            }
        else:
            print("Please enter a positive integer!")
            return None

    except ValueError:
        print("Please enter an integer!")
        return None


def process_delivery(current_value, new_value):
    """Calculate new inventory total."""
    current_value += new_value
    return current_value


def calculate_tax(amount):
    """Calculate tax."""
    amount *= tax_rate
    return amount


def generate_report(total_orders, failed_attempts):
    """Print summary."""
    print(
        f"Exiting..\n"
        f"Total Orders Processed: {total_orders}\n"
        f"Failed/Rejected Entries: {failed_attempts}"
    )


def load_inventory():
    """Load previous orders from inventory.txt."""
    try:
        with open(inventory_file, "r") as file:
            lines = file.readlines()

        orders = []

        for line in lines:
            line = line.strip()

            if not line:
                continue

            if line == "Current Orders:" or line == "New Orders:":
                continue

            parts = line.split(",")

            if len(parts) == 3:
                order_id = int(parts[0].strip())
                product_name = parts[1].strip()
                quantity = int(parts[2].strip())

                orders.append({
                    "order_id": order_id,
                    "product_name": product_name,
                    "quantity": quantity
                })

        return orders

    except FileNotFoundError:
        return []


def save_inventory(previous_orders, new_orders):
    """Save previous and new orders to inventory.txt."""
    with open(inventory_file, "w") as file:
        file.write("Current Orders:\n\n")

        for order in previous_orders:
            file.write(
                f"{order['order_id']}, "
                f"{order['product_name']}, "
                f"{order['quantity']}\n\n"
            )

        if new_orders:
            file.write("New Orders:\n\n")

            for order in new_orders:
                file.write(
                    f"{order['order_id']}, "
                    f"{order['product_name']}, "
                    f"{order['quantity']}\n\n"
                )


def main():
    # Load previous orders when program starts
    previous_orders = load_inventory()

    # New orders are kept separately during this program run
    new_orders = []

    # Calculate current inventory
    inventory = sum(
        order["quantity"] for order in previous_orders
    )

    failed_attempts = 0
    orders_processed = 0

    # Display previous orders
    print("Current Orders:\n")

    for order in previous_orders:
        print(
            f"{order['order_id']}, "
            f"{order['product_name']}, "
            f"{order['quantity']}\n"
        )

    while True:
        stock_count = get_valid_input()

        if stock_count == "quit":
            save_inventory(previous_orders, new_orders)
            print("\nOrder successfully saved to inventory.txt")
            break

        if stock_count is None:
            failed_attempts += 1
            continue

        product_name = stock_count["product_name"]
        quantity = stock_count["quantity"]

        # Check capacity
        new_inventory = process_delivery(inventory, quantity)

        if new_inventory > max_capacity:
            failed_attempts += 1
            print("Overstocked!!! Transaction rejected.\n")
            continue

        # Generate new order ID
        all_orders = previous_orders + new_orders

        if len(all_orders) == 0:
            order_id = 1001
        else:
            order_id = all_orders[-1]["order_id"] + 1

        # Create new order
        new_order = {
            "order_id": order_id,
            "product_name": product_name,
            "quantity": quantity
        }

        # Store new order in memory only
        new_orders.append(new_order)

        # Update inventory
        inventory = new_inventory

        orders_processed += 1

        print("\nNew Order Added:")
        print(f"{order_id}, {product_name}, {quantity}\n")


if __name__ == "__main__":
    main()