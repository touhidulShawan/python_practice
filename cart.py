cart_item = []  # Global variable

# add item


def add_item():
    while True:
        choosen_item = input("Add product to your cart (Press q to quit) -> ")
        if choosen_item == "q":
            break
        else:
            cart_item.append(choosen_item)
            print("Item added to cart successfully\n")
# remove item


def delete_item():
    item_to_be_delete = input(
        "Which item do you want to delete (type (all) to remove all ) --> ")

    if item_to_be_delete == "all":
        cart_item.clear()
        print("All items are removed")
    else:
        try:
            cart_item.remove(item_to_be_delete)
            print(f"{item_to_be_delete} removed successfully")
        except:
            print(f"{item_to_be_delete} is not available in your cart.")


# check item


def check_item():
    print("**** Items in your Cart ****")
    print(f"Total item in your cart {len(cart_item)}")
    for item in cart_item:
        print(f"--- {item}")
    if len(cart_item) == 0:
        print("\nPlease add item your cart.")

# Option


def shopping_option():
    print("""
    -----------------------------
    1. Add Item to your cart
    2. Delete item from your cart
    3. Check item on your cart
    0. Quit.
    -----------------------------
    """)


try:
    while True:
        shopping_option()
        user_choice = int(input("Choose your option --> "))
        print("\n")
        if user_choice == 1:
            add_item()
        elif user_choice == 2:
            delete_item()
        elif user_choice == 3:
            check_item()
        elif user_choice == 0:
            break
        else:
            print("Please choose option correctly!!")

except:
    print("Something wrong!! try agian later.")
