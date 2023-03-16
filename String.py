#STRING
'''
#1.VIEW
x="shivansh"
print(x[2])

print(x.index("v"))

print(type(x))

#4.UPDATE
x="your next test is on monday"
print(x.replace("monday","today"))


#Program

x=input("Enter string:").split()
for i in x:
    print(i.capitalize(),end=" ")
    
#Program

x="hello how are you"
for i in range(len(x)):
    if(i%2==0):
        print(x[i].upper(),end="")
    else:
        print(x[i].lower(),end="")


#Program

a="shivansh sharma jha"
b=a.split()
for i in b:
    for x in range(len(i)):
        if(x==0  or x==len(i)-1 ):
            print(i[x].upper())
        else:
            print(i[x].lower())  

#Program

x="shivansh"
c=""
for i in x:
    if i not in c:
        c+=i
print(c)


#Program

x=input()
y=input()
unique=""
duplicate=""
count=0
for i in x:
    if i not in unique:
        unique+=i
    elif i not in duplicate:
        if i in y:
            duplicate+=i
            count+=1
for j in y:
    if j not in unique:
        unique+=j
    elif j not in duplicate:
        if j in y:
            duplicate+=j
            count+=1
print("count:",count)

            #or

x=input()
y=input()
count=0

if(len(x)>len(y)):
    for i in y:
        if i in x:
            count+=1

if(len(y)>len(x)):
    for i in x:
        if i in y:
            count+=1
print(count)
'''





          
    
