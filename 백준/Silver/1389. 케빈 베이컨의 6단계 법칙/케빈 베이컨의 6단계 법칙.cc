#include <iostream>
using namespace std;
//백준 1389
// 플로이드- 와샬 알고리즘
int N; // 유저의 수
int M; // 친구 관계의 수
int temp;
int a[101][101]; // 친구의 관계를 담는 배열
const int INF = 10000;
void floid() {
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (i != j && a[i][j] != 1)
				a[i][j] = INF;
		}
	}
	for (int k = 1; k <= N; k++) { // k는 거쳐가는 점.
		for (int i = 1; i <= N; i++) { // i는 시작점
			for (int j = 1; j <= N; j++) {// j는 도착하는 점.
			if (a[i][k] + a[k][j] < a[i][j])
				a[i][j] = a[i][k] + a[k][j]; // 직접 가는 값을 돌아서 가는 값으로 교체.
			}
		}
	}
}
int main() {
	cin >> N >> M;
	
	// 친구 관계를 받기
	for (int i = 0; i < M; i++) {
		int p, q;
		cin >> p >> q;
		a[p][q] = 1;
		a[q][p] = 1;
	}
	floid();
	int val = 10000000;
	int res;
	for (int i = 1; i <= N; i++) {
		int tmp = 0;
		for (int j = 1; j <= N; j++) {
			tmp += a[i][j];
		}
		if (tmp < val) {
			val = tmp;
			res = i;
		}
	}
	cout << res;
}