#include <string>
#include <vector>
#include <map>
#include <set>
#include <sstream>
using namespace std;

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    vector<int> answer(id_list.size(), 0);

    map<string, int> id_map;
    map<string, set<string>> report_count; // 신고 받은 한 사람과 그 사람을 신고한 사람들을 저장하는 map
    for (int i = 0; i < id_list.size(); i++) {
        id_map[id_list[i]] = i;
    }
    // report 에서는 신고 한사람 -> 신고 받은 사람으로 데이터가 들어온다.
    // 신고 당한 한 사람과 / 신고를 한 사람들을 한 사람, 그 사람을 신고한 배열들로 파싱하여 report_count에 담는다.
        for (auto rep : report) {
            stringstream ss(rep);
            string from, to;
            ss >> from >> to;
            report_count[to].insert(from);
        }
        //만약 신고를 한 사람들의 숫자가 일정 숫자(k)가 넘어가면, 신고를 받아서 정지를 하고, 
        //id_map(회원 리스트)의 있는 사람들을 검색하여(id_map[in_iter]) 그 사람이 받는 메일의 갯수(answer)의 값을 증가 시킨다.
        for (auto iter : report_count) {
            if (iter.second.size() >= k) {
                for (auto in_iter : iter.second) {
                    answer[id_map[in_iter]]++;
                }
            }
        }
    return answer;
}