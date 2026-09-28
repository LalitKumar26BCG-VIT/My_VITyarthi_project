Contents = {}


def get_int(prompt, min_value=None, max_value=None):
    """Safely read an integer, re-prompting on bad input instead of crashing."""
    while True:
        raw = input(prompt).strip()
        if not raw.lstrip("-").isdigit():
            print("PLEASE ENTER A VALID NUMBER.")
            continue
        value = int(raw)
        if min_value is not None and value < min_value:
            print(f"PLEASE ENTER A NUMBER >= {min_value}.")
            continue
        if max_value is not None and value > max_value:
            print(f"PLEASE ENTER A NUMBER <= {max_value}.")
            continue
        return value


def loading_menu():
    try:
        with open("menu.txt", "r") as file:
            for line in file:
                item, price = line.strip().split("|")
                Contents[item] = int(price)
    except FileNotFoundError:
        with open("menu.txt", "w") as file:
            file.write("DOSA|200\n")
            file.write("PAV BHAAJI|200\n")
            file.write("VADA PAV|100\n")
            file.write("NOODELS|70\n")
            file.write("PIZZA|300\n")
            file.write("BURGER|150\n")
            file.write("MOMOS|100\n")
            file.write("SANDWICH|90\n")
            file.write("BREAD PAKODA|50\n")
            file.write("SAMOSA|40\n")
            file.write("KATCHORI|40\n")
            file.write("PASTERY|70\n")
            file.write("GULABJAMUN|40\n")

        with open("menu.txt", "r") as file:
            for line in file:
                item, price = line.strip().split("|")
                Contents[item] = int(price)


def saving_menu():
    with open("menu.txt", "w") as file:
        for item in Contents:
            file.write(f"{item}|{Contents[item]}\n")


def checking_identity():
    ask = input("ARE YOU OUR EMPLOYEE? [Y/N]: ").strip().upper()

    if ask.startswith("Y"):
        menu_edit()

    display(Contents)
    return 1


def display(Items_and_their_prices: dict):
    count = 1
    print("\n------------ FOOD SPACE'S TODAY'S MENU ------------")
    print(f"{'S.NO':<8} | {'ITEM':^20} | {'PRICE':>10}")
    print("-" * 45)

    for key in Items_and_their_prices:
        print(f"{count:<8} | {key:^20} | {Items_and_their_prices[key]:>10} INR")
        count += 1


Orders_placed = []


def recieving_order():
    num_of_items = get_int("NUMBER OF ITEMS YOU WANT TO ORDER: ", min_value=1)
    Contents1 = list(Contents)
    iterator = 0

    print("\nENTER ITEM NUMBER OR ITEM NAME:")

    while iterator < num_of_items:
        Order_placed = input(f"ITEM {iterator + 1}: ").strip().upper()

        if Order_placed.isdigit():
            item_number = int(Order_placed)

            if 1 <= item_number <= len(Contents1):
                Orders_placed.append(Contents1[item_number - 1])
                iterator += 1
            else:
                print("INVALID ITEM NUMBER.")

        elif Order_placed in Contents:
            Orders_placed.append(Order_placed)
            iterator += 1

        else:
            print("ITEM NOT AVAILABLE IN MENU.")

    print("ORDER RECEIVED.")
    conforming_order(Orders_placed)


def toremove():
    if not Orders_placed:
        print("YOUR ORDER IS EMPTY.")
        return

    print("\nYOUR CURRENT ORDER:")
    for i in range(len(Orders_placed)):
        print(f"{i + 1}. {Orders_placed[i]}")

    rem_count = get_int(
        "NUMBER OF ITEMS TO REMOVE: ", min_value=1, max_value=len(Orders_placed)
    )
    b = 0

    while b < rem_count:
        if not Orders_placed:
            print("ORDER IS NOW EMPTY.")
            break

        item_number = get_int(
            "ENTER ITEM NUMBER TO REMOVE: ", min_value=1, max_value=len(Orders_placed)
        )
        todel = Orders_placed[item_number - 1]
        Orders_placed.remove(todel)
        print(f"{todel} REMOVED.")
        b += 1

    conforming_order(Orders_placed)


