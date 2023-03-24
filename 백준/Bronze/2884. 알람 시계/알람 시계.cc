#include <iostream>
using namespace std;
int main() {
	int h, m;
	cin >> h >> m;
	 
		if (h >= 0 and h <= 23 and m >= 0 and m <= 59) {
			if (m >= 45)
				cout << h << " " << m - 45 << endl;
			else if (m < 45 and h>0)
				cout << h - 1 << " " << 15 + m << endl;
			else if (m < 45 and h == 0)
				cout << 23 << " " << 15 + m << endl;
		}
	
	}