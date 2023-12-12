#list
L=[10,40,30,20]
print(L)
L.sort() #mutable
print(L)
print(type(L))
print(L[0],L[1],L[-1])
L.append(30)
print(L)
L[0]=999 #mutable
print(L)
L.remove(30)
print(L)
print(L[1:3]) #slice
