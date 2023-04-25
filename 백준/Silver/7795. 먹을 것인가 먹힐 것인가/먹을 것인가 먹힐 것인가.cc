#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int a, b;
        cin >> a >> b;

        vector<int> arraya (a);
        vector<int> arrayb (b);

        for (int i = 0; i < a; i++) {
            cin >> arraya[i];
        }

        for (int i = 0; i < b; i++) {
            cin >> arrayb[i];
        }

        sort(arraya.begin(), arraya.end());
        sort(arrayb.begin(), arrayb.end());

        int count = 0;
        int j = 0;
        for (int i = 0; i < a; i++) {
            while (j < b && arraya[i] > arrayb[j]) {
                j++;
            }
            count += j;
        }
        cout << count << "\n";
        arraya.clear();
        arrayb.clear();
    }
    return 0;
}
