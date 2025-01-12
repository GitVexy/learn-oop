#!/usr/bin/env python3
import sys

# Generates init variables for python class. Requires bash function (bottom)
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

""" Import function to ~/.bash_functions and source to enable. generate_init.py must be in $PATH!

# Copies python __init__ variables to clipboard "pyinit 'a, b, c' [2] [-p]"
pyinit() {
    INT="\033[0;35mint\033[0m"
    TWO="\033[0;35m2\033[0m"
    BLU="\033[0;34m"
    CY="\033[0;36m"
    RE="\033[0m"
    GRN="\033[0;32m"
    YE="\033[0;33m"
    if [ $# -eq 0 ]; then
        echo "No arguments provided. pyinit -h for help"
        return 1
    elif [ $# -gt 3 ]; then
        echo "Too many arguments. pyinit -h for help"
        return 1
    elif [[ " ${1} " =~ " -h " ]] || [[ " ${1} " =~ " --help " ]]; then
        echo -e "$RE"
        echo -e "Format: pyinit$CY 'a, b, c'$RE [$TWO] [$BLU-p$RE]"
        echo ""
        echo -e "  $INT = tab depth (default = $TWO, optional, starts at line 2)"
        echo -e "  $BLU-p$RE =$BLU private$RE (must be last)"
        echo ""
        echo "Examples:"
        echo -e "  pyinit$CY 'a, b, c'$RE $TWO $BLU-p$RE   # With tab depth set to $TWO and$BLU private$RE variables"
        echo -e "  pyinit$CY 'a, b, c'$RE   $BLU-p$RE   # With default tab depth and$BLU private$RE variables"
        echo -e "  pyinit$CY 'a, b, c'$RE        # With default tab depth and no private variables"
        echo ""
        echo -e $GRN"user: $ $RE pyinit$CY 'a, b, c'$RE $TWO $BLU-p$RE "
        echo -e "(Copies the following to clipboard:)$YE"
        echo "self.__a = a"
        echo "        self.__b = b"
        echo "        self.__c = c"
        echo -e "$RE"
        return 0
    elif [[ " ${2} " =~ " -p " ]]; then
        python3 /home/vexy/development/github.com/GitVexy/learn-oop/generate_init.py "$1" "-p" | xclip -selection clipboard
        echo "Copied to clipboard: $1 with default (2) tabs (private)"
    elif [ -n "$2" ] && [ ! -n "$3" ]; then
        python3 /home/vexy/development/github.com/GitVexy/learn-oop/generate_init.py "$1" "$2" | xclip -selection clipboard
        echo "Copied to clipboard: $1 with $2 tabs"
    # Check if "-p" is in the arguments
    elif [[ " ${3} " =~ " -p " ]]; then
        python3 /home/vexy/development/github.com/GitVexy/learn-oop/generate_init.py "$1" "$2" "-p" | xclip -selection clipboard
        echo "Copied to clipboard: $1 with $2 tabs (private)"
    else
        python3 /home/vexy/development/github.com/GitVexy/learn-oop/generate_init.py "$1" | xclip -selection clipboard
        echo "Copied to clipboard: $1"
    fi
}
"""