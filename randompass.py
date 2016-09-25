import random as rand


def rand_char():
    c = chr(rand.randrange(97,122))
    return c


n = int(input("Enter length of pass:"))

for _ in range(5):
    for __ in range(n):
        print(rand_char(), end="")
    print(" ")
