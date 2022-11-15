import extra_functions as x
import file_handlers as fh
import cafe_app as a


def create_order(list_type, menu_type):
    temp_dict = {
        "customer_name": "",
        "customer_address": "",
        "customer_phone_number": "",
        "product_id_index": "",
        "courier_id": "",
        "status": "preparing",
    }
    for key, _ in temp_dict.items():
        if not key == "status":
            if key == "product_id_index":
                for item in fh.products_list:
                    print(item)
                product_id_info = [
                    id
                    for id in input(
                        "Input product id(s). Leave space for multiple ids\n"
                    ).split()
                ]
                id_str_list = ""
                for id in product_id_info:
                    if id not in [value["id"] for value in fh.products_list]:
                        print(f"id {id} does not exist. Order details cancelled")
                        a.sub_menu(list_type, menu_type)
                    if not product_id_info:
                        a.incorrect_input()
                    else:
                        id_str_list += id + ","
                        temp_dict[key] = id_str_list[:-1]
            elif key == "courier_id":
                for courier in fh.couriers_list:
                    print(courier)
                input_info_str = input(f"Input {key.replace('_', ' ')}\n")
                if not input_info_str:
                    a.incorrect_input()
                if input_info_str not in [value["id"] for value in fh.couriers_list]:
                    print(
                        f"id {input_info_str} does not exist. Order details cancelled"
                    )
                    a.sub_menu(list_type, menu_type)
                else:
                    temp_dict[key] = input_info_str
            else:
                input_info_str = input(f"Input {key.replace('_', ' ')}\n")
                if not input_info_str:
                    a.incorrect_input()
                else:
                    temp_dict[key] = input_info_str
        else:
            break
    list_type.append(temp_dict)
    x.view_list(list_type, menu_type)


def update_order_status(list_type, menu_type):
    if len(list_type) == 0:
        x.view_list(list_type, menu_type)
    else:
        for index, order in enumerate(fh.orders_list):
            print(index, order)
        try:
            order_number = int(input("Input order number to change status\n"))
            if order_number == 0 or order_number < len(list_type):
                print(fh.orders_list[order_number])
                order_number_status = int(
                    input(
                        """To change status, input: 
1 for preparing
2 for dispatched
3 for delivered
4 to return to menu \n"""
                    )
                )
                if order_number_status == 1:
                    if fh.orders_list[order_number]["status"] == "preparing":
                        print("Status already set to preparing")
                        a.sub_menu(list_type, menu_type)
                    else:
                        fh.orders_list[order_number].update({"status": "preparing"})
                        x.view_list(list_type, menu_type)
                elif order_number_status == 2:
                    if fh.orders_list[order_number]["status"] == "dispatched":
                        print("Status already set to dispatched")
                    else:
                        fh.orders_list[order_number].update({"status": "dispatched"})
                        x.view_list(list_type, menu_type)
                elif order_number_status == 3:
                    if fh.orders_list[order_number]["status"] == "delivered":
                        print("Status already set to delivered")
                    else:
                        fh.orders_list[order_number].update({"status": "delivered"})
                        x.view_list(list_type, menu_type)
                elif order_number_status == 4:
                    a.sub_menu(list_type, menu_type)
                else:
                    a.incorrect_input()
            else:
                print(f"Order {order_number} isn't in {menu_type} list")
                x.view_list(list_type, menu_type)
        except (ValueError, KeyError):
            print("Invalid input")
            a.sub_menu(list_type, menu_type)


def updating_existing_order(list_type, menu_type):
    for index, order in enumerate(fh.orders_list):
        print(index, order)
    try:
        order_number = int(input("Input number of order you would like to update\n"))
        for key, _ in fh.orders_list[order_number].items():
            if key == "status":
                continue
            elif key == "product_id_index":
                for item in fh.products_list:
                    print(item)
                product_id_info = [
                    id
                    for id in input(
                        "Input product id(s). Leave space for multiple ids\n"
                    ).split()
                ]
                id_str_list = ""
                for id in product_id_info:
                    if product_id_info and id not in [
                        value["id"] for value in fh.products_list
                    ]:
                        print(f"id {id} does not exist. Order details cancelled")
                        a.sub_menu(list_type, menu_type)
                    elif not product_id_info:
                        continue
                    else:
                        id_str_list += id + ","
                        fh.orders_list[order_number][key] = id_str_list[:-1]
            elif key == "courier_id":
                for courier in fh.couriers_list:
                    print(courier)
                input_info_str = input(f"Input {key.replace('_', ' ')}\n")
                if input_info_str and input_info_str not in [
                    value["id"] for value in fh.couriers_list
                ]:
                    print(
                        f"id {input_info_str} does not exist. Order details cancelled"
                    )
                    a.sub_menu(list_type, menu_type)
                else:
                    if not input_info_str:
                        continue
                    else:
                        fh.orders_list[order_number][key] = input_info_str
            else:
                info = input(f"Input new {key.replace('_', ' ')}\n")
                if not info:
                    continue
                else:
                    fh.orders_list[order_number][key] = info
    except IndexError or TypeError:
        a.incorrect_input()
    x.view_list(list_type, menu_type)
