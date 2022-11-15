import file_handlers as fh
import extra_functions as x
import order_functions as of
import csv


def incorrect_input():
    print("Incorrect input")
    main_menu()


def main_menu():
    cmd = input(
        f"""Main Menu:
0 to save and exit
1 for product menu options
2 for courier menu options
3 for order menu options
>>> """
    )
    if cmd == "0":
        with open("products.csv", "w") as products:
            writer = csv.writer(products, delimiter=",")
            if fh.products_list:
                writer.writerow(list(fh.products_list[1].keys()))
            for i in range(len(fh.products_list)):
                writer.writerow(list(fh.products_list[i].values()))

        with open("couriers.csv", "w") as couriers:
            writer = csv.writer(couriers, delimiter=",")
            if fh.couriers_list:
                writer.writerow(list(fh.couriers_list[1].keys()))
            for i in range(len(fh.couriers_list)):
                writer.writerow(list(fh.couriers_list[i].values()))

        with open("orders.csv", "w") as orders:
            writer = csv.writer(orders, delimiter=",")
            if fh.orders_list:
                writer.writerow(list(fh.orders_list[1].keys()))
            for i in range(len(fh.orders_list)):
                writer.writerow(list(fh.orders_list[i].values()))
        return None  # return without the none is buggy...
    elif cmd == "1":
        menu_type = "product"
        list_type = fh.products_list
        sub_menu(list_type, menu_type)
    elif cmd == "2":
        menu_type = "courier"
        list_type = fh.couriers_list
        sub_menu(list_type, menu_type)
    elif cmd == "3":
        menu_type = "order"
        list_type = fh.orders_list
        sub_menu(list_type, menu_type)
    else:
        incorrect_input()


def sub_menu(list_type, menu_type):
    if menu_type == "order":
        cmd = input(
            f"""Menu {menu_type.title()} Options: 
0 to return to main menu
1 to view 
2 to add
3 to update order status
4 to update existing order
5 to delete
>>> """
        )
    else:
        cmd = input(
            f"""Menu {menu_type.title()} Options: 
0 to return to main menu
1 to view 
2 to add
3 to update 
4 to delete
>>> """
        )
    if cmd == "0":
        main_menu()
    elif cmd == "1":
        x.view_list(list_type, menu_type)
    elif cmd == "2":
        if list_type == fh.orders_list:
            of.create_order(list_type, menu_type)
        else:
            x.create(list_type, menu_type)
    elif cmd == "3":
        if list_type == fh.orders_list:
            of.update_order_status(list_type, menu_type)
        else:
            x.update(list_type, menu_type)
    elif cmd == "4":
        if list_type == fh.orders_list:
            of.updating_existing_order(list_type, menu_type)
        else:
            x.delete(list_type, menu_type)
    elif cmd == "5":
        if list_type == fh.orders_list:
            x.delete(list_type, menu_type)
        else:
            incorrect_input()
    else:
        incorrect_input()


# main_menu()
# print('Have a nice day!')
