#FUNCTIONS

#PROGRAM----MULTIPLE ARGUMENT
'''
def multi_arg(name,p_name,batch,age):
    
    print(" My name is {}\n My father's name is {}\n I am in {} batch\n I am {} years old".format(name,p_name,batch,age))


x=input("enter name:")
y=input("enter father's name:")
z=input("enter batch name:")
a=int(input("enter age:"))

multi_arg(x,y,z,a)
'''

#PROGRAM-----POWER
'''
def power(x,y):

    print(x**y)

x=int(input("enter a f_number:"))
y=int(input("enter a s_number:"))
power(x,y)
'''

#PROGRAM----SORTING
'''
def sorting(x):
    for i in range(len(x)):
        for j in range(i+1):
            if(x[i]<x[j]):
                x[i],x[j]=x[j],x[i]
    print(x)
            
x=[]
y=int(input("enter a number:"))
for i in range(y):
    val=int(input("value:"))
    x.append(val)
print(x)
sorting(x)
'''

#PROGRAM----SUM
'''
def sum(x):
    count=0
    for i in x:
        count+=i
    print("sum:",count)
    
x=[]
y=int(input("enter a number:"))
for i in range(y):
    val=int(input("value:"))
    x.append(val)
print(x)
sum(x)
'''

#PROGRAM----REVERSE
'''
def reverse(x):
    print(x[::-1])
    
x=[]
y=int(input("enter a number:"))
for i in range(y):
    val=int(input("value:"))
    x.append(val)
print(x)
reverse(x)
'''

#PROGRAM----PALINDROME
'''
def palindrome(x):
    y=""
    for i in x:
        y=i+y
    if(x==y):
        print("palindrome")
    else:
        print("non palindrome")
    
    
x=input("Enter a string:")
palindrome(x)
'''

#PROGRAM----FACTORIAL
'''
def factorial(x):
    fact=1
    if(x<=0):
        print("garbage")
    else:
        for i in range(1,x+1):
            fact*=i
        print("factorial:",fact)

        
x=int(input("enter a number:"))
factorial(x)
'''



