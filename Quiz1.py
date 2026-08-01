#Write a program to find the student with the highest mark.
'''
highest=0
top_student=""
student = {
    "Sana": 90,
    "Amina": 85,
    "Hana": 95,
    "Aysha": 80
}
for name,marks in student.items():
    if marks > highest:
        highest=marks
        top_student=name
        
print("Top student = ",top_student)        
print("Highest Mark = ",highest)

'''

#Write a program to count how many students scored above 80.
'''
student = {
    "Sana": 90,
    "Amina": 85,
    "Hana": 95,
    "Aysha": 80
}
count=0
for mark in student.values():
    if mark > 80:
        count=count+1
print("students scored above 80 = ",count)
'''

#Write a program to reverse a string without using [::-1].
'''
string=input("Enter the string: ")
rev=""
for ch in (string):
    rev=ch+rev
print(rev)
'''

#Write a program to find duplicate numbers in a list.
'''
numbers=list(map(int,input("Enter the numbers: ").split()))    #input to list
duplicate=[]
for n in range(len(numbers)):
    for m in range(n+1,len(numbers)):
        if numbers[n] == numbers[m] and numbers[n] not in duplicate:
            duplicate.append(numbers[n])
print("Duplicates are: ",duplicate)
'''    

#Write a program to find the second largest number from a list entered by the user

numbers=list(map(int,input("Enter the numbers: ").split()))
numbers=list(set(numbers))
numbers.sort()
print(numbers[-2])



