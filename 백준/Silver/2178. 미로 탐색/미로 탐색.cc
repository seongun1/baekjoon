#include <iostream>
#include <queue>
using namespace std;
int a[101][101];
int go_y[4] = { 0,1,0,-1 };
int go_x[4] = { 1,0,-1,0 };
int N, M; // N은 세로 , M은 가로
int BFS(int y, int x)
{
	queue <pair<int,int>> que;
	que.push({ y,x });
	
	while (!que.empty()) {
		int y = que.front().first;
		int x = que.front().second;
		que.pop();
		for (int i = 0; i < 4; i++) {
			int dy = y + go_y[i];
			int dx = x + go_x[i];
			if (dx < 0 || dx >= M || dy < 0 || dy >= N)continue; // 범위를 벗어나면 튕겨냄
			if (a[dy][dx] == 0) continue; // 벽이 있다면 튕겨냄
			if (a[dy][dx] == 1) {
				a[dy][dx] = a[y][x] + 1;
				que.push({ dy,dx });
			}
		}
	}
	return a[N - 1][M - 1];
}

int main() {
	
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			char x;
			cin >> x;
			a[i][j] = x - '0';
		}
	}
	cout << BFS(0, 0) << endl;
}