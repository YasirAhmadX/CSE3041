n = int(input("Enter number of biscuits in shop: "))
inventory = dict()
for i in range(n):
    key = input("Enter name of biscuit: ")
    stock = int(input("Enter stock quantity: "))
    price = int(input("Enter price: "))

    inventory[key] = [stock,price]

n = int(input("Enter number of biscuits to buy: "))
bill = 0
for i in range(n):
    b = input("Enter biscuit name: ")
    qt = int(input("Enter quantity: "))
    if b in inventory.keys():
        if inventory[b][0] >= qt:
            inventory[b][0] -= qt
            bill = inventory[b][1]*qt
        else:
            print("Not enought stock.")
    else:
        print("Biscuit not in inventory.")

print("Total bill: ",bill)
