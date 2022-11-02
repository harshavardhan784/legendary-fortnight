def knapsack(W,w,n):
    if( w==0):
        return 1
    if(w<0):
        return 0
    if(n<=0):
        return 0
    return(knapsack(W,w-W[n-1],n)+knapsack(W,w,n-1))
    # elif(W[n-1]>w):
    #     return(knapsack(W,w,n-1))

w=int(input("Coin:"))
n=int(input("No of denominations:"))
W=[]
print("Denominations array-")
for i in range(n):
    W.append(int(input()))
i,j=(n+1,w+1)
t=[[int(-1)]*j]*i
print("change:",knapsack(W,w,n))