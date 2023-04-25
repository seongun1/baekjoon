#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void quicksort(int a, int b, vector<int>& array) {
    int pivot = (a + b) / 2;
    if (a > b) return;
    int left = a;
    int right = b;
    while (left <= right) {
        while (array[left] < array[pivot]) left++;
        while (array[right] > array[pivot]) right--;
        if (left <= right) {
            swap(array[left], array[right]);
            left++;
            right--;
        }
    }
    quicksort(a, right, array);
    quicksort(left, b, array);
}

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