#include<bits/stdc++.h>
using namespace std;
int main() {
    int i, ans, c=0;
    cin >> i;
    ans = i/5; 
    ans += i%5==0? 0: 1;
    cout << ans;
    return 0;
}