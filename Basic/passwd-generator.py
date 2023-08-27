import random

passwd = ""
characters = "abcdefghijklmnopqrstuvwxyzçABCDEFGHIJKLMNOPQRSTUVWXYZÇ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/"

x = int(input("how many characters do you need? "))

for digit in range(x):
    ran = random.choice(characters)
    passwd += ran

print("-" *10, "Λ", "-" *10)
print(passwd)
print("-" *10, "V", "-" *10)
