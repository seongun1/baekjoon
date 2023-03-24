#include <iostream>
using namespace std;
int main() {
	int score;
	cin >> score;
	if (score >= 0 && score <= 100) {
		if (score <= 100 and score >= 90)
			cout << 'A' << endl;
		if (score <= 89 and score >= 80)
			cout << 'B' << endl;
		if (score <= 79 and score >= 70)
			cout << 'C' << endl;
		if (score <= 69 and score >= 60)
			cout << 'D' << endl;
		if(score <=59)
			cout << 'F' << endl;
	}
	}