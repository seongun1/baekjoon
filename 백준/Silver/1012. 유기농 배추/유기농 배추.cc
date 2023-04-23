#include <iostream>
#include <cstring>
using namespace std;
int a[51][51];
int jirung[51][51];
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
void DFS(int x, int y) //a가 원래 지도, b가 지렁이가 다니는 밭
{
	for (int i = 0; i < 4; i++) {
		if (jirung[x + dx[i]][y + dy[i]] == 0 && a[x + dx[i]][y + dy[i]] == 1) {
				jirung[x + dx[i]][y + dy[i]] = 1;
				DFS(x + dx[i], y + dy[i]);
		}
	}
}

int main()
{
	int t, m, n, k;
	cin >> t; // 트라이 횟수
	
	for (int i = 0; i < t; i++)
	{
		cin >> m >> n >> k; // m행//n열//배추의 갯수
		
		int q, w; // 좌표값
		for (int j = 0; j < k; j++) {
			cin >> q >> w;
			a[q][w] = 1;
		}
		if (k == 1) {
			cout << 1 << endl;
			continue;
		}
		
		int count = 0;
		for (int x = 0; x < n; x++) {
			for (int y = 0; y < m; y++) {
				if (jirung[y][x] == 0 && a[y][x] == 1) {
					jirung[y][x] = 1;
					DFS(y, x);
					count++;
				}
			}
		}
		cout << count << endl;
		count = 0;
		memset(a, 0, sizeof(a));
		memset(jirung, 0, sizeof(jirung));
	}
	
}