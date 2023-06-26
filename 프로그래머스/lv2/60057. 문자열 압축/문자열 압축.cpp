#include <string>
using namespace std;
int solution(string s) {
    int answer = s.size();
    for (int i = 1; i <= s.size() / 2; i++) {
        int count = 1;
        string box = ""; // 개행문자 하나씩 자르기.
        string temp = "";
        box = s.substr(0, i);
        for (int j = i; j < s.size(); j += i) {
            if (box == s.substr(j, i))
                count++;
            else {
                if (count > 1)
                    temp += to_string(count);
                temp += box;
                box = s.substr(j, i);
                count = 1;
            }
        }
        if (count > 1)
            temp += to_string(count);
        temp += box;
        if (answer > temp.size())
            answer = temp.size();
    }
    return answer;
}