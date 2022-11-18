import cafe_app as a
import file_handlers as fh


def view_list(list_type, menu_type):
    if len(list_type) == 0:
        print(f"{menu_type.title()} list is empty.\n")
        a.sub_menu(list_type, menu_type)
    else:
        for item in list_type:
            print(item)
        a.sub_menu(list_type, menu_type)
        
def id_generator(temp_dict):
    temp_dict.update(
        {
            "id": "".join(
                [
                    value[:2]
                    for key, value in temp_dict.items()
                    if key == "name" 
                ]
            )
            + "".join(
                [
                    value
                    for key, value in temp_dict.items()
                    if key == "id"
                ]
            )
            + "".join(
                [
                    value[-1]
                    for key, value in temp_dict.items()
                    if key == "name"
                ]
            )
        }
    )
    return temp_dict


def create(list_type, menu_type):
    temp_dict = {}
    if len(list_type) == 0:
        view_list(list_type, menu_type)
    if menu_type == "product":
        temp_dict = {"id": (len(list_type)), "name": "", "price": ""}
    elif menu_type == "courier":
        temp_dict = {"id": len(list_type), "name": "", "phone_number": ""}

    for key, _ in temp_dict.items():
        if key == "id":
            temp_dict[key] += 1
            temp_dict[key] = str(temp_dict[key])
        elif key == "price":
            try:
                input_info_int = float(input(f"Input {key.replace('_', ' ')}\n"))
                temp_dict[key] = input_info_int
                break
            except ValueError:
                a.incorrect_input()
        else:
            input_info_str = input(f"Input {key.replace('_', ' ')}\n")
            if not input_info_str:
                a.incorrect_input()
            else:
                temp_dict[key] = input_info_str

    id_generator(temp_dict)
    list_type.append(temp_dict)
    return view_list(list_type, menu_type)


def update(list_type, menu_type):
    if len(list_type) == 0:
        view_list(list_type, menu_type)
    else:
        for item in list_type:
            print(item)
        info = input(f"Input id of {menu_type}\n")
        if info in [value["id"] for value in list_type]:
            index = next(
                (index for (index, key) in enumerate(list_type) if key["id"] == info),
                None,
            )
            for key, _ in list_type[int(index)].items():
                if key == "price":
                    try:
                        input_info_int = float(
                            input(f"Input {key.replace('_', ' ')}\n")
                        )
                        list_type[index][key] = input_info_int
                    except TypeError and ValueError:
                        continue
                else:
                    if not key == "id":
                        input_info_str = input(f"Input {key.replace('_', ' ')}\n")
                        if not input_info_str:
                            continue
                        else:
                            list_type[index][key] = input_info_str
                    else:
                        continue
            list_type[index].update({"id": str(len(list_type))})        
            list_type[index].update(
        {
            "id": "".join(
                [
                    value[:2]
                    for key, value in list_type[index].items()
                    if key == "name" 
                ]
            )
            + "".join(
                [
                    value
                    for key, value in list_type[index].items()
                    if key == "id"
                ]
            )
            + "".join(
                [
                    value[-1]
                    for key, value in list_type[index].items()
                    if key == "name"
                ]
            )
        }
    )
        else:
            a.incorrect_input()
    view_list(list_type, menu_type)


def delete(list_type, menu_type):
    if len(list_type) == 0:
        view_list(list_type, menu_type)
    elif list_type == fh.orders_list:
        for index, order in enumerate(fh.orders_list):
            print(index, order)
        try:
            order_number = int(
                input("Input number of order you would like to delete\n")
            )
            del fh.orders_list[order_number]
        except (IndexError, ValueError):
            a.incorrect_input()
        view_list(list_type, menu_type)
    else:
        for item in list_type:
            print(item)
        info = input(f"Input id of {menu_type} to delete\n")
        if [value["id"] for value in list_type if info in value["id"]]:
            index = next(
                (index for (index, key) in enumerate(list_type) if key["id"] == info),
                None,
            )
            del list_type[index]
            for item in fh.orders_list:
                for key, _ in item.items():
                    if (
                        list_type == fh.products_list
                        and key == "product_id_index"
                        and str(index + 1) in item[key]
                    ):
                        item.update(
                            {
                                "product_id_index": ",".join(
                                    [
                                        value
                                        for value in [*item[key]]
                                        if value != "," and value != str(index + 1)
                                    ]
                                )
                            }
                        )
                    elif (
                        list_type == fh.couriers_list
                        and key == "courier_id"
                        and str(index + 1) in item[key]
                    ):
                        item.update(
                            {
                                "courier_id": ",".join(
                                    [
                                        value
                                        for value in [*item[key]]
                                        if value != "," and value != str(index + 1)
                                    ]
                                )
                            }
                        )
            for item in fh.orders_list:
                print(item)  # checking to see if id deleted from id index
            view_list(list_type, menu_type)
        else:
            a.incorrect_input()
