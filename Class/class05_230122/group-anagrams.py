 def join(strs):

     hashMap={}
     sbList=[]
     for s in strs:
         count=[0]*26
         for ch in s:
             #print(ord(ch)-ord('a'))
             count[ord(ch)-ord('a')]+=1
         sb=""
         #print(count)
         for i in range(26):
             sb+="#"
             sb+=(str(count[i]))
         #print("sb=",sb)
         sbList.append(sb)
         if sb in hashMap:
             hashMap[sb].append(s)
         else:
             hashMap[sb]=[s]
     #print(sbList)
     return hashMap.values()

 strs=["eat","tea","tan","bat","nat","ate"]
 print(join(strs))
