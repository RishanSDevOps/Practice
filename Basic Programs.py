# Basic Programs

"""
1.Write a program that prints "Hello, World!" to the console.
2.To find largest of three numbers.
3.Accept two numbers from the user and print their sum.
4.program to determine if a number is even or odd.
5.Build a calculator to perform addition , subtraction , division , multilplication. 
6.Python code to check given number is positive, negative or zero
7.Program to print sum of all the digits of given number
8.find the factorial of a given number
9.python program to check if given number prime or not
10.python program to print prime numbers between 10 to 99
11.Accept 5 numbers from the user and display their cube values.
12.Program to reverse a given number.
13.To determine whether a given year is a leap year or not.
14.In certain university, grades are assigned to the marks obtained in respective subjects. Grades are assigned as given below.Write a python program to accept Marks in Math and display respective grade as an output using if…elif…elif..else statements (Using multiple conditions).
Hint : Relational operators: <, >, <=, >=, ==, !=
15. Write a python program to Print following statements as an output using print statement.
Student Name:
Address:
Contact _No:
Mother Tongue:
School_Name:
Year:
Panel:
Roll_No:
 b) In the previous code you written, modify the statements printing following fields  into multi-line comments, so these fields will not be the part of the output.
Address:
Contact _No:
Mother Tongue
16. Accept roll number, name and marks of three subjects and calculate pass or fail. Percentage and range of marks.
"""


# 1
print("Hello, World!")

# 2
a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

# 3
a = int(input())
b = int(input())
print(a + b)

# 4
a = int(input())
if a % 2 == 0:
    print("Even")
else:
    print("Odd")

# 5
a = float(input())
b = float(input())
o = input()
if o == "+":
    print(a + b)
elif o == "-":
    print(a - b)
elif o == "*":
    print(a * b)
elif o == "/":
    print(a / b)

# 6
a = int(input())
if a > 0:
    print("Pos")
elif a < 0:
    print("Neg")
else:
    print("Zero")

# 7
n = input()
s = 0
for d in n:
    s += int(d)
print(s)

# 8
n = int(input())
f = 1
for i in range(1, n + 1):
    f *= i
print(f)

# 9
n = int(input())
p = True
if n < 2:
    p = False
for i in range(2, n):
    if n % i == 0:
        p = False
        break
if p:
    print("Prime")
else:
    print("Not Prime")

# 10
for n in range(10, 100):
    p = True
    for i in range(2, n):
        if n % i == 0:
            p = False
            break
    if p:
        print(n)

# 11
for i in range(5):
    x = int(input())
    print(x**3)

# 12
n = input()
print(n[::-1])

# 13
y = int(input())
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print("Leap")
else:
    print("Not Leap")

# 14
m = int(input())
if m >= 90:
    print("A")
elif m >= 75:
    print("B")
elif m >= 50:
    print("C")
elif m >= 35:
    print("D")
else:
    print("F")

# 15
# a
print("Student Name:")
print("Address:")
print("Contact _No:")
print("Mother Tongue:")
print("School_Name:")
print("Year:")
print("Panel:")
print("Roll_No:")

# b
print("Student Name:")
"""
Address:
Contact _No:
Mother Tongue:
"""
print("School_Name:")
print("Year:")
print("Panel:")
print("Roll_No:")

# 16
r = input()
n = input()
m1 = int(input())
m2 = int(input())
m3 = int(input())
t = m1 + m2 + m3
p = t / 3
if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Pass")
else:
    print("Fail")
print("%:", p)
print("Min:", min(m1, m2, m3), "Max:", max(m1, m2, m3))

