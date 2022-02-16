def maxLengthBetweenEqualCharacters(s):
    # length=-1
    # idxMap={}
    # for idx,char in enumerate(s):
    #     if char in idxMap:
    #         idxMap[char].append(idx)
    #         length=max(length, (idx-min(idxMap[char])-1))
    #     else:
    #         idxMap[char]=[idx]
    # return length
    #print([s.rfind(ch) - s.find(ch) - 1 for ch in set(s)])
    #return max(s.rfind(ch) - s.find(ch) - 1 for ch in set(s))
    return max(map(sub, count(), map({}.setdefault, s, count(1))))


print(maxLengthBetweenEqualCharacters('abcdefbsgjasjbjkfoea'))
