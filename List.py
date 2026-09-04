# Lists

"""
1 Write a program to create a list of 5 integers and display the list items. Access individual elements through index. 
2 Write a program to append a new item to the end of the list. 
3 Write a program to reverse the order of the items in the list. 
4 Write a program to print the number of occurrences of a specified element in a list. 
5 Write a program to append the items of list1 to list2 in the front. 
6 Write a program to insert a new item before the second element in an existing list. 
7 Write a program to remove the item from a specified index in a list. 
8 Write a program to remove the first occurrence of a specified element from a list. 
9 Accept 20 values from user and save it in list. Perform following operations on it
 a) count similar elements of list and print their index value   
b) count even and odd values of list 
c) count positive and negative values of list.
10 Accept 10 values from user and save it in list. Perform following operations on it  
a) Sort list in ascending order using sorted() function and display sorted list
b) sort list in descending order using sort() function
c) display length of list
11 Accept two lists from user and merge them using + in a single list
12 An acronym is a word formed by taking the first letters of the words in a phrase and making a word from them. For example, RAM is an acronym for “random access memory.” Write a program that allows the user to type in a phrase and then outputs the acronym for that phrase. Note: the acronym should be all uppercase, even if the words in the phrase are not capitalized.
13 Write a program to print the abbreviation of a month, given its number
14.Write a Python program to insert, delete, and display elements of a list.
15.Python program to merge two lists into a dictionary (one list as keys, another as values).
16.Python program to remove duplicate elements from a list.
17.Python program to convert two lists into a dictionary using zip().
18.Python program to find common elements in two lists.
"""

# 1
a = [10, 20, 30, 40, 50]
print(a)
print(a[0], a[1], a[2], a[3], a[4])

# 2
a = [1, 2, 3]
a.append(4)
print(a)

# 3
a = [1, 2, 3, 4, 5]
a.reverse()
print(a)

# 4
a = [1, 2, 2, 3, 2, 4]
print(a.count(2))

# 5
a = [1, 2]
b = [3, 4]
b = a + b
print(b)

# 6
a = [10, 30, 40]
a.insert(1, 20)
print(a)

# 7
a = [10, 20, 30, 40]
a.pop(2)
print(a)

# 8
a = [10, 20, 30, 20]
a.remove(20)
print(a)

```python
# 9
a = []
for i in range(20):
    a.append(int(input()))
# a
for x in set(a):
    print("v:", x, "c:", a.count(x))
    for i in range(20):
        if a[i] == x:
            print("i:", i)
# b
e = 0
o = 0
for x in a:
    if x % 2 == 0:
        e += 1
    else:
        o += 1
print("e:", e)
print("o:", o)
# c
p = 0
n = 0
for x in a:
    if x > 0:
        p += 1
    elif x < 0:
        n += 1
print("p:", p)
print("n:", n)

# 10
a = []
for i in range(10):
    a.append(int(input()))
# a
b = sorted(a)
print(b)
# b
a.sort(reverse=True)
print(a)
# c
print(len(a))

```python
# 11
a = input().split()
b = input().split()
c = a + b
print(c)

# 12
a = input()
b = ""
for w in a.split():
    b += w[0].upper()
print(b)

# 13
m = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
n = int(input())
print(m[n - 1])

# 14
a = [10, 20, 30]
a.insert(1, 15)
print(a)
a.pop(2)
print(a)

# 15
a = ["a", "b", "c"]
b = [1, 2, 3]
d = {}
for i in range(len(a)):
    d[a[i]] = b[i]
print(d)

# 16
a = [1, 2, 2, 3, 4, 4]
b = []
for x in a:
    if x not in b:
        b.append(x)
print(b)

# 17
a = ["a", "b", "c"]
b = [1, 2, 3]
d = dict(zip(a, b))
print(d)

# 18
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
c = []
for x in a:
    if x in b:
        c.append(x)
print(c)
