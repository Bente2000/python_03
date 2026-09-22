#!/usr/bin/env python3

import sys

class KeyError(Exception):
    pass

class ValuesError(Exception):
    pass

class SyntaxError(Exception):
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



def display_inventory(args: list) -> None:
    i = 1
    keys = []
    values = []
    try:
        check_syntax(args) # waarom kan deze ook boven try
        while i < len(args):
            key, value = args[i].split(':')
            if i == 1:
                dic = {key: int(value)}
            else:
                dic.update({key: int(value)})
            keys.append(key)
            values.append(int(value))
            i += 1
    except KeyError as e:
        print(f"KeyError found: {e}")
    except SyntaxError as e:
        print(f"SyntaxError found: {e}")
    except ValuesError as e:
        print(f"ValuesError found: {e}")
    except ValueError as e:
        print(f"Quantity error: {e}")
    #print(f"Got inventory: {dic}") # wil nog doorgaan na 'hello' exception

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    display_inventory(sys.argv)
