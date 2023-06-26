	#include <iostream>
	#include <vector>
	#include <algorithm>
	#include <cmath>
	using namespace std;
	class position {
	public:
		int x, y;
	};
	int N, M;
	int MIN = 987654321;
	bool seleted[13];
	vector<position> chicken_h;
	vector<position> house_h;
	vector<position> picked;

	int DIstance(position a, position b) {
		return abs(a.x - b.x) + abs(a.y - b.y);
	}
	void min_distance() {
		int result = 0;
		for (int i = 0; i < house_h.size(); i++) { // 각 집으로부터 -> 모든 살아남은 치킨집 까지의 최소거리를 구함.
			int min_distance = 987654321;
			for (int j = 0; j < picked.size(); j++) {
				min_distance = min(min_distance, DIstance(house_h[i], picked[j]));
			}
			result += min_distance;
		}
		MIN = min(MIN, result);
	}
	void find_picked_h(int p, int m) { //폐업시키고 M개의 치킨집을 고르는 과정
		if (m == M)
			min_distance();

		for (int i = p; i < chicken_h.size(); i++) { // 치킨집 M개 고르기.
			if (seleted[i] == true) // 이미 다 골라져 있다면 다음 치킨집을 선정.
				continue;

			seleted[i] = true;
			picked.push_back({ chicken_h[i].x, chicken_h[i].y });
			find_picked_h(i, m + 1);
			seleted[i] = false;
			picked.pop_back();
		}
	}
	int main() {
		cin >> N >> M;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				int temp;
				cin >> temp;
				if (temp == 1) // 가정집이라면, 가정집 벡터에 넣기
					house_h.push_back({ i,j });
				else if (temp == 2) // 치킨집이라면 , 치킨집 벡터에 넣기
					chicken_h.push_back({ i,j });

			}
		}
		find_picked_h(0, 0);
		cout << MIN << endl;
	}