def eraseOverlapIntervals(intervals):
    overlap=0
    intervals=sorted(intervals, key=lambda x:x[1])
    i=0
    j=1
    while j<len(intervals):
        #print(j)
        if intervals[i][1]<=intervals[j][0]:
            #print(intervals[i][0],intervals[i][1])
            i=j
        else:
            overlap+=1
        j+=1
    return overlap
