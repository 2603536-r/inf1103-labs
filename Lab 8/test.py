"""Lab 8 demo/tests. Run: python test_lab8.py"""
from Supplier import Supplier
from product import Product
from physical import PhysicalProduct
from digital import DigitalProduct
from inventory import Inventory
from Order import Order


def show_product_details(product: Product) -> None:
    name, price, stock = product.display_information()
    print(f"  {name} | ${price:.2f} | stock {stock}")
    print(f"  {product.get_fulfilment_info()}")


def test_association() -> None:
    print("\n== 2. Association: Supplier <-> Product ==")
    supplier = Supplier("S001", "TechSource", "sales@techsource.com")
    laptop = PhysicalProduct("P100", "Laptop", 1200.0, 5, 2.0, supplier)
    antivirus = DigitalProduct("P101", "Antivirus", 70.0, 200, 250.0, supplier)

    print(laptop.get_supplier().display_information())
    print(antivirus.get_supplier().display_information())
    print("Same supplier object:", laptop.get_supplier() is antivirus.get_supplier())

    del supplier   # PREDICT FIRST: what happens now?
    print("After del supplier:", laptop.get_supplier().display_information())


def test_aggregation() -> None:
    print("\n== 3. Aggregation: Inventory <> Product ==")
    s = Supplier("S002", "GadgetCo", "hi@gadgetco.com")
    mouse = PhysicalProduct("P200", "Mouse", 25.0, 40, 0.1, s)   # exists first

    inv_a, inv_b = Inventory(), Inventory()
    inv_a.add_product(mouse)
    print("In A:", inv_a.find_product("P200") is mouse)

    inv_a.remove_product("P200")     # PREDICT FIRST: does mouse still work?
    print("Removed from A; still works:", mouse.display_information())
    print("A find ->", inv_a.find_product("P200"))

    inv_b.add_product(mouse)
    print("Added to B (same object):", inv_b.find_product("P200") is mouse)


def test_composition() -> None:
    print("\n== 4. Composition: Order *-- OrderLine ==")
    s = Supplier("S003", "KeysRUs", "k@keys.com")
    keyboard = PhysicalProduct("P300", "Keyboard", 45.0, 20, 0.8, s)
    software = DigitalProduct("P301", "Editor", 70.0, 50, 120.0, s)

    order1, order2 = Order("O1"), Order("O2")
    order1.add_order_line(keyboard, 2)
    order1.add_order_line(software, 1)
    order2.add_order_line(keyboard, 3)    # PREDICT FIRST: how many lines / products?

    for line in order1.get_order_lines():
        print(" ", line.display_information())
    print("Order 1 total:", order1.calculate_total())
    print("Order 2 total:", order2.calculate_total())

    line1 = order1.get_order_lines()[0]
    line2 = order2.get_order_lines()[0]
    print("Same OrderLine object?  ", line1 is line2)
    print("Same Product object?    ", line1.get_product() is line2.get_product())

    order1.remove_order_line("P300")
    print("After removing line, order 1 total:", order1.calculate_total())
    print("Keyboard still exists:", keyboard.display_information())


def test_lsp_and_polymorphism() -> None:
    print("\n== 6/7. LSP + polymorphism ==")
    s = Supplier("S004", "MixedSupply", "m@mixed.com")
    inv = Inventory()
    inv.add_product(PhysicalProduct("P400", "Headphones", 30.0, 25, 0.3, s))
    inv.add_product(DigitalProduct("P401", "Antivirus", 70.0, 200, 250.0, s))

    for product in inv.display_products():     # one loop, no isinstance
        show_product_details(product)

    for product in inv.display_products():     # LSP: update_stock behaves the same
        product.update_stock(7)
        assert product.get_stock() == 7
    print("update_stock works identically on both subclasses")


if __name__ == "__main__":
    test_association()
    test_aggregation()
    test_composition()
    test_lsp_and_polymorphism()