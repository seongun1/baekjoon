#include<vector>
#include <iostream>
#include <queue>
using namespace std;
int go_y[4] = { 1,0,-1,0 };
int go_x[4] = { 0,1,0,-1 };
bool way[101][101] = { false, };
int dist[101][101] = { 0, };
queue <pair<int, int>> que;
int solution(vector<vector<int>> maps)
{
    int N = maps.size();
    int M = maps[0].size();
    
    way[0][0] = true;
    dist[0][0] = 1;
    que.push({ 0,0 });
    while (!que.empty())
    {
        int y = que.front().first;
        int x = que.front().second;
        que.pop();
        for (int i = 0; i < 4; i++) {
            int ny = y + go_y[i];
            int nx = x + go_x[i];
            if ((0 <= nx && nx < M) && (0 <= ny && ny < N) && (!way[ny][nx] && maps[ny][nx] == 1) ) {
                way[ny][nx] = true;
                que.push({ ny,nx });
                dist[ny][nx] = dist[y][x] + 1;
            }
        }
    }
    int answer = dist[N - 1][M - 1];
    if (answer == 0)
        return -1;
    return answer;
}