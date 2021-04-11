#include<bits/stdc++.h>
#include<algorithm>
#define ll long long
using namespace std;

int main(){
    ll t;
    cin >> t;
    while(t--)
    {
		ll x,n,m;
        cin>>x>>n>>m;
 
        ll flag=0;
        while((x>20)&&(n>0)){
            x = x/2 + 10;
            n--;    
        }
 
        while((x>0)&&(m>0)){
            x = x-10;
            m--;
            if(x<=0){
                flag=1;
                break;
            }
        }
 
        if(flag==1){
            cout<<"YES"<<"\n";
        }else{
            cout<<"NO"<<"\n";
        }
    }
}