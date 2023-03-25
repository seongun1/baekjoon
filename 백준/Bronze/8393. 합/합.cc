#include <iostream>
using namespace std;
int main() {
	int n,a=0;
	cin >> n;
	if (n >= 1 and n <= 10000) {
		for (int i = 1; i <= n; i++) {
			a+=i ;
		}
	}
	cout << a;
}