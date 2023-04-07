#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int water_lose, tape_lenth;

 	cin >> water_lose >> tape_lenth;
	
 	vector<double> pipe;
	int a;
	for (int i = 0; i < water_lose; i++) {
		cin >> a;
		pipe.push_back(a);
	}
	sort(pipe.begin(), pipe.end());


	int hole_start = 0;
	int i = 0;
	int tape = 1; 
	
	while (i < water_lose)
	{
		if (pipe[hole_start] - 0.5 + tape_lenth >= pipe[i] + 0.5)
			i++;
		else {
			tape++;
			hole_start = i;
		}
	}
	
	cout << tape;
}