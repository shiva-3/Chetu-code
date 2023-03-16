#DICTIONARY{:} --- KEY-VALUE PAIRS

#1.VIEW
std={'name':'shivansh','batch':'python','class':'b.tech','age':21}

print(std['name'])

print(std['class'])

for i in std:
    print(i)

for i in std:
    print(i, std[i])

#2.INSERT --- UPDATE()
    
std={'name':'shivansh','batch':'python','class':'b.tech','age':21}

std['mobile']=7068722000
print(std)

std.update({'organization':'chetu'})
print(std)

std['mobile']=1234567890

std.update({'organization':'Chetu'})

print(std)

#3.DELETE --- POP(),POPITEM(),CLEAR(),DEL

std={'name': 'shivansh', 'batch': 'python', 'class': 'b.tech', 'age': 21, 'mobile': 1234567890, 'organization': 'Chetu'}

std.pop('name')
print(std)

std.popitem()
print(std)

std.clear()
print(std)

#del std
#print(std)

#4.IN-BUILT FUNCTIONS ---- LEN(),MAX(),MIN()

std={'name': 'shivansh', 'batch': 'python', 'class': 'b.tech', 'age': 21, 'mobile': 1234567890, 'organization': 'Chetu'}

print(len(std))

print(max(std))

print(min(std))

#Program

mydict={}
for i in range(11):
    mydict[i]=i**2
print(mydict)
print(mydict.keys())
print(mydict.items())


#Program

mydict={}
for i in range(11):
    mydict[i]=i**2
save=mydict.items()
save=list(mydict.items())
print(save)

#Program

std={'name': 'shivansh', 'batch': 'python', 'class': 'b.tech', 'age': 21, 'mobile': 1234567890, 'organization': 'Chetu'}
save=list(mydict.keys())
print(mydict[save[0]])

#Program

std={'name': 'shivansh', 'batch': 'python', 'class': 'b.tech', 'age': 21, 'mobile': 1234567890, 'organization': 'Chetu'}
new={}

key=list(mydict.keys())
value=list(mydict.values())

for x,y in zip(key,value):
    new[x]=y
print(new)

#Program

x={}
for i in range(4):
    key=eval(input("Enter key:"))
    value=eval(input("Enter value:"))
    x[key]=value
print(x)

#Program
x={'a':'apple','b':'ball'}
print(x.get('a'))
