n=int(input("Enter the limit: "))
list=[]
odd=0
even=0
for i in range(n):
    entry=(int(input("Enter the number: ")))
    list.append(entry)
    #6 and 7 lines we can type as one line like below
    #list.append((int(input("Enter the number: "))))
    
for entry in (list):
    if entry % 2 == 0:
        even=even+1
    else:
        odd=odd+1
print("Odd numbers = ",odd)
print("even numbers = ",even)
