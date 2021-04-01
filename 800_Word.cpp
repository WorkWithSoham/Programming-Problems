#include<bits/stdc++.h>
using namespace std;
int main() {
    string s;
    int count_up=0, count_lo=0;
    cin >> s;
    for(int i=0; i<s.length(); i++){
        s[i] == tolower(s[i])? count_lo+=1 : count_up+=1;
        // cout << count_lo << count_up << "\n";
    }
    if(count_up > count_lo){
        transform(s.begin(), s.end(), s.begin(), ::toupper);
        cout << s;
    } else {
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        cout << s;
    } 
    return 0;
}