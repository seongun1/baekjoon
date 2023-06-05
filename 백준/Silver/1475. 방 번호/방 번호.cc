#include <iostream>
using namespace std;
int slice_N[10] = {};
int N;
int max(int a, int b)
{
	return (a > b) ? a : b;
}
int main() {
	// 숫자열을 하나씩 잘라서, 만약 같은 숫자들이 있다면 cnt를 추가한다.
	cin >> N;
	while (N != 0) {
		slice_N[N % 10]++;
		N /= 10;
	}

	int ans = 0;
	for (int i = 0; i < 10; i++) {
		if (i != 6 && i != 9)
			ans = max(slice_N[i], ans);
	}
	cout << max(ans,(slice_N[6] + slice_N[9]+1)/2);
}