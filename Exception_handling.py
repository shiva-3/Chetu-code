#EXCEPTION HANDLING

#Program-----Zero Division Error
'''
x=int(input("number 1:"))
y=int(input("number 2:"))

try:
    print(x/y)

except ZeroDivisionError:
    print("zero division error occur")

print(x+y)
'''

#Program-----Multiple Error Catching
'''
try:
    x=int(input("number 1:"))
    y=int(input("number 2:"))
    print(x/y)

except ZeroDivisionError:
    print("zero division error occur")

except KeyboardInterrupt:
    print("cancel by user")

except ValueError:
    print("non int value given")

except:
    print("something wrong")

else:
    print(x+y)
'''

#Program----Negative Error
'''
class NegativeError(Exception):
    pass

try:
    num=int(input("Enter a number:"))
    if(num<0):
        raise NegativeError
    else:
        print(num,"positive number")

except NegativeError:
    print("negative number given")

except ValueError:
    print("non int value given")

except:
    print("something wrong")
'''

#Program-----RangeError
'''
class RangeError(Exception):
    pass

try:
    num=int(input("enter a number:"))
    if(num>7):
        raise RangeError
    else:
        a=0
        b=1
        print(a,b,end=" ")
        for i in range(num):
            c=a+b
            print(c,end=" ")
            a=b
            b=c

except RangeError:
    print("out of range ")
'''

#Program-----password
'''
from getpass import getpass

class pass_len(Exception):
    pass

try:
    user=getpass("enter your password")
    if(len(user)<=7):
        raise pass_len
    else:
        print(user)

except pass_len:
    print("password length less than 8 digit")
'''

#Program-----outofrange
'''
class outofrange(Exception):
    pass

try:
    num=int(input("enter a number:"))
    if(num>10):
        raise outofrange
    else:
        for i in range(num):
            print(i,end=" ")

except outofrange:
    print("out of range number given")
'''

