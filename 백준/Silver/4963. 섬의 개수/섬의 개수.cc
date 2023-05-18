#include <iostream>
#include <cstring>
using namespace std;

int w, h; // 너비 w, 높이 h
int a[51][51];
int b[51][51] = { 0 };
int cnt[100] = { 0 };
int go_y[8] = { 0, 1, 0, -1, 1, -1, -1, 1 };
int go_x[8] = { 1, 0, -1, 0, 1, -1, 1, -1 };

void DFS(int y, int x)
{
    b[y][x] = 1;
    for (int i = 0; i < 8; i++)
    {
        int dy = y + go_y[i];
        int dx = x + go_x[i];
        if (dy >= 0 && dy < h && dx >= 0 && dx < w) {
            if (a[dy][dx] == 1 && b[dy][dx] == 0) {
                DFS(dy, dx);
            }
        }
    }
}

int main() {
    int k = 0;
    while (true)
    {
        cin >> w >> h; // 너비 w, 높이 h
        if (w == 0 && h == 0) break;

        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++)
            {
                char x;
                cin >> x;
                a[i][j] = x - '0';
            }
        }

        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (a[i][j] == 1 && b[i][j] == 0) {
                    b[i][j] = 1;
                    DFS(i, j);
                    cnt[k]++;
                }
            }
        }
        k++;
        memset(a,0, sizeof(a));
        memset(b,0, sizeof(b));
    }

    for (int i = 0; i < k; i++)
        cout << cnt[i] << endl;
}
