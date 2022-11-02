def knapsack(W,V,w,n):
    if(n==0 or w==0):
        return 0
    if(W[n-1]<=w):
        return(max((V[n-1]+knapsack(W,V,w-W[n-1],n-1)),knapsack(W,V,w,n-1)))
    elif(W[n-1]>w):
        return(knapsack(W,V,w,n-1))

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
t=[[int(-1)]*j]*i
print("The maximum profit or value is:",knapsack(W,V,w,n))