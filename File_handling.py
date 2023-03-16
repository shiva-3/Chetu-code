#FILE HANDLING

#FUNCTION
'''
1.tell()---it tells the location/position of the cursor i.e. the length of message
2.seek()---it moves the cursor to the given location/position entered manually such that 0 or 1 or 2 
'''

#MODES
'''
1. 'r'----READ
2. 'w'----WRITE
3. 'a'----APPEND
4. 'x'----EXCLUSIVE
'''

#ADVANCE MODES
'''
1. 'r+'----READ+APPEND
2. 'a+'----APPEND+READ
3. 'w+'----WRITE+READ
4. 'x+'----EXCLUSIVE+READ
'''

#1. 'w'---write
'''
f=open('demofile.txt','w')
msg=input("enter a message:")
f.write(msg)
f.close()
'''
#2. 'a'---append
'''
f=open('demofile.txt','a')
msg=input('enter a msg:')
f.write(msg)
f.close()
'''

#3. 'x'---exclusive
'''
f=open('demo.txt','x')
msg=input()
f.write(msg)
f.close()
'''

#4. 'r'---read
'''
f=open('demofile.txt','r')
print(f.read())
f.close()
         #or
f=open('demofile.txt','r')
print(f.readline(5))
f.close()
        #or
f=open('demofile.txt','rb')
print(f.readline(5))
f.close()
'''

#5. 'w+'---write+read
'''
f=open("demofile.txt",'w+')
msg=input()
f.write(msg)
print(f.tell())
f.seek(0)
print(f.read())
f.close()
'''

#6. 'a+'---append+read
'''
f=open('demofile.txt','a+')
msg=input('msg:')
f.write(msg)
f.seek(f.tell()-len(msg))
print(f.read())
f.close()
          #or
f=open('test.txt','a+')
store=f.tell()
f.write('kamlesh')
f.seek(0)
print(f.read(store))
f.close()
'''

#7. 'x+'---exclusive+read
'''
f=open('aabc.txt','x+')
msg=input()
f.write(msg)
f.seek(0)
print(f.read())
f.close()
'''

#8. 'r+'---read+append
'''
f=open('demofile.txt','r+')
print(f.read())
msg=input()
f.write(msg)
f.close()
'''
