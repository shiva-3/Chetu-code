#OOPs

#NOTE:- class : contain attributes and behaviour
#NOTE:- class accessed by object
#NOTE:- 'Attributes'=='Variables'
#NOTE:- 'Behaviour'=='Methods'

#Program
'''
class chetu:
    def start(self,name,address,cl):
        self.name=name
        self.add=address
        self.cl=cl

    def display(self):
        print(f' My name is {self.name} lived in {self.add} and {self.cl} remain')

t1=chetu()
t2=chetu()

t1.start("abhishek","noida",8)
t2.start("nirdesh","delhi",2)

t1.display()
t2.display()
'''

#Program
'''
class chetu:
    def add(self):
        self.a=134
        self.b=98
        print(self.a+self.b)

    def sub(self):
        print(self.a-self.b)

obj=chetu()
obj.add()
obj.sub()
'''

#Program
'''
class chetu:
    cl=10
t1=chetu()
print(dir(t1))
'''

#Program
'''
class chetu:
    cl=10
    def test(self):
        pass
t1=chetu()
t2=chetu()
t1.name="abhishek"
t1.cl=7
print(t1.__dict__)
chetu.cl=2
print(chetu.cl)
'''

#Program
'''
class match:
    def run(self):
        print("run")
ram=match()
mohan=match()
sohan=match()

match.run(ram)
mohan.run()
'''

#Program
'''
class function:
    def add(self):
        a=12
        b=2
        print(a+b)
        print(a-b)
        print(a*b)
        print(a/b)
obj=function()
obj.add()
'''

#Contructor
'''
class chetu:
    def __init__(self,name,address,age):
        self.name=name
        self.address=address
        self.age=age

    def printdata(self):
        print(self.name,self.address,self.age)

shivansh=chetu("Shivansh","Noida",21)
shivansh.printdata()
'''
#Note:- Python doesn't support method overloading by default due to interpreter.

#Manual Method Overloading
'''
class A:
    def student(self,name,age):
        print("first")

    def student(self,name,age,roll):
        print("second")

obj=A()
obj.student("shivansh",21) #o/p: A.student() missing 1 required positional argument: 'roll'
obj.student("shivansh",21,18) #o/p: second
'''

#Decorator
'''
from multipledispatch import dispatch

class A:
    
    @dispatch(int)
    def __init__(self,value):
        print("int:",value)
        
    @dispatch(str)
    def __init__(self,value):
        print("string:",value)

    @dispatch(int,int)
    def student(self,age,roll):
        print("first")

    @dispatch(str,str)
    def student(self,name,address):
        print("second")

obj=A(4)
obj.student("shivansh","Noida")
obj.student(21,18)
'''

#Attributes

#1.Instance Variable
'''
class test:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    

t1=test("shivansh",21,"noida")
t2=test("nirdesh",21,"delhi")
print(t1.name) #o/p: shivansh
print(t2.name) #o/p: nirdesh
'''

#2.Class Variable
'''
class test:
    cl=10
    def __init__(self):
        self.name="rohit"
        self.age=21
        self.address="lucknow"

t1=test()
t2=test()
t2.cl=7
test.cl=20
print(t1.cl) #o/p: 20
print(t2.cl) #o/p: 7
print(dir(t1))
'''

#Methods

#1.Instance Method
'''
class chetu:
    def __init__(self,name,address,cl):
        self.name=name
        self.address=address
        self.cl=cl

    def set(self,value): #set
        self.cl=value

    def get(self): #get
        return self.cl

    def display(self):
        print(f'{self.name}\n{self.address}\n{self.cl}')

t1=chetu("shivansh","noida",5)
t1.set(7)
t1.display()
print(t1.get())
'''

#2.Class Method
'''
class chetu:
    session="python"
    
    @classmethod
    def change(cls,value):
        cls.session=value

obj=chetu()
obj.change("java")
print(obj.session) #with/without classmethod- "java"
print(chetu.session) #with classmethod- "java" and without classmethod- "python"
'''

