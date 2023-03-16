#Driving License
'''
age=int(input("age:"))
if(age>=18 and age<60):
    print("you are eligible")
else:
    print("you are not eligible")

'''

#Vowel Check
'''
ch=input("Enter a alphabet:")
if(len(ch)==1):
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
        print("VOWEL")
    else:
        print("Consonent")
else:
    print("neither a consonent nor a vowel")

'''

#Sentence Check
'''
ch=input("Enter Anything:")
if(' ' in ch and '.' in ch):
    print("complete sentence")
elif(' ' in ch):
        print("incomplete Sentence")
elif(len(ch)==1):
    print("character")
else:
    print("word")
'''

#Word or Character Check
'''
ch=input("Enter Anything:")
if(len(ch)>1):
    print("word")
else:
    print("character")
    
'''

#Age Check
'''
ram=int(input("ram age:"))
shyam=int(input("shyam age:"))
mohan=int(input("mohan age:"))

if(ram>shyam):
    if(ram>mohan):
        print("ram")
    else:
        print("mohan")
else:
    if(shyam>mohan):
        print("shyam")
    else:
        print("mohan")
        
'''

#Calculator
'''
a=eval(input("Enter first number:"))
b=eval(input("Enter second number:"))
print(" 1 Addition\n 2 Substraction\n 3 Multiply\n 4 Division\n 5 Modullus\n 6 Exponential\n 7 Floor Division\n 8 Exit")
ch=int(input("Enter a number:"))
if(b==0 and ch==4):
    print("Infinite")
elif(ch==1):
    print("Sum:",a+b)
elif(ch==2):
    print("subtract:",a-b)
elif(ch==3):
    print("multiplication:",a*b)
elif(ch==4):
    print("division:",a/b)
elif(ch==5):
    print("mod:",a%b)
elif(ch==6):
    print("exponent:",a**b)
elif(ch==7):
    print("Floor value:",a//b)
elif(ch==8):
    print("Exit")
else:
    print("Invalid")
'''

#Marksheet
'''s
name=input("Enter a name:")
rollno=int(input("Enter Roll number:"))

eng_marks=int(input("Enter English Marks:"))
if(eng_marks>100 or eng_marks<0):
    print("invalid marks")
else:
    if(eng_marks>=31):
        print('')
    else:
        print("fail in english")

    
math_marks=int(input("Enter Maths Marks:"))
if(math_marks>100 or math_marks<0):
    print("invalid marks")
else:
    if(math_marks>=31):
        print('')
    else:
        print("fail in math")

        
phy_marks=int(input("Enter Physics Marks:"))
if(phy_marks>100 or phy_marks<0):
    print("invalid marks")
else:
    if(phy_marks>=31):
        print('')
    else:
        print("fail in physics")

        
chem_marks=int(input("Enter Chemistry Marks:"))
if(chem_marks>100 or chem_marks<0):
    print("invalid marks")
else:
    if(chem_marks>=31):
        print('')
    else:
        print("fail in chemistry")

        
hindi_marks=int(input("Enter Hindi Marks:"))
if(hindi_marks>100 or hindi_marks<0):
    print("invalid marks")
else:
    if(hindi_marks>=31):
        print('')
    else:
        print("fail in hindi")


if((eng_marks>100 or eng_marks<0) or (math_marks>100 or math_marks<0) or (phy_marks>100 or phy_marks<0) or (chem_marks>100 or chem_marks<0) or (hindi_marks>100 or hindi_marks<0)):
    print("invalid marks")

else:
    list=[eng_marks , math_marks , phy_marks , chem_marks , hindi_marks]
    count=0
    for i in range(0,len(list)):
        if(list[i]<33):
            count+=1
        
    if(count<=2 and count>0):
        if(eng_marks==31):
            eng_marks+=2
            print("English marks with grace:",eng_marks)
        elif(eng_marks==32):
            eng_marks+=1
            print("English marks with grace:",eng_marks)
            
        
        if(math_marks==31):
            math_marks+=2
            print("Math marks with grace:",math_marks)
        elif(math_marks==32):
            math_marks+=1
            print("Math marks with grace:",math_marks)

        
        if(phy_marks==31):
            phy_marks+=2
            print("Physics marks with grace:",phy_marks)
        elif(phy_marks==32):
            phy_marks+=1
            print("Physics marks with grace:",phy_marks)


        if(chem_marks==31):
            chem_marks+=2
            print("Chemistry marks with grace:",chem_marks)
        elif(chem_marks==32):
            chem_marks+=1
            print("Chemistry marks with grace:",chem_marks)

        
        if(hindi_marks==31):
            hindi_marks+=2
            print("Hindi marks with grace:",hindi_marks)
        elif(hindi_marks==32):
            hindi_marks+=1
            print("Hindi marks with grace:",hindi_marks)
   
        
    else:
        print(" ")
        
        
    Total_Marks= eng_marks + math_marks + phy_marks + chem_marks + hindi_marks
    Max_Marks=500
    per=(Total_Marks/Max_Marks)*100


    if((eng_marks<33) or (math_marks<33) or (phy_marks<33) or (chem_marks<33) or (hindi_marks<33)):
        print("overall fail")
        print("Total_Marks:", Total_Marks)
        print("Maximum_Marks:",Max_Marks)
        #print("Percentage:", per)
    
    
    else:
        if(Total_Marks>=0):
            print("Total_Marks:",Total_Marks)
            print("Maximum_Marks:",Max_Marks)
            print("Percentage:",per)
            print("Pass")
            if(per>90 and per<=100):
                print("Grade A+")
            elif(per>80 and per<=90):
                print("Grade A")
            elif(per>70 and per<=80):
                print("Grade B+")
             elif(per>60 and per<=70):
                print("Grade B")
            elif(per>50 and per<=60):
                print("Grade C+")
            elif(per>40 and per<=50):
                print("Grade C")
            else:
                print("Grade D")
        else:
            print("Check Marks Again")
'''

