#include<bits/stdc++.h>
using namespace std;
int main(){

    string s, sample="WUB";
    cin >> s;
    for(int i=0; i<s.size(); i++){
        s.substr(i, 3) == sample? s.replace(i, 3, "   "): "";
    };
    cout << s;
    return 0;
}