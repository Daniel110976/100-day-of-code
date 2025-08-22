# Logical Operators
# and, or, not

# and = true if both operands are true
# true and true = true
# true and false = false
# false and false = false

# or = true if at least one operand is true
# true or false = true
# false or true = true
# false or false = false

# not = reverses the boolean value
# not true = false
# not false = true
# ! = not, !true = false, !false = true

a = 5
b = 7
 
if a >= b and a != b:
    print("A")
elif not a >= b and a != b:
    print("B")
else:
    print("C")