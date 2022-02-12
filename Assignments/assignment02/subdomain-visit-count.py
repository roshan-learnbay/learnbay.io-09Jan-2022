def subdomainVisits(cpdomains):
    n=len(cpdomains)
    hashMap={}
    i=0
    while(i<n):
        j=0
        digit=0
        rep=0
        l=len(cpdomains[i])
        while(cpdomains[i][j]!=' '):
            digit=ord(cpdomains[i][j])-ord('0')
            rep=rep*10+digit
            j+=1
        newString=cpdomains[i][j:l]
        j=len(newString)-1
        word=""
        while(j>=0):
            word=word+newString[j]
            if newString[j-1]=='.' or j==1:
                if word in hashMap:
                    hashMap[word]+=rep
                else:
                    hashMap[word]=rep
            j-=1
        i+=1
    newHashMap=[]
    for item in hashMap.keys():
        newHashMap.append(str(hashMap[item])+' '+item[::-1])

    return newHashMap

cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(subdomainVisits(cpdomains))
