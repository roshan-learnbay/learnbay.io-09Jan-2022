def maxNumberOfBalloons(text):
    import collections
    cnt = collections.Counter(text)
    cntBalloon = collections.Counter('balloon')
    return min([cnt[c] // cntBalloon[c] for c in cntBalloon])


print(maxNumberOfBalloons('loonbalxlpoon'))
