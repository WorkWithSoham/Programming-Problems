#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main() {
    string s1, s2;
    cin >> s1 >> s2;
    transform(s1.begin(), s1.end(), s1.begin(), ::tolower);
    transform(s2.begin(), s2.end(), s2.begin(), ::tolower);
    int i;
    i = (s1 == s2)? 0: i;
    i = (s2 > s1)? -1: i;
    i = (s2 < s1)? 1: i;
    cout << i;
}
