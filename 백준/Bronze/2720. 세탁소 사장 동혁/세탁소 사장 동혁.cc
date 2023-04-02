#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	int Q , D , N, P;// Q =25 D =10 N =5 P =1
	int charge;
	for (int i = 0; i < T; i++) {
			cin >> charge;
			Q = charge / 25;
			D = (charge - (25 * Q)) / 10;
			N = (charge - (25 * Q) - (10 * D)) / 5;
			P = (charge - (25 * Q) - (10 * D)-(5*N)) / 1;
			cout << Q << " " << D << " " << N << " " << P << endl;
	}
}