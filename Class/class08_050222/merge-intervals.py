def merge(intervals):
    intervals=sorted(intervals, key=lambda x:x[0])      #O(NlogN) for sorting
    n=len(intervals)
    i=0
    j=1
    while j<n:
        if intervals[i][1]>intervals[j][0]:
            intervals[i][1]=max(intervals[i][1],intervals[j][1])
        else:
            i+=1
            intervals[i]=intervals[j]
        j+=1
    return intervals[0:i+1]


intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
