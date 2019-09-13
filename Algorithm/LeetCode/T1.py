A=input()
A=A.split()
A = [int(A[i]) for i in range(len(A))]

xiaomi=[]
dami=[]

while True:


    xiaomi.append(max(A[0],A[-1]))
    if len(A) == 1:
        break
    A.remove(max(A[0], A[-1]))

    dami.append(max(A[0],A[-1]))
    if len(A) == 1:
        break
    A.remove(max(A[0], A[-1]))


if sum(xiaomi) >= sum(dami):
    print('Yes')
else:
    print('No')