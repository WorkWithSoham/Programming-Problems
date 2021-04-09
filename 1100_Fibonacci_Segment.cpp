#include<bits/stdc++.h>
#include<algorithm>
using namespace std;

#define fo(n) for(int i=0; i<n; i++)

int main() {
    int a, ans=-1, count=0;
    cin >> a;
    vector<int> vc;
    fo(a){
        int x;
        cin >> x;
        vc.push_back(x);
    }
    for(int j=0; j<a; j++){
        if(j < 2){
			count++;
			ans = max(ans,count);
			continue;
		}
		if(vc[j] == vc[j-1]+vc[j-2]){
			if(count == 0)
				count = 2;
			count++;
			ans = max(ans,count);
		}
		else{
			ans = max(ans,count);
			count = 0;
		}
    }
    if (vc.size() <= 2) ans=vc.size();
    cout << ans;
    return 0;
}