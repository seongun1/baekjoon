
def solution(diffs, times, limit):
    def time_count(level):
        time =times[0]
        for i in range(1,len(diffs)):
            if level >= diffs[i]:
                time += times[i]
            else:
                time += (diffs[i] - level) * (times[i-1] + times[i])  + times[i]
            if time > limit:
                return False
        return True
    
    low,high = 1,max(diffs)
    middle = (low + high) //2
    while (low < high):
        middle = (low+high) //2
        if not time_count(middle):
            low = middle+1
        else:
            high = middle
    return low
    