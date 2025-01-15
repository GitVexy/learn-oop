from operator import neg, pos


class Calc():
    def __init__(self, value):
        self.value = value
    
    def get_value(self):
        return self.value
    
    def check_type(self, other):
        if not isinstance(other, Calc):
            raise TypeError(f"\n{other} is of type {type(other)}, not {Calc}")
    
    def __add__(self, other):
        self.check_type(other)
        
        a = self.value
        b = other.get_value()
        return Calc(a + b)

    def __sub__(self, other):
        self.check_type(other)
        
        a = self.value
        b = other.get_value()
        return Calc(a - b)

    def __mul__(self, other):
        self.check_type(other)
        
        a = self.value
        b = other.get_value()
        return Calc(a * b)

    def __pow__(self, other):
        self.check_type(other)

        a = self.value
        b = other.get_value()
        return Calc(a ** b)

    def __truediv__(self, other):
        self.check_type(other)

        a = self.value
        b = other.get_value()
        return Calc(a / b)

    def __floordiv__(self, other):
        self.check_type(other)

        a = self.value
        b = other.get_value()
        return Calc(a // b)

    def __mod__(self, other):
        self.check_type(other)

        a = self.value
        b = other.get_value()
        return Calc(a % b)

    def __lshift__(self, other):
        self.check_type(other)

        a = self.value
        b = other.get_value()
        return Calc(a << b)

    def __rshift__(self, other):
        self.check_type(other)

        a = self.value
        b = other.get_value()
        return Calc(a >> b)

    def __and__(self, other):
        self.check_type(other)

        a = self.value
        b = other.get_value()
        return Calc(a & b)

    def __or__(self, other):
        self.check_type(other)

        a = self.value
        b = other.get_value()
        return Calc(a | b)

    def __xor__(self, other):
        self.check_type(other)

        a = self.value
        b = other.get_value()
        return Calc(a ^ b)

    def __invert__(self):
        a = self.value
        return Calc(~ a)
    
    def __pos__(self):
        return Calc(self.get_value())
        
    def __neg__(self):
        return Calc(0 - self.get_value())
        
    def __abs__(self):
        if self.get_value() < 0:
            return Calc(0 - self.get_value())
        return self

def main():
    
    a = Calc(5)
    b = Calc(2)
    c = ""

    print("--------------------------------------------\n")
    print("Starting evaluation")

    print(f"\na = {a.get_value()}\nb = {b.get_value()}\n")
    print("Arithmatic operators:")
    print(f"Addition            {a.get_value()}  +   {b.get_value()}  =  {(a +  b).get_value()}")
    print(f"Subtraction         {a.get_value()}  -   {b.get_value()}  =  {(a -  b).get_value()}")
    print(f"Multiplication      {a.get_value()}  *   {b.get_value()}  =  {(a *  b).get_value()}")
    print(f"Power               {a.get_value()}  **  {b.get_value()}  =  {(a ** b).get_value()}")
    print(f"Division            {a.get_value()}  /   {b.get_value()}  =  {(a /  b).get_value()}")
    print(f"Floor Division      {a.get_value()}  //  {b.get_value()}  =  {(a // b).get_value()}")
    print(f"Remainder (modulo)  {a.get_value()}  %   {b.get_value()}  =  {(a %  b).get_value()}")

    print("\nBitwise:")

    print(f"Bitwise Left Shift  {bin(a.get_value())[2:]:>5}  << {bin(b.get_value())[2:]:>5}  =  {bin((a << b).get_value())[2:]:>5}    (decimal: {(a << b).get_value ( )})")
    print(f"Bitwise Right Shift {bin(a.get_value())[2:]:>5}  >> {bin(b.get_value())[2:]:>5}  =  {bin((a >> b).get_value())[2:]:>5}    (decimal: {(a >> b).get_value ( )} )")
    print(f"Bitwise AND         {bin(a.get_value())[2:]:>5}  &  {bin(b.get_value())[2:]:>5}  =  {bin((a & b).get_value())[2:]:>5}    (decimal: {(a & b).get_value()} )  ")
    print(f"Bitwise OR          {bin(a.get_value())[2:]:>5}  |  {bin(b.get_value())[2:]:>5}  =  {bin((a | b).get_value())[2:]:>5}    (decimal: {(a | b).get_value   ( )} )")
    print(f"Bitwise XOR         {bin(a.get_value())[2:]:>5}  ^  {bin(b.get_value())[2:]:>5}  =  {bin((a ^ b).get_value())[2:]:>5}    (decimal: {(a ^ b).get_value()} )  ")
    print(f"Bitwise NOT                ~  {bin(a.get_value())[2:]:>5}  =  {bin((  ~  a).get_value())[2:]:>5}    (decimal: {(  ~ a).get_value()})")

    a = Calc(-5)
    b = Calc(5)

    print(f"\na = {a.get_value()}\nb = {b.get_value()}")
    print("\nUnary operators:\n")
    print(f"Running +(a) = {+a.get_value()}")
    print(f"Running -(b) = {-b.get_value()}")
    print(f"Running abs(a) = {abs(a).get_value()}")

main()

""" 
Outputs:

--------------------------------------------

Starting evaluation

a = 5
b = 2

Arithmatic operators:
Addition            5  +   2  =  7
Subtraction         5  -   2  =  3
Multiplication      5  *   2  =  10
Power               5  **  2  =  25
Division            5  /   2  =  2.5
Floor Division      5  //  2  =  2
Remainder (modulo)  5  %   2  =  1

Bitwise:
Bitwise Left Shift    101  <<    10  =  10100    (decimal: 20)
Bitwise Right Shift   101  >>    10  =      1    (decimal: 1 )
Bitwise AND           101  &     10  =      0    (decimal: 0 )  
Bitwise OR            101  |     10  =    111    (decimal: 7 )
Bitwise XOR           101  ^     10  =    111    (decimal: 7 )  
Bitwise NOT                ~    101  =   b110    (decimal: -6)

a = -5
b = 5

Unary operators:

Running +(a) = -5
Running -(b) = -5
Running abs(a) = 5
"""