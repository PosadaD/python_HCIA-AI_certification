#What is control flow?
#the control flow of a program is the execution order of the program code.
#There are three basic control flow structures in python.

#1) Sequencial structure
#2) Branch structure 
#3) Loop structure

#if statement 
age = 16
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

#loops 
count = 1
while count <= 5:
    print(count)
    count += 1  # Increment the count to avoid an infinite loop

#for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)

matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]];
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()  # For new line after each row


