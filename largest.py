#Largest of 3 numbers
'''
n1=int(input("enter 1st number"))
n2=int(input("enter 2nd number"))
n3=int(input("enter 3rd number"))
if n1 > n2 and n1 > n3:
    print(n1,"is largest")
elif n2 > n1 and n2 > n3:
    print(n2,"is largest")
else:
    print(n3,"is largest")
'''

#To find largest from given input by user

n=int(input("Enter the limit: "))
list=[]
for i in range(n):
    num=int(input(""))
    list.append(num)
largest=list[0]
for num in (list):
    if num > largest:
        largest = num
print("largest is= ",largest)