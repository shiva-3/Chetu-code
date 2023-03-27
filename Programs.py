#Program---To Count data type in list
'''
x=[1,2,True,8j,9.8,"sid"]
s=0
c=0
f=0
b=0
i=0

for z in x:
    if(type(z)==int):
        i+=1
    elif(type(z)==str):
        s+=1
    elif(type(z)==bool):
        b+=1
    elif(type(z)==complex):
        c+=1
    else:
        f+=1
print(f'string:{s}\nComplex:{c}\nFloat:{f}\ninteger:{i}\nboolean:{b}')
'''

#Program-----To Sum non prime number
'''
user=1
sum=0
while(user<=100):
    count=0
    loop=2
    while(loop<=user//2):
        if(user%loop==0):
            count+=1
            break
        loop+=1
    if(count==1):
        sum+=user
    user+=1
print(sum)
'''

#Program----To print non armstrong numbers 100-500
'''
prod=0
for i in range(100,200):
    x=str(i)
    y=i
    for j in x:
        prod=(int(j)*int(j)*int(j))+prod
    if(y!=prod):
        print(y,end=",")
'''

#Write a program to reverse an integer in Python.
'''
x=input("enter a value in int:")
num=""
for i in x:
    num=i+num
print(int(num))
'''

#Write a program in Python to check whether an integer is Armstrong number or not.
'''
x=input("enter a integer value:")
z=int(x)
y=0

for i in x:
    y+=int(i)**3

if(y==z):
    print("armstrong number")
else:
    print("not a armstrong number")
'''

#Write a program in Python to check given number is prime or not.
'''
x=int(input("enter a number:"))
count=0
for i in range(2,x//2+1):
    if(x%i==0):
        count+=1
        break
if(count==0):
    print("prime")
else:
    print("non prime")
'''
            #OR
'''
x=int(input("enter a number:"))
count=0
loop=2
while(loop<=x//2):
    if(x%loop==0):
        count+=1
        break
    loop+=1
if(count==0):
    print("prime")
else:
    print("non prime")
'''    

#Write a program in Python to print the Fibonacci series using iterative method.
'''
x=int(input("enter a value:"))
a=0
b=1
print(a,b,end=" ")
for i in range(x):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
'''
        #OR
'''
x=int(input("enter a value:"))
a=0
b=1
print(a,b,end=" ")
loop=1
while(loop<=x):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    loop+=1
'''

#Write a program in Python to print the Fibonacci series using recursive method.
'''
def fibonacci():
    x=int(input("enter a value:"))
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(x):
        c=a+b
        print(c,end=" ")
        a=b
        b=c

fibonacci()
'''

#Write a program in Python to check whether a number is palindrome or not using iterative method.
'''
x=input("enter a string:")
new=""
for i in x:
    new=i+new
if(x==new):
    print("palindrome")
else:
    print("non palindrome")
'''

#Write a program in Python to check whether a number is palindrome or not using recursive method.
'''
def palindrome():
    x=input("enter a string:")
    new=""
    for i in x:
        new=i+new
    if(new==x):
        print("palindrome")
    else:
        print("non palindrome")
        
palindrome()
'''

#Write a program in Python to find greatest among three integers.
'''
x=int(input("enter first number:"))
y=int(input("enter second number:"))
z=int(input("enter third number:"))

if(x>y):
    if(x>z):
        print(x,"is greatest")
    else:
        print(z,"is greatest")
else:
    if(y>z):
        print(y,"is greatest")
    else:
        print(z,"is greatest")
'''

#Write a program in Python to find sum of digits of a number using recursion?
'''
def Sum():
    x=input("enter a number:")
    y=0
    for i in x:
        y+=int(i)
    print(y)

Sum()
'''

#Write a program in Python to swap two numbers without using third variable?
'''
x=int(input("enter first number:"))
y=int(input("enter second number:"))
x,y=y,x
print(x,y)
'''
        #OR
'''
x=int(input("enter first number:"))
y=int(input("enter second number:"))
x=x+y
y=x-y
x=x-y
print(x,y)
'''

#Write a program in Python to swap two numbers using third variable?
'''
x=int(input("enter first number:"))
y=int(input("enter second number:"))

z=x
x=y
y=z
print(x,y)
'''

#Write a program in Python to find given number is perfect or not?
'''
x=int(input("enter a number:"))
y=0
for i in range(1,x//2+1):
    if(x%i==0):
        y+=i
if(x==y):
    print("perfect number")
else:
    print("not perfect number")
'''

#Python Program to find the Average of numbers with explanations.
'''
x=int(input("how many elements:"))
y=[]
for i in range(x):
    val=int(input("value:"))
    y.append(val)

z=sum(y)
zz=len(y)
avg=z/zz
print(avg)
'''

#Python Program to calculate factorial using iterative method.
'''
x=int(input("enter a number:"))
fact=1
for i in range(1,x+1):
    fact*=i
print(fact)
'''

#Python Program to calculate factorial using recursion.
'''
def factorial():
    x=int(input("enter a number:"))
    fact=1
    for i in range(1,x+1):
        fact*=i
    print(fact)

factorial()
'''

#Python Program to check a given number is even or odd.
'''
x=int(input("enter a number:"))
if(x%2==0):
    print("even number")
else:
    print("odd number")
'''

#Python program to print first n Prime Number with explanation.
'''
n=int(input("enter a number:"))
for i in range(1,n+1):
    count=0
    for j in range(2,i//2+1):
        if(i%j==0):
            count+=1
            break
    if(count==0):
        print(i)
'''

            #OR
'''
n=int(input("enter a number:"))
loop1=1
while(loop1<=n):
    count=0
    loop2=2
    while(loop2<=loop1//2):
        if(loop1%loop2==0):
            count+=1
            break
        loop2+=1
    if(count==0):
        print(loop1)
    loop1+=1
'''

#Python Program to print Prime Number in a given range.
'''
start=int(input("enter a number to start range:"))
stop=int(input("enter a number to stop range:"))
for i in range(start,stop+1):
    count=0
    for j in range(2,i//2+1):
        if(i%j==0):
            count+=1
            break
    if(count==0):
        print(i)
'''

        #OR

'''
loop1=int(input("enter a number:"))
n=int(input("enter a number:"))
while(loop1<=n):
    count=0
    loop2=2
    while(loop2<=loop1//2):
        if(loop1%loop2==0):
            count+=1
            break
        loop2+=1
    if(count==0):
        print(loop1)
    loop1+=1
'''

#Python Program to find Smallest number among three.
'''
x=int(input("enter first number:"))
y=int(input("enter second number:"))
z=int(input("enter third number:"))

if(x<y):
    if(x<z):
        print(x,"is smallest")
    else:
        print(z,"is smallest")
else:
    if(y<z):
        print(y,"is smallest")
    else:
        print(z,"is smallest")
'''

#Python program to calculate the power using the POW method.
'''
from math import pow

x=int(input("enter a number:"))
y=int(input("enter a power number:"))
print(pow(x,y))
'''

#Python Program to calculate the power without using POW function.(using for loop).
'''
x=int(input("enter a number:"))
y=int(input("enter a power number:"))
print(x**y)
'''

