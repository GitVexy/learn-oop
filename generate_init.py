#!/usr/bin/env python3
import sys

# Generates init variables for python class. Requires bash function (separate file)
def generate_init(s, tabs=2, is_private=False):
    indent = "    " * tabs
    first_var = True
    for word in s.split(", "):
        if is_private:
            var_name = f"__{word}"
        else:
            var_name = word
        
        if first_var:
            print(f"self.{var_name} = {word}")
            first_var = False
        else:
            print(f"{indent}self.{var_name} = {word}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: generate_init.py 'var1, var2, var3' [tabs | private]")
    else:
        variables = sys.argv[1]
        is_private = False
        tabs = 2

        # Check for "-p" in any of the arguments, and set is_private flag
        if "-p" in sys.argv:
            is_private = True
            sys.argv.remove("-p")  # Remove "-p" from the argument list

        # Check if there's a second argument and it's a number for tabs
        if len(sys.argv) > 2:
            try:
                tabs = int(sys.argv[2])
            except ValueError:
                pass

        generate_init(variables, tabs, is_private)
