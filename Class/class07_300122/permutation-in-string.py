def isZero(freqCount):
    for i in range(26):
        if freqCount[i]!=0:
            return False
    return True
def checkInclusion(s1, s2):
#******************************************************
#       Working but O(m*nlogn)
#******************************************************
    '''
        n=len(s2)
        start=0
        end=len(s1)-1
        s1 = ''.join(sorted(s1))
        while(end<n):
            tmpStr=str(s2[start:end+1])
            tmpStr = ''.join(sorted(tmpStr))
            if tmpStr==s1:
                return True
            start+=1
            end+=1
        return False
    '''
#******************************************************
#       Working with O(N)
#******************************************************
    n=len(s2)
    freq=[0]*26
    for c in s1:
        freq[ord(c)-ord('a')]+=1
    #print(freq)
    start=end=0
    while end<n:
        freq[ord(s2[end])-ord('a')]-=1

        while (end-start+1)>len(s1):
            freq[ord(s2[start])-ord('a')]+=1
            start+=1
        if (end-start+1)==len(s1):
            if isZero(freq):
                return True
        #print(freq)
        end+=1
    return False

print(checkInclusion("ab","eidbaoo"))
