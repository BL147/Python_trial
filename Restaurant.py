# Restaurants billing and all

name = input("Enter your name:")

print("Welcoem what would yout like to eat Mr/Mrs" + name)

menu_order = input("pizza\nburger\nmendu vada\nWhat would you like (type the same as what it is written)")

menu = ["Pizza", "Burger", "Mendu vada"]

if menu_order == "pizza":
    print("Here is your" + menu[0])
elif menu_order == "burger":
    print("Here is your" + menu[1])
elif menu_order == "mendu vada":
    print("Here is your" + menu[2])
else:
    print("wrong spelling pls try again")
