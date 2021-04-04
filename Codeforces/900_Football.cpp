#include <bits/stdc++.h>
using namespace std;
int output(string a)
{
    int num = 1;
    for (int i = 1; i <= a.size() - 1; i++)
    {
        if (a[i - 1] == a[i])
        {
            num++;
        }
        else
        {
            num = 1;
        }
        if (num == 7)
        {
            cout << "YES" << endl;
            return 0;
        }
    }
    cout << "NO" << endl;
    return 0;
}
main()
{
    string a;
    cin >> a;
    output(a);
}