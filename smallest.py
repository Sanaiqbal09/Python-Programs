n=int(input("Enter the limit: "))
list=[]
for i in range(n):
    entry=int(input("Enter the number: "))
    list.append(entry)
smallest=list[0]
for entry in (list):
    if entry < smallest:
        smallest = entry
        
print("Smallest number= ",smallest)