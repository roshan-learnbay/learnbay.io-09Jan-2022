def getDescentPeriods(prices):
    sdp=0
    start=0
    end=1
    while end<len(prices):
        #print(prices[end],start,end,sdp,'outside')
        if prices[end]==prices[end-1]-1:
            sdp+=end-start+1
        else:
            start=end
            sdp+=end-start+1
            #print(prices[end],start,end,sdp)
        end+=1

    return sdp+1

print(getDescentPeriods([3,2,1,4,6,10,9,8,7]))
