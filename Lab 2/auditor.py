inventory = 0

while True:
    stock_count = input("Enter stock quantity or quit to exit: ")
    if stock_count == "quit":
        break
    try:
        stock_count = int(stock_count)
        if stock_count >= 0:
            inventory += stock_count
            print(f"Added {stock_count} items to inventory. Total inventory: {inventory}")
        else:
            print("Please enter a positive integer!")
    except ValueError:
        print("Please enter an integer!")