#!/usr/bin/env python3

import sys

class KeyError(Exception):
    pass

class ValuesError(Exception):
    pass

class SyntaxError(Exception):
    pass

class QuantityError(Exception):
    pass

def check_syntax(args: list) -> None:
    i = 1
    j = 0
    while i < len(args):
        input = args[i].partition(':')
        if input[0] == "":
            raise KeyError("No key found")
        if input[1] == "":
            raise SyntaxError(f"Invalid parameter: {input[0]}")
        if input[2] == "":
            raise ValuesError("No value found")
        while j < len(input[2]):
            if input[2][j] == ':':
                raise SyntaxError("Extra delimeter")
            j += 1
        i += 1

def add_to_inventory(inventory: dict[str,int], item: str) -> None:
    try:
        key, value = item.split(':', 1)
        if key == "" or value == "":
            raise ValueError
    except ValueError as e:
        raise SyntaxError(f"for '{item}': no value found") from e
    if key in inventory:
        raise ValueError(f"Duplicate item '{key}' found, discarding")
    if ':' in value:
        raise SyntaxError(f"invalid value: {value}")
    try:
        inventory[key] = int(value)
    except ValueError as e:
        raise QuantityError(f"for '{key}': {e}") from e

def display_inventory(args: list) -> None:
    inventory: dict[str,int] = {}
    for arg in args[1:]:
        try:
            add_to_inventory(inventory, arg)
        except Exception as e:
            print(f"{type(e).__name__} {e}")
    print(f"inventory: {inventory}")
    print(f"item list: {list(inventory.keys())}")
    item_sum = sum(inventory.values())
    print(f"total quantity of the {len(inventory.keys())} items: {item_sum}")
    for item,quantity in inventory.items():
        percent = float(quantity) / (float(item_sum) * 0.01)
        print(f"Item {item} represents {round(percent, 1)}%")
    max_item = max(inventory.items(), key=lambda kv: kv[1])
    min_item = min(inventory.items(), key=lambda kv: kv[1])
    print(f"Item most abundant: {max_item[0]} with quantity {max_item[1]}")
    print(f"Item least abundant: {min_item[0]} with quantity {min_item[1]}")
    add_to_inventory(inventory, "magic_item:1")
    print(f"Updated inventory: {inventory}")
    # i = 1
    # keys = []
    # values = []
    # try:
    #     check_syntax(args) # waarom kan deze ook boven try
    #     while i < len(args):
    #         key, value = args[i].split(':')
    #         if i == 1:
    #             dic = {key: int(value)}
    #         else:
    #             dic.update({key: int(value)})
    #         keys.append(key)
    #         values.append(int(value))
    #         i += 1
    # except KeyError as e:
    #     print(f"KeyError found: {e}")
    # except SyntaxError as e:
    #     print(f"SyntaxError found: {e}")
    # except ValuesError as e:
    #     print(f"ValuesError found: {e}")
    # except ValueError as e:
    #     print(f"Quantity error: {e}")
    #print(f"Got inventory: {dic}") # wil nog doorgaan na 'hello' exception

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    display_inventory(sys.argv)