#3.Static Method
'''
class chetu:

    @staticmethod
    def independent():
        print("independent work")

obj=chetu()
obj.independent()
chetu.independent()
'''

#Example of OOPs(Calculator)
'''
class calculator:

    def add(self,a,b):
        self.a=a
        self.b=b
        print("Addition:",self.a+self.b)

    def subtract(self,a,b):
        self.a=a
        self.b=b
        print("Subtraction:",self.a-self.b)

    def multiply(self,a,b):
        self.a=a
        self.b=b
        print("Multiplication:",self.a*self.b)

    def divide(self,a,b):
        self.a=a
        self.b=b
        print("Division:",self.a/self.b)

obj=calculator()
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
a=int(input("number1:"))
b=int(input("number2:"))
val=int(input("choose from above:"))


if(val==1):
    obj.add(a,b)
elif(val==2):
    obj.subtract(a,b)
elif(val==3):
    obj.multiply(a,b)
elif(val==4):
    obj.divide(a,b)
elif(val==5):
    exit()
else:
    print("choose from above")
'''

#INHERITANCE

#Types of Inheritance

#1.Single Inheritance
'''
class parents:
    def f1(self):
        print("parents")

class child(parents):
    def f2(self):
        print("child")

obj=child()
print(dir(obj))
obj.f1() #Parents
'''

#2.Multilevel Inheritance
'''
class A:   #Parents
    def f1(self):
        print("A")


class B(A):  #Intermediate
    def f2(self):
        print("B")

class C(B):  #Child
    def f3(self):
        print("C")

obj=C()
obj.f1()
obj.f2()

obj2=B()
obj2.f1()
'''

#3.Multiple Inheritance
'''
class A:
    def f1(self):
        print("A")

class B:
    def f1(self):
        print("B")

class C(B,A):
    pass

obj=C()
obj.f1()
'''

#4.Hybrid Inheritance
'''
class A:
    def f1(self):
        print("A")

class B(A):
    def f2(self):
        print("B")

class C(A):
    def f3(self):
        print("C")

class D(B,C):
    def f4(self):
        print("D")

obj=D()
obj.f1()
'''

#Example
'''
class A:
    def f1(self):
        print("A")

class B(A):
    def f1(self):
        print("B")

class C(B):
    def f1(self):
        A.f1(self)

obj=C()
obj.f1()
'''


#Example
'''
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("A")

class B(A):
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        print(self.a+self.b)

obj=B(6,6)
obj.add()
'''

#Example
'''
class A:
    def __init__(self):
        self.a=34

    def view(self):
        print(self.a)

    def __del__(self):
        print("Destructor Calling")

obj=A()
obj.view()
del obj
obj.view() #Not possible after run destructor
'''

#Example
'''
class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def view(self):
        print(f'Name {self.name}\nAge {self.age}')

class B(A):
    def __init__(self,name,age,location):
        super().__init__(name,age)
        self.location=location

obj=B("Priyanka",34,"Noida")
obj.view()
'''

#Program OOPs

