#include<bits/stdc++.h>
#include<vector>
#include<algorithm>

#define fo(n) for(int i=0; i<n; i++)

using namespace std;

int main() {

    int tc;
    // vector<int> numbers;
    cin >> tc;
    while(tc--){
        int n;
        string ans = "NO";
        cin >> n;
        int numbers[n];
        fo(n) cin >> numbers[i];
        fo(n) {
            for(int j=i+2; j<n;j++){
                if(numbers[i] == numbers[j]){
                    ans = "YES";   
                }
            }
        }
        cout << ans << endl;
    }
}