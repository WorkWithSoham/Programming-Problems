#include<bits/stdc++.h>
#include<algorithm>
using namespace std;

#define fo(m) for(int i=0; i<m; i++)
long long int arr[100000];

int main() {
    for(long long int i=0;i<=100005;i++)
    {
        arr[i]=i*i*i;
    }
    int t;
    cin>>t;
    while(t--)
    {
        long long int n;
        cin>>n;
        int i=1;
        i=cbrt(n)+1;
        int cb=i;
        int l=1;
        int r=i;
        int f=0;
        while(l<=r)
        {
            if(arr[l]+arr[r]>n){r--;}
            else if(arr[l]+arr[r]<n){l++;}
            else if(arr[l]+arr[r]==n)
            {f=1;
            break;
            }
        }
 
        if(f){cout<<"YES"<<endl;}
        else{cout<<"NO"<<endl;}
    }
    return 0;
}