class Bike:

    def __init__(self):
        self.bike_menu()

    def buy_bike(self):
        self.bike_name="Kawasaki Ninja H2"
        self.price="20Lakhs"
        self.available=15
        print(f'Bike name:-{self.bike_name}\nBike price:-{self.price}\nBikes available:-{self.available}')
        
        x=input("If you want to buy a bike, type yes:")
        if(x.lower()=="yes"):
            y=int(input("How many bikes you wanna buy:"))
            if(y<=self.available):
                Total_price=y*2000000
                print("Payment:",Total_price)
                print("CONGRATULATIONS SIR...ENJOY YOUR DAY!!")
                print("\t\tThanks to visit our website...keep visiting!!!")

            else:
                print("Out Of Stock")
                print("\t\tThanks to visit our website...keep visiting!!!")
                

        else:
            print("\t\tThanks to visit our website...keep visiting!!!")

    def rent_bike(self):
        self.bike_name="Kawasaki Ninja H2"
        self.price="10000/hr."
        self.available=10
        print(f'Bike name:-{self.bike_name}\nBike price:-{self.price}\nBikes available:-{self.available}')
        
        x=input("If you want to rent a bike, type yes:")
        if(x.lower()=="yes"):
            y=int(input("How many bikes you wanna rent:"))
            if(y<=self.available):
                z=int(input("For how many hours you wanna rent:"))
                Total_price=y*10000*z
                print("Payment:",Total_price)
                print("CONGRATULATIONS SIR...ENJOY YOUR DAY!!")
                print("\t\tThanks to visit our website...keep visiting!!!")

            else:
                print("Out Of Stock")
                print("\t\tThanks to visit our website...keep visiting!!!")
                
        else:
            print("\t\tThanks to visit our website...keep visiting!!!")


    def bike_menu(self):
        print(f"Do you have to buy or rent a bike\n1.Buy a Bike\n2.Rent a Bike\n3.Exit")
        val=int(input("Make a choice:"))
        if(val==1):
            self.buy_bike()

        elif(val==2):
            self.rent_bike()

        elif(val==3):
            exit()

        else:
            print("choose from above")


class Car:

    def __init__(self):
        self.car_menu()

    def buy_car(self):
        self.car_name="BMW X4"
        self.price="80Lakhs"
        self.available=15
        print(f'Car name:-{self.car_name}\nCar price:-{self.price}\nCars available:-{self.available}')
        
        x=input("If you want to buy a car, type yes:")
        if(x.lower()=="yes"):
            y=int(input("How many cars you wanna buy:"))
            if(y<=self.available):
                Total_price=y*8000000
                print("Payment:",Total_price)
                print("CONGRATULATIONS SIR...ENJOY YOUR DAY!!")
                print("\t\tThanks to visit our website...keep visiting!!!")

            else:
                print("Out Of Stock")
                print("\t\tThanks to visit our website...keep visiting!!!")
                

        else:
            print("\t\tThanks to visit our website...keep visiting!!!")

    def rent_car(self):
        self.car_name="BMW X4"
        self.price="20000/hr."
        self.available=25
        print(f'Car name:-{self.car_name}\nCar price:-{self.price}\nCars available:-{self.available}')
        
        x=input("If you want to rent a car, type yes:")
        if(x.lower()=="yes"):
            y=int(input("How many cars you wanna rent:"))
            if(y<=self.available):
                z=int(input("For how many hours you wanna rent:"))
                Total_price=y*20000*z
                print("Payment:",Total_price)
                print("CONGRATULATIONS SIR...ENJOY YOUR DAY!!")
                print("\t\tThanks to visit our website...keep visiting!!!")

            else:
                print("Out Of Stock")
                print("\t\tThanks to visit our website...keep visiting!!!")
                
        else:
            print("\t\tThanks to visit our website...keep visiting!!!")


    def car_menu(self):
        print(f"Do you have to buy or rent a car\n1.Buy a Car\n2.Rent a Car\n3.Exit")
        val=int(input("Make a choice:"))
        if(val==1):
            self.buy_car()

        elif(val==2):
            self.rent_car()

        elif(val==3):
            exit()

        else:
            print("choose from above")


class Vehicle(Car,Bike):
    def __init__(self):
        print("\t\tWELCOME TO OUR WEBSITE...")
        self.menu()

    def menu(self):
        print(f"What you wanna have a car or a bike\n1.Car\n2.Bike\n3.Exit")
        val=int(input("Make a choice:"))
        if(val==1):
            self.car_menu()

        elif(val==2):
            self.bike_menu()

        elif(val==3):
            exit()

        else:
            print("Choose from above")

        
            
        
            
        
        


