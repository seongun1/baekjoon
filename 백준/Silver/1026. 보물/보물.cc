#include <iostream> 
#include <vector>
#include <algorithm>
using namespace std;

int main() {

	int n;
	cin >> n;

	// a의 최댓값과 b의 최솟값을 각각 곱하는 방법
	vector <int> a(n);
	vector <int> b(n);
	vector <int> c(n,0);
	vector <int> d(n);
	int k = 0;
	
	for (int i = 0; i < n; i++)
	{
		cin >>k;
		a[i] = k;
	}
	
	for (int i = 0; i < n; i++)
	{
		cin >> k;
		b[i] = k;
	}
	c = b;
	sort(a.begin(), a.end());
	sort(c.begin(), c.end());
	int p = n - 1;

	for (int i = 0; i < n; i++)
	{
		d[i] = a[i] * c[p];
		p--;
	}
	int sum = 0;
	for (int i = 0; i < n; i++)
	{
		sum += d[i];
	}
	cout << sum;
}