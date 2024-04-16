"""
Write a C++ program that contains a string (char pointer) with a value \Hello World’. The program should AND or and XOR each character in this string with 127 and display the result.
"""

str = "Hello World"

# AND each character with 127
and_result = [chr(ord(char) & 127) for char in str]
print("AND result:", "".join(and_result))

# XOR each character with 127
xor_result = [chr(ord(char) ^ 127) for char in str]
print("XOR result:", "".join(xor_result))
