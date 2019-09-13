A=input()
print(type(A))

length=len(A)

if length <= 2:
    print( False)
if length>=3:
    print(True) if A == A[:: -1] else print( False)




