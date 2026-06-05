
# ---------- 1. COMMENTS ----------
# This is a single-line comment
print("Hello! Let's learn Python fundamentals!")

"""
This is a
multi-line comment
(also called docstring)
"""

# ---------- 2. VARIABLES AND DATA TYPES ----------
print("\n" + "="*50)
print("VARIABLES AND DATA TYPES")
print("="*50)

# Numbers
age = 25                    # Integer (int)
price = 19.99              # Float (float)
complex_num = 3 + 4j       # Complex number

# Text
name = "Alice"             # String (str)
message = 'Python is fun!' # String with single quotes

# Boolean
is_student = True          # Boolean (bool)
has_job = False

# Display variables and their types
print(f"Name: {name} (Type: {type(name)})")
print(f"Age: {age} (Type: {type(age)})")
print(f"Price: ${price} (Type: {type(price)})")
print(f"Is Student: {is_student} (Type: {type(is_student)})")

# ---------- 3. TYPE CONVERSION ----------
print("\n" + "="*50)
print("TYPE CONVERSION")
print("="*50)

# String to Integer
num_str = "100"
num_int = int(num_str)
print(f'Converting "{num_str}" to integer: {num_int}')

# Integer to Float
num_float = float(age)
print(f"Converting {age} to float: {num_float}")

# Number to String
age_str = str(age)
print(f"Converting {age} to string: '{age_str}'")

# Float to Integer (truncates decimal)
pi = 3.14159
pi_int = int(pi)
print(f"Converting {pi} to integer: {pi_int}")

# ---------- 4. STRING OPERATIONS ----------
print("\n" + "="*50)
print("STRING OPERATIONS")
print("="*50)

greeting = "Hello"
name = "Bob"

# String concatenation
combined = greeting + " " + name
print(f"Concatenation: {combined}")

# String repetition
laugh = "Ha" * 3
print(f"Repetition: {laugh}")

# String methods
text = "  Python Programming  "
print(f"Original: '{text}'")
print(f"Strip whitespace: '{text.strip()}'")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Replace: {text.replace('Python', 'Java')}")
print(f"Split: {text.split()}")

# String formatting (f-strings)
name = "Charlie"
score = 95
print(f"Student: {name}, Score: {score}")

# String slicing
word = "Programming"
print(f"Word: {word}")
print(f"First 3 chars: {word[:3]}")
print(f"Last 3 chars: {word[-3:]}")
print(f"Reverse: {word[::-1]}")

# ---------- 5. BASIC OPERATORS ----------
print("\n" + "="*50)
print("BASIC OPERATORS")
print("="*50)

a = 10
b = 3

# Arithmetic operators
print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponent: {a} ** {b} = {a ** b}")

# Comparison operators
print(f"\nComparison Operators:")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")

# Logical operators
print(f"\nLogical Operators:")
x = True
y = False
print(f"x = {x}, y = {y}")
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}")

# ---------- 6. GETTING USER INPUT ----------
print("\n" + "="*50)
print("USER INPUT")
print("="*50)

# In Colab, you can use input() - it will prompt in the cell output
name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"\nHello {name}! You are {age} years old.")
print(f"In 5 years, you will be {int(age) + 5} years old!")

# ---------- 7. CONDITIONAL STATEMENTS ----------
# Example 1: Simple if
temperature = int(input("Enter the temperature"))
print(f"Temperature: {temperature}°C")

if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("It's warm outside! ")
elif temperature > 10:
    print("It's cool outside! ")
else:
    print("It's cold outside! ")

# Example 2: Nested conditions
age = int(input("Enter your age:"))
has_license = bool(input("Enter 'True' if you have licence and 'False' if you dont have it:"))

if age >= 18:
    if has_license:
        print("You can drive a car! ")
    else:
        print("You're old enough but need a license first!")
else:
    print("You're too young to drive!")

# FOR loop - iterating over a range
print("For loop - Counting 1 to 5:")
for i in range(1, 6):
    print(f"Count: {i}")
