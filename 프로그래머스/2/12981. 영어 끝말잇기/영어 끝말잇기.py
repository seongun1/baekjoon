def solution(n, words):
    arr= []
    arr.append(words[0])
    for i in range(1,len(words)):
        word = words[i]
        if arr[-1][-1] == word[0] and word not in arr:
            #print(arr)
            arr.append(word)
            continue
        else:
            #print(i,n)
            return [(i%n)+1,(i//n)+1]
            
    return [0,0]