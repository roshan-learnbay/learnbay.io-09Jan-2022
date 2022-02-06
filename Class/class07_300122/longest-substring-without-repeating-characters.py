def lengthOfLongestSubstring(s):
    n=len(s)
    resLen=0
    hashSet=set()
    start=end=0

    while(end<n):

        while(end<n and (s[end] not in hashSet)):

            hashSet.add(s[end])
            #print(s[end],hashSet)
            tmpLen=len(hashSet)
            resLen=max(tmpLen,resLen)
            end+=1
        #print('start',start,"end",end, "length",resLen)
        #print(hashSet,"before removal", s[start])
        #print("repeat")
        while (end<n and (s[end] in hashSet)):
            #print(start,end)
            hashSet.remove(s[start])
            start+=1
        #print(hashSet,"after removal", s[start])
        if end<n:
            hashSet.add(s[end])
        #start+=1
        end+=1
    
    return resLen

print(lengthOfLongestSubstring("abcabcbb"))
