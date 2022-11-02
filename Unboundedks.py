w=int(input("Enter the capacity of bag:"))
n=int(input("Enter the no of weights:"))
V=[]
W=[]
print("Weight array-")
for i in range(n):
    W.append(int(input()))
print("Value array-")
for i in range(n):
    V.append(int(input()))
i,j=(n+1,w+1)
arr=[[int(0)]*j]*i
for i in range(n+1):
    for j in range(w+1):  
        if(j==0 or i==0):
            arr[i][j]=0
for i in range(n+1):
    for j in range(w+1):
        if(W[i-1]<=j):
            arr[i][j]=max((V[i-1]+arr[i][j-W[i-1]]),arr[i-1][j])
        elif(W[i-1]>j):
            arr[i][j]=arr[i-1][j]
print("The maximum profit is:",arr[n][w])