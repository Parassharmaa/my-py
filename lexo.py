n = list(input("Enter Name: "))
n.sort(key=lambda x: x.strip(' '))
print("Name in lexo:", end="")
print("".join(n))

