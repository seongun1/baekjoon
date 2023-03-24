#include <iostream>
using namespace std;
int main() {
	int a, b,c;
	cin >> a >> b;
	cin >> c;
	if (b + c < 60)
		cout << a << " " << b + c << endl;
	else if (b + c >= 60) {
		int h = (b + c) / 60;
		int m = (b + c) % 60;
		if (a + h < 24)
			cout << a + h << " " << m << endl;
		else if (a + h >= 24)
			cout << (a + h) - 24 << " " << m << endl;
	}
	}