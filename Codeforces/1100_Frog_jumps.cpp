#include<bits/stdc++.h>
#include<vector>
#include<algorithm>
using namespace std;

#define ar array
#define vi vector<int>
#define fo(n) for(int i=0; i<n; i++)

int tc;
string l;
vector<int> vc;
int main(){
    cin >> tc;
    while(tc--){
        int a=0, b=0, c=0;
        cin >> l;
        vc.clear();
        fo(l.size()){
            if(l[i] == 'R'){
                vc.push_back(i+1);
            }
        }
        if (vc.size() == 0) vc.push_back(l.size()+1);
        a = vc[0];
        c = l.size() - vc[vc.size()-1] + 1;
        fo(vc.size()-1){
            b = max((vc[i+1]-vc[i]), b);            
        }
        cout << max(c, max(a, b)) << endl;
    }
}