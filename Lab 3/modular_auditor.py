# GLOBAL CONSTANT
max_capacity = 500
tax_rate = 0.1

def get_valid_input():
    """Function to get and validate input"""
    user_input = input("Enter stock quantity or quit to exit: ")
    if user_input == "quit":
        return "quit"
    # check if user input is integer or string
    try:
        user_input = int(user_input) 
        # check positive integer
        if user_input >= 0:
            return user_input
        else:
            # if not positive, is negative
            print("Please enter a positive integer!")
            return None
    # if user input not integer, then ask user to enter integer
    except ValueError:
        print("Please enter an integer!")
        return None

def process_delivery(current_value, new_value):
    """Function to calculate delivery value"""
    current_value += new_value
    return current_value

def calculate_tax(amount):
    """Function to calculate tax"""
    amount *= tax_rate
    return amount

def generate_report(total_units,failed_attempts):
    """Function to print summary"""
    print(f"Exiting..\nTotal Deliveries Processed: {total_units}\nFailed/Rejected Entries: {failed_attempts}")

def main():
    # initialize constants
    inventory = 0
    tax = 0
    deliveries_processed = 0
    failed_attempts = 0

    while True:
        stock_count = get_valid_input()

        if stock_count == "quit":
            generate_report(deliveries_processed, failed_attempts)
            print(f"Total inventories entered: {inventory}\nTotal tax: {tax}")
            break

        if stock_count is None:
            failed_attempts += 1
            continue

        inventory = process_delivery(inventory, stock_count)

        # ensure that stock count is within capacity
        if inventory > max_capacity:
            failed_attempts += 1
            print("Overstocked!!! Exiting..")
            generate_report(deliveries_processed, failed_attempts)
            print(f"Total inventories entered: {inventory}\nTotal tax: {tax}")
            break

        # if doesnt break, stock count is within capacity, means delivery is successfully, increment
        deliveries_processed += 1
        tax = calculate_tax(inventory)
        print(f"Total Inventory: {inventory}")

if __name__ == "__main__":
    main()