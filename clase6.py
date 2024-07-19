# operadores numericos
a = 10
b = 3 
print("suma:", a + b)
print("resta:", a - b)
print("multiplicacion:", a * b)
print("division:", a / b)
print("modulo:", a % b)
print("parte entera de la division:", a // b)
print("potenciacion:", a ** b)
#other ways to use +, -, / , * 
a += 2 
print(a)

# Example to illustrate PEMDAS
# Using the expression: (2 + 3) * 4**2 / 2 - 1

# Step-by-step breakdown:
# 1. Parentheses: (2 + 3) = 5
# 2. Exponents: 4**2 = 16
# 3. Multiplication and Division (from left to right): 5 * 16 / 2 = 40
# 4. Subtraction: 40 - 1 = 39

# Writing it in Python:
result = (2 + 3) * 4**2 / 2 - 1

print("The result of the expression (2 + 3) * 4**2 / 2 - 1 is:", result)