#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
//1. k 진수를 바꾸는 함수.
//2. 소수인지 판별하는 함수.
//3. k진수로 바꾸었을 때, 0을 기준으로 나누는 함수.
string to_n_number(int n, int k) // 10진수에서n의 숫자를 k 진수로 변환하기
{
	string s ="";
	while (n > 0) {
		s += to_string(n % k);
		n /= k;
	}
	reverse(s.begin(), s.end());
	return s;
}
bool is_prime(long long num) // 소수인지 판별하는 함수.
{
	if (num < 2)
		return false;
	for (int i = 2; i <= sqrt(num); i++) { // 제곱근 이하의 숫자에서 num을 나눌 수 있는 숫자가 있는지 생각 -> 있다면 그 숫자는 소수가 아님
		if (num % i == 0)
			return false;
	}
	return true;
}
int solution(int n, int k) {
	string s ="";
	s = to_n_number(n, k); // n 진수로 변환
	string tmp ="";
	int answer = 0;
	for (char c : s) // string s를, 하나씩 가져와서 검사하는 for- each문!
	{
		if (c == '0') { // 0을 기준으로 쪼갬
			if (!tmp.empty() && is_prime(stoll(tmp)))
				answer++;
			tmp = "";
		}
		else
			tmp += c;
	}
	if (!tmp.empty() && is_prime(stoll(tmp))) // 마지막 경우 = 0P인 경우.
		answer++;
	return answer;
}
