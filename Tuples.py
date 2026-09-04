# Tuples

"""
Write a program to print the 4th element from first and 4th element from last in a tuple. 
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90) 
print("Tuple:", numbers) 
print("4th element from first:", numbers[3]) 
print("4th element from last:", numbers[-4])

2 Write a program to check whether an element exists in a tuple or not.

numbers = (10, 20, 30, 40, 50) 
element = int(input("Enter element to search: ")) 
if element in numbers: 
print("Element exists in the tuple") 
else: 
print("Element does not exist in the tuple")
 

3 Write a program to convert a list into a tuple. 

numbers_list = [10, 20, 30, 40, 50] 
numbers_tuple = tuple(numbers_list)
 print("List:", numbers_list) 
print("Tuple:", numbers_tuple)

4 Write a program to find the index of an item in a tuple. 
numbers = (10, 20, 30, 40, 50)
 element = int(input("Enter element: ")) 
if element in numbers:
 print("Index of element:", numbers.index(element)) 
else: 
print("Element not found")

5 Write a program to replace last value of tuples in a list to 100. 
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)] 

numbers = [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
new_list = [] 
for tup in numbers: 
new_tup = tup[:-1] + (100,) 
new_list.append(new_tup) 
print("Original List:", numbers) 
print("Updated List:", new_list)

6.Python program to find the maximum and minimum element in a tuple.
 
 numbers = (25, 10, 45, 5, 60, 30) 
maximum = max(numbers) 
minimum = min(numbers) 
print("Tuple:", numbers) 
print("Maximum element:", maximum) 
print("Minimum element:", minimum)

7.Python program to swap the first and last element of a tuple.
numbers = (10, 20, 30, 40, 50) 
new_tuple = (numbers[-1],) + numbers[1:-1] + (numbers[0],) 
print("Original Tuple:", numbers) 
print("Tuple after swapping:", new_tuple)
"""

# 1
a = (10, 20, 30, 40, 50, 60, 70, 80, 90)
print(f"a: {a}\n4th 1st: {a[3]}\n4th last: {a[-4]}")

# 2
a = (10, 20, 30, 40, 50)
x = int(input())
print("Yes" if x in a else "No")

# 3
a = [10, 20, 30, 40, 50]
b = tuple(a)
print(f"L: {a}\nT: {b}")

# 4
a = (10, 20, 30, 40, 50)
x = int(input())
print(a.index(x) if x in a else "No")

# 5
a = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
b = [x[:-1] + (100,) for x in a]
print(b)

# 6
a = (25, 10, 45, 5, 60, 30)
print(f"Max: {max(a)} Min: {min(a)}")

# 7
a = (10, 20, 30, 40, 50)
b = (a[-1],) + a[1:-1] + (a[0],)
print(b)
