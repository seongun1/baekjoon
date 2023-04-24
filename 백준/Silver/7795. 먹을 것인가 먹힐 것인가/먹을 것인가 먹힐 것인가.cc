#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int t, n, m;
vector<int> a, b;

int main() {
	scanf("%d",&t);
	while (t--) {
		scanf("%d%d", &n, &m);
		a = vector<int>(n);
		b = vector<int>(m);

		for (int i = 0; i < n; i++)scanf("%d", &a[i]);
		for (int i = 0; i < m; i++)scanf("%d", &b[i]);
		
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());

		int ans = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++)
				if (a[i] > b[j]) {
					ans++;
				}
				else break;
		}
		printf("%d\n", ans);
	}
	return 0;
}