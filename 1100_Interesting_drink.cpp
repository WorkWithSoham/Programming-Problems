#include<bits/stdc++.h>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;

#define fo(n) for(int i=0; i<n; i++)
#define vi vector<int>
#define ll long long

const int MAXN = 1e5;
int ar [ MAXN ];

int main() {
	int n;
	cin >> n;
	fo(n) cin >> ar [ i ];
	sort(ar , ar + n);
	int m;
	cin >> m;
	fo(m)
	{
		int a;
		cin >> a;
		cout <<  upper_bound(ar, ar + n, a) - ar << endl;
	}	
}