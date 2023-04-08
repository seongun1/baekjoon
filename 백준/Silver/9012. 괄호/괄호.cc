#include <iostream>
using namespace std;

int main() {
	char a = '(';
	char b = ')';
	int as=0, bs=0;
	int count;
	cin >> count;
	string sign;
	for (int i = 0; i < count; i++) {
		cin >> sign;
		int k = 0;
		while (k < sign.size()) {
			if (sign[k] == a)
				as++;
			else if (sign[k] == b)
				bs++;
			if (bs > as) {
				cout << "NO" << endl;
				break;
			}
			k++;
			if (as == bs && k == sign.size())
				cout << "YES" << endl;
			else if (as != bs && k == sign.size())
				cout << "NO" << endl;
			
		}

		as = 0, bs = 0;
	}

	
}
