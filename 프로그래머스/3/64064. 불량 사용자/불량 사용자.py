from itertools import combinations

def is_same(arr1,arr2):
    for k in range(len(arr1)):
        if arr1[k] == '*':
            continue
        elif arr1[k] != arr2[k]:
            return False
    return True
        

def solution(user_id, banned_id):
    combination = []
    for i in range(len(banned_id)):
        tmp = []
        for j in range(len(user_id)):
            if len(banned_id[i]) == len(user_id[j]):
                if is_same(banned_id[i],user_id[j]):
                    tmp.append(user_id[j])
        combination.append(tmp)
    print(combination)
    cases = set()
    def dfs(idx,selected):
        if idx == len(combination):
            cases.add(tuple(sorted(selected)))
            return
        for user in combination[idx]:
            if user not in selected:
                dfs(idx+1,selected + [user])
                
    dfs(0,[])
    
    return len(cases)