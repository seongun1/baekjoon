import sys

s = sys.stdin.readline().strip()

def isAkaraka(s):
    while(1):
        if len(s) ==1:
            break

        middle = len(s) //2
        if len(s) %2:
            s1 = s[:middle]
            s2 = s[middle+1:]
            s2 = s2[::-1]
            #print(s,s1,s2)

        else:
            s1 = s[:middle]
            s2 = s[middle:]
            s2 = s2[::-1]

        if s1 == s2:
            s = s1[::]
        else:
            print("IPSELENTI")
            return
        
    print('AKARAKA')
    return

isAkaraka(s)
        
            