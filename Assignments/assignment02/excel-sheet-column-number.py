def titleToNumber(columnTitle):
    n=len(columnTitle)
    colNum=0
    i=0
    while i<n:
        charNum=ord(columnTitle[i])-ord('A')+1
        factor=26**(n-i-1)
        #print(charNum,factor)
        colNum+=factor*charNum
        i+=1
    return colNum

columnTitle="ASDFG"
print(titleToNumber(columnTitle))
