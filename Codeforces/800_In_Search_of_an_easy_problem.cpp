#include<bits/stdc++.h>
using namespace std;
int main() {
    int i;
    cin >> i;
    string ans = "EASY";
    while(i--){
        int x;
        cin >> x;
        if (x == 1){
            ans = "HARD";
            break;
        } 
    }
    cout << ans;
    return 0;
}