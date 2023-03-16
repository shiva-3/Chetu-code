#LIST[]

'''
#1.View

x=[1,2,3,4.4,32,56]

print(type(x))
print(x[4])
print(x.index(56))
print(list(enumerate(x)))

y=[1,2,3,45,67,43,[87,344,6775,766,23,[99,96,43,42],67,87,34],56,999]
print(y[-3][-4][-3])


#slicing in list

x=[1,2,3,4.4,32,56,65,89,43,78,54,90]

print(x[3:-2])

print(x[2:])

print(x[:2])

print(x[-2:])

print(x[:-2])

print(x[-8:-3])

print(x[2:-2])

print(x[-8:3])

'''

#list(view,insert,delete,replace)
'''
x=[]
y=int(input("how many value:"))
for i in range(y):
    val=int(input("value:"))
    x.append(val)
print(x)

print("list",x)

print("sum:",sum(x))

print("max:",max(x))

print("min:",min(x))

x.sort()
print(x)

x.reverse()
print(x)

copy_x=x.copy()
print("copylist:",copy_x)

print(x.count(34))

print(len(x))

x.append(35)
print(x)

x.append([1,2,3])
print(x)

x.extend([1,2,3])
print(x)

x.insert(2,45)
print(x)

x[2]=54
print(x)

x.pop()
print(x)

x.pop(3)
print(x)

x.remove(34)
print(x)

x.clear()
print(x)

del x
print(x)

print(copy_x)

print(x.index(34))
'''

#Program to Add integer value in list
'''
x=[]
a=int(input("how many value:"))
for i in range(a):
    val=eval(input("value:"))
    x.append(val)
print(x)

count=0
for j in x:
    if(type(j)==int or type(j)==float):
        count+=j
print(count)
'''
#Program to count element(datatype) in list
'''
x=[]
a=int(input("how many value:"))
for i in range(a):
    val=eval(input("value:"))
    x.append(val)
print(x)

str_c=0
complex_c=0
bool_c=0
float_c=0
int_c=0

for j in x:
    if(type(j)==int):
        int_c+=1
    elif(type(j)==str):
        str_c+=1
    elif(type(j)==complex):
        complex_c+=1
    elif(type(j)==float):
        float_c+=1
    else:
        bool_c+=1

print(f' Integer {int_c}\n String {str_c}\n Complex {complex_c}\n Float {float_c}\n Boolean {bool_c}')
'''    
        
#Program t0 add element of list and add it into a new list
'''
a=[]
b=[]
c=[]

x=int(input("how many value:"))
for i in range(x):
    val=int(input("Value:"))
    a.append(val)
print(a)

y=int(input("how many vale:"))
for i in range(y):
    val=int(input("value:"))
    b.append(val)
print(b)

if(len(a)>len(b)):
    for i in range(len(b)):
        x=a[i]+b[i]
        c.append(x)
    print(c)
else:
    for i in range(len(a)):
        x=a[i]+b[i]
        c.append(x)
    print(c)
'''

#List Comprehension

#Program to display natural no.
'''
num=[x for x in range(1,51)]
print(num)
'''

#Program to display even-odd number
'''
num=[x for x in range(1,51) if x%2==0]
print(num)

num=[x for x in range(1,51) if x%2!=0]
print(num)
'''

#Program to display sum of even-odd number
'''
num=[x for x in range(1,51,2)]
print(sum(num))

num=[x for x in range(2,51,2)]
print(sum(num))
'''

# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
'''
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)
'''

#Write a Python program to generate a 3*4*6 3D array whose each element is *

#Write a Python program to print the numbers of a specified list after removing even numbers from it.
'''
c=[22,44,7,56,16,78]
c=[x for x in c if x%2!=0]
print(c)
'''

#Write a Python program to shuffle and print a specified list
'''
import random
x=[1,2,3,4,5,6]
random.shuffle(x)
print(x)
'''

