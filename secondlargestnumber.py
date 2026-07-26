n=int(input("enter limit: "))
number=[]
for i in range(n):
    num=int(input(""))
    number.append(num)
number.sort()
print("second largest number= ",number[-2])
    