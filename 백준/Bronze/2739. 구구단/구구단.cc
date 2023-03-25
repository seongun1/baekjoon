#include <iostream>
using namespace std;
int main() {
	int n;
	cin >> n;
	if (n >= 1 and n <= 9) {
		for (int i = 1; i < 10; i++) {
			cout <<n<<" " << "*" <<" " << i <<" " << '=' <<" "<< n * i << endl;
		}
	}
	}