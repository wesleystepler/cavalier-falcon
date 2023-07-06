# Wesley Stepler (pws3ms)
# CS 3710: Introduction to Cybersecurity
# Professor Orebaugh
# Programing Assignment 2: RSA Encryption

import sympy, random, math

# Generate random values for p and q
p = sympy.randprime(1, 10000)
print(f"p = {p}")

q = sympy.randprime(1, 10000)
print(f"q = {q}")

# Calculate n and phi(n)
n = p*q
phi_n = (p-1)*(q-1)

#Select e
e = None
while e == None:
    # Keep picking values such that 1 < temp < phi_n
    temp = random.randint(2, (phi_n)-1)
    # If the value is relatively prime to phi_n, set e to that value
    if math.gcd(temp, phi_n) == 1:
        e = temp
print(f"e = {e}")

# Keep checking values from 1 to phi_n. When that value * e % phi_n is 1, set d to that value
for i in range(1, phi_n):
    if (i*e) % phi_n == 1:
        d = i
print(f"d = {d}")

# Enter Message to be encrypted
M = int(input("Enter message: "))

# Encrypt
cipher_text = (M**e) % n
print(f"Encrypted Message: {cipher_text}") 

#Decrypt
plaintext = ((cipher_text**d) % n)
print(f"Decrypted Message: {plaintext}")
