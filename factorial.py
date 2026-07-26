num = int(input("Enter a number: "))
fact = 1

for i in range(num, 0, -1):
    print(i, end="")

    if i != 1:
        print(" * ", end="")
    else:
        print(" = ", end="")

    fact = fact * i

print(fact)