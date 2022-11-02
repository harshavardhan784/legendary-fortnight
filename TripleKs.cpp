#include <bits/stdc++.h>
#define maxN 31
#define maxW 31
using namespace std;
int dp[maxN][maxW][maxW][maxW];
int MaxCount(int* arr, int n, int w1_r, int w2_r, int w3_r ,int i)
{
    if (i == n)
        return 0;
    if (dp[i][w1_r][w2_r][w3_r] != -1)
    return 0;
    int fill_w1 = 0, fill_w2 = 0, fill_w3 =0 ,fill_none = 0;
 
    if (w1_r >= arr[i])
        fill_w1 = arr[i] +MaxCount(arr, n, w1_r - arr[i], w2_r, w3_r , i + 1);
 
    if (w2_r >= arr[i])
        fill_w2 = arr[i] +MaxCount(arr, n, w1_r, w2_r - arr[i], w3_r, i + 1);
    
    if (w3_r >= arr[i])
        fill_w3 = arr[i] +MaxCount(arr, n, w1_r, w2_r , w3_r- arr[i], i + 1);
 
    fill_none = MaxCount(arr, n, w1_r, w2_r, w3_r ,i + 1);
    dp[i][w1_r][w2_r][w3_r] = max(fill_none, max(fill_w1,max(fill_w2,fill_w3)));
    return dp[i][w1_r][w2_r][w3_r];
}

int main()
{
    // int arr[] = { 1,1,1,1,5};
    int arr[maxN];
    int n;
    cout<<"No of weights:"<<endl;
    cin>>n;
    cout<<"weights Array:"<<endl;
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    memset(dp, -1, sizeof(dp));
    int w1,w2,w3;
    cout<<"Enter w1:";
    cin>>w1;
    cout<<"Enter w1:";
    cin>>w2;
    cout<<"Enter w1:";
    cin>>w3;
    // int w1 = 4, w2 = 2, w3= 1;
    cout <<"The max weight trucks can load is:"<<MaxCount(arr, n, w1, w2, w3, 0);
    return 0;
}