def modifying_order():
    print("1. ADD ITEM")
    print("2. REMOVE ITEM")

    act = get_int("WHAT DO YOU WANT TO DO? ", min_value=1, max_value=2)

    if act == 1:
        recieving_order()
    elif act == 2:
        toremove()


def saving_order_history(Orders):
    Total_price = 0

    with open("order_history.txt", "a") as file:
        file.write("\n" + "=" * 45 + "\n")
        file.write("FOOD SPACE ORDER\n")
        file.write("=" * 45 + "\n")

        for order in Orders:
            file.write(f"{order} - {Contents[order]} INR\n")
            Total_price += Contents[order]

        file.write(f"TOTAL PRICE: {Total_price} INR\n")
        file.write("=" * 45 + "\n")


def conforming_order(Orders):
    iterator = 1
    Total_price = 0

    print("\n------------------- YOUR ORDER -------------------")
    print(f"{'S.NO':>8} | {'ITEM':^20} | {'PRICE'}")
    print("-" * 45)

    for order in Orders:
        print(f"{iterator:>8} | {order:^20} | {Contents[order]} INR")
        Total_price += Contents[order]
        iterator += 1

    print("-" * 45)
    print(f"TOTAL PRICE: {Total_price} INR")

    y = input("DO YOU WANT TO ORDER SOMETHING ELSE? [Y/N]: ")

    if y.strip().upper().startswith("Y"):
        modifying_order()
    else:
        saving_order_history(Orders)
        print("THANK YOU FOR PLACING YOUR ORDER.")
        print("YOUR ORDER HAS BEEN SAVED.")


def menu_edit():
    emp_id = input("ENTER YOUR EMPLOYEE ID: ").strip().upper()

    if not emp_id.startswith("FOOD_SPACE@"):
        print("INVALID EMPLOYEE ID.")
        return

    print("\n1. ADD A NEW ITEM")
    print("2. REMOVE AN ITEM")
    print("3. EDIT PRICE")

    change = get_int("ENTER YOUR ANSWER: ", min_value=1, max_value=3)

    if change == 1:
        numofitemstobeadded = get_int("HOW MANY ITEMS DO YOU WANT TO ADD? ", min_value=1)

        for i in range(numofitemstobeadded):
            nameofitem = input("NAME OF ITEM: ").strip().upper()
            priceofitem = get_int("PRICE OF ITEM: ", min_value=0)
            Contents[nameofitem] = priceofitem

        saving_menu()
        print("MENU UPDATED.")

    elif change == 2:
        if not Contents:
            print("MENU IS ALREADY EMPTY.")
            return

        numofitemstoberemoved = get_int(
            "HOW MANY ITEMS DO YOU WANT TO REMOVE? ", min_value=1, max_value=len(Contents)
        )

        for i in range(numofitemstoberemoved):
            if not Contents:
                print("MENU IS NOW EMPTY.")
                break
            display(Contents)
            Contents1 = list(Contents)
            item_number = get_int(
                "ENTER ITEM NUMBER TO REMOVE: ", min_value=1, max_value=len(Contents1)
            )
            itemtoberemoved = Contents1[item_number - 1]
            Contents.pop(itemtoberemoved)
            print(f"{itemtoberemoved} REMOVED.")

        saving_menu()
        print("MENU UPDATED.")

    elif change == 3:
        if not Contents:
            print("MENU IS EMPTY.")
            return

        numofitemstoedited = get_int(
            "NUMBER OF ITEMS WHOSE PRICE YOU WANT TO CHANGE: ",
            min_value=1,
            max_value=len(Contents),
        )

        for i in range(numofitemstoedited):
            display(Contents)
            Contents1 = list(Contents)
            item_number = get_int(
                "ENTER ITEM NUMBER: ", min_value=1, max_value=len(Contents1)
            )
            itemtoedit = Contents1[item_number - 1]
            newprice = get_int(f"NEW PRICE FOR {itemtoedit}: ", min_value=0)
            Contents[itemtoedit] = newprice

        saving_menu()
        print("PRICES UPDATED.")


def ordering_system():
    checking_identity()
    recieving_order()


loading_menu()
ordering_system()