#include<bits/stdc++.h>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;

#define fo(n) for(int i=0; i<n; i++)
#define vi vector<int>
#define ll long long

int main(){
    int n, m, k;
    cin >> n;
    vi pr;
    fo(n) {
        cin >> k;
        pr.push_back(k);
    }
    cin >> m;
    vi co;
    fo(m) {
        cin >> k;
        co.push_back(k);
    }
    fo(m) {
        int ans=0;
        for(int j=0; j<n; j++){
            if(co[i] >= pr[j]){
                ans++;
            }
        }
        cout <<  ans << endl;
    }
    return 0;
}