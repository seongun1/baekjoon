#include <iostream>
using namespace std;
int main() {
	int x, y;
	cin >> x;
	cin >>y;
	if (-1000 <= x and x <= 1000 and -1000 <= y and y <= 1000) {
		if (x > 0 and y > 0)
			cout << 1 << endl;
		if (x >0 and y < 0)
			cout << 4 << endl;
		if (x < 0 and y>0)
			cout << 2 << endl;
		if (x < 0 and y < 0)
			cout << 3 << endl;
	}
	}