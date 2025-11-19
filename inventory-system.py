inventory = {
    "Apples": {"price": 0.5, "stock": 50},
    "Bananas": {"price": 0.3, "stock": 100},
    "Cherries": {"price": 1.5, "stock": 20}
}

print("\nINVENTORY: 50 Apples (50p), 100 Bananas (30p), 20 Cherries (£1.50)")
basket = 0

while True:
    item = input("\nWhat item would you like to buy?\n -> ").capitalize()
    quantity = int(input("\nHow many?\n -> "))

    if item in inventory:
        if quantity <= inventory[item]["stock"]:
            cost = inventory[item]["price"] * quantity
            inventory[item]["stock"] -= quantity
            print(f"\nTotal cost: ${cost:.2f}")
            basket += cost
            print(f"\nRemaining {item}: {inventory[item]['stock']}")
            print(f"\nBASKET: ${basket:.2f}")
        else:
            print("\nNot enough stock.")
    else:
        print("\nItem not found.")

    if inventory["Apples"]["stock"] == 0 and inventory["Bananas"]["stock"] == 0 and inventory["Cherries"]["stock"] == 0:
        print("\n We're all out of stock!")
        break
    