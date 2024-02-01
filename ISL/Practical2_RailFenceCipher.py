"""

Write a Python program to perform encryption and decryption using the method of Transposition technique.

There are many different transposition techniques, each with its own strengths and weaknesses. Some of the most well-known methods include:

1) Rail fence cipher: This technique involves writing the plaintext in "zigzag" rows across a grid, then reading the letters off row by row.

2) Columnar transposition cipher: This technique involves writing the plaintext in columns of a certain width, then reading the letters off column by column in a different order determined by a key.

3) Route cipher: This technique involves following a specific path through a grid to rearrange the letters of the plaintext.

"""

# 1) Rail Fence Cipher

def encryptRailFence(text, key):
   """Encrypts text using the rail fence cipher."""

   rail = [['\n' for i in range(len(text))] 
           for j in range(key)]
   dir_down = False
   row, col = 0, 0

   for i in range(len(text)):
       rail[row][col] = text[i]
       col += 1

       if (row == 0) or (row == key - 1):
           dir_down = not dir_down

       if dir_down:
           row += 1
       else:
           row -= 1

   result = []
   for i in range(key):
       for j in range(len(text)):
           if rail[i][j] != '\n':
               result.append(rail[i][j])
   return("" . join(result))

def decryptRailFence(cipher, key):
   """Decrypts text using the rail fence cipher."""

   rail = [['\n' for i in range(len(cipher))] 
           for j in range(key)]
   dir_down = None
   row, col = 0, 0

   for i in range(len(cipher)):
       if row == 0:
           dir_down = True
       if row == key - 1:
           dir_down = False
       rail[row][col] = '*'
       col += 1

       if dir_down:
           row += 1
       else:
           row -= 1

   index = 0
   for i in range(key):
       for j in range(len(cipher)):
           if ((rail[i][j] == '*') and
               (index < len(cipher))):
               rail[i][j] = cipher[index]
               index += 1

   result = []
   row, col = 0, 0
   for i in range(len(cipher)):
       if row == 0:
           dir_down = True
       if row == key - 1:
           dir_down = False
       if (rail[row][col] != '*'):
           result.append(rail[row][col])
           col += 1

       if dir_down:
           row += 1
       else:
           row -= 1
   return("".join(result))

# Example usage
text = "Sinhgad"
key = 3

encrypted_text = encryptRailFence(text, key)
print("Encrypted text:", encrypted_text)

decrypted_text = decryptRailFence(encrypted_text, key)
print("Decrypted text:", decrypted_text)
