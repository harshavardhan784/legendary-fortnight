from xmlrpc.client import MAXINT


w=int(input("Coin(x):"))
n=int(input("Enter the no of denominations:"))
V=[]
W=[]
print("Denomination Array-")
for i in range(n):
    W.append(int(input()))
i,j=(n+1,w+1)
arr=[[int(0)]*j]*i
for i in range(n+1):
    for j in range(w+1):
        if(j==0 ):
            arr[i][j]=0
        if(i==0):
            arr[i][j]=MAXINT
for j in range(w+1):
    if(j%W[0]==0):
        arr[i][j]=j/W[0]
    else:
        arr[1][j]=MAXINT
for i in range(n+1):
    for j in range(w+1):
        if(W[i-1]<=j):
            arr[i][j]=min((1+arr[i-1][j-W[i-1]]),arr[i-1][j])
        elif(W[i-1]>j):
            arr[i][j]=arr[i-1][j]
if(arr[n][w]<MAXINT):
    print("The minimum no of coins required:",arr[n][w])
else:
    print("Change cannot be given")