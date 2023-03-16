#SET{}

x={}
print(type(x))

x=set()
print(type(x))

#1.VIEW ---- NOT SUPPORTED

#2.INSERT ---- ADD(),UPDATE()

x={1,2,3,4,5,6}
print(x)

x.add(34)
print(x)

x.add(45)
print(x)

x.update([11,22,33])
print(x)

#3.DELETE ----POP(),REMOVE(),DISCARD(),CLEAR(),DEL

x={1,2,3,4,5,6}

x.pop()
print(x)

x.remove(3)
print(x)

x.discard(2)
print(x)

x.clear()
print(x)

del x
print(x)

#4.REPLACE ---- NOT SUPPORTED

#5.IN-BUILT FUNCTIONS ---SUM(),MAX(),MIN(),SORTED(),LEN(),UNION(A|B),INTERSECTION(A&B),DIFFERENCE(A-B),SYMMTERIC_DIFFERENCE(A^B)

x={1,2,3,4,5}

print(sum(x))

print(max(x))

print(min(x))

print(len(x))

print(sorted(x))

x={1,2,3,4,5}
y={4,5,9,8,7}

print(x.union(y),x|y)

print(x.intersection(y),x&y)

print(x.difference(y),x-y)

print(x.symmetric_difference(y),x^y)