#Table
'''
table=int(input("Enter a number:"))
sum=0
for i in range(1,11):
    #sum=table*i
    #print(sum)
    print(f'{table} * {i} = {table*i}')
'''

#Factorial
'''
num=int(input("Enter a  number:"))
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)
'''

#Prime number
'''
num=int(input("Enter a number:"))
count=0
for i in range(2,num//2+1):
    if(num%i==0):
        count+=1
        break
if(count==0):
    print("Prime")
else:
    print("Not prime")
'''

#Prime number(1-100)
'''
num=int(input("Enter a number:"))
print("Prime number")

for i in range(1,num+1):
    count=0
    for j in range(2,i//2+1):
        if(i%j==0):
            count+=1
            break
    if(count==0):
       print(i)
'''   
    

#Sum of odd number
'''
num=int(input("Enter a number:"))
sum=0
for i in range(1,num+1):
    if(i%2!=0):
        sum+=i
print(sum)
'''

#Sum of even number
'''
num=int(input("Enter a number:"))
sum=0
for i in range(1,num+1):
    if(i%2==0):
        sum+=i
print(sum)
'''

#Sum of N-natural number
'''
num=int(input("Enter a number:"))
sum=0
for i in range(1,num+1):
    sum+=i
print(sum)
'''

#Natural number
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(i)
'''

#Even number
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    if(i%2==0):
        print(i)
'''

#list number
'''
list=[1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(list)):
    print(i)
'''

#count digits in a number
'''
num=input("Enter a number:")
digit=0
for i in num:
    digit+=1
print(digit)
'''

#Palindrome
'''
x=input("Enter anything:")
y=x[::-1]
if(x==y):
    print("Palindrome")
else:
    print("Not Palindrome")
'''

#Palindrome using For loop
'''
string=input("Enter a string:")
reverse_string=''
for i in string:
    reverse_string=i+reverse_string

if(string==reverse_string):
    print("Palindrome")
else:
    print("not palindrome")
'''

#Armstrong Number
'''
num=input("Enter a number:")
sum=0
val=int(num)
for i in num:
    a=int(i)
    prd=a*a*a
    sum+=prd

if(sum==val):
    print(f'{val} is a Armstrong Number')
else:
    print(f'{val} is not a Armstrong Number')
'''

#Count Even and Odd number
'''
num=int(input("Enter a number:"))
even_count=0
odd_count=0
for i in range(1,num+1,2):
    odd_count+=1
print(f'odd numbers are: {odd_count}')
for j in range(2,num+1,2):
    even_count+=1
print(f'even_numbers are: {even_count}')
'''

#Convert month name into Number of days in a month
'''
month=input("Enter a month name:")
days=31
Days=30
DAYS=28
DDays=29
if(month=="january" or month=="march" or month=="may" or month=="july" or month=="august" or month=="october" or month=="december"):
            print(f'Days in month is : {days}')
elif(month=="april" or month=="june" or month=="september" or month=="november"):
    print(f'Days in month is: {Days}')
elif(month=="february"):
    x=int(input("Enter year:"))
    if(x%100==0 and x%400!=0):
        print(f'Days in month is: {DAYS}')
    else:
        print(f'Days in month is: {DDays}')
else:
    print("invalid month name")
'''
#Number except prime number in a range
'''
num=int(input("Enter a number:"))
for i in range(1,num+1):
    for j in range(2,i//2+1):
        if(i%j==0):
            print(i)
            break
'''

#Fibonacci Series
'''
a=0
b=1
print(a,b,end=" ")
for i in range(10):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
'''

       
    
   






