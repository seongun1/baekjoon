#include <iostream> 
int max(int a, int b) { return (a > b) ? a : b; }
using namespace std;
int dp[10001];
int wine[10001];
int main() {
	int n; // 포도주 잔의 갯수 n
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int volume; // 포도주 1잔에 담긴 각각의 포도주 양
		cin >> volume;
		wine[i] = volume;
	}
	for (int i = 0; i < n; i++)
	{
		if (i == 0) {
			dp[0] = wine[0];
		}
		else if (i == 1)
		{
			dp[1] = wine[0] + wine[1];
		}
		else if (i == 2)
			dp[2] = max(wine[0] + wine[1], max(wine[0] + wine[2], wine[1] + wine[2]));
		else if (i > 2) // i가 3일때부터 적용
		{
			dp[i] = max(dp[i - 1], max(dp[i - 2] + wine[i], dp[i - 3] + wine[i] + wine[i - 1]));
		}
	}
	cout << dp[n-1];
}