#!/usr/bin/env python3

import sys

class TooManyValues: # sword::3 == syntax error == Exception
    pass

class NotEnoughValues: # sword: 3 == syntax error == Exception
    pass

def value_check(arg: str) -> None: # saus
    key, value = arg.split(':')
    number = 0
    if  number is int(key):
        raise TypeError

def display_inventory(args: list) -> None:
    i = 1
    keys = []
    values = []
    try:
        while i < len(args):
            key, value = args[i].split(':')
            keys.append(key)
            values.append(int(value))
            i += 1
    except TypeError as e: # hoezo deze niet bij 3:abc ??
        print(f"Caught TypeError: {e}")
    #except Exception as e:
    #    print(f"Caught Exception: {e}")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print(keys)
    print(values)

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    args = sys.argv
    print(args)
    display_inventory(args)
    #display_items()
    #display_percentages()
    #display_abundance()
    #update_inventory()
