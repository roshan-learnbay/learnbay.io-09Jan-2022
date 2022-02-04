def myAtoi(s):
    import sys
    if len(s)==0:
        return 0

    index=0
    sign=1
    while(index<len(s) and s[index]==" "):
        index+=1

    if index==len(s):
        return 0

    if s[index]=='+' or s[index]=='-':
        sign=1 if s[index]=='+' else -1
        index+=1

    res=0

    while(index<len(s)):
        digit=ord(s[index])-ord('0')
        if digit<0 or digit>9:
            break
        #print(res,index,len(s),digit)
        if (((2**31-1-digit)//10)<res):
            return 2**31-1 if sign==1 else (-2**31)
        res=res*10 + digit
        index+=1
    #res=res*10+digit
    return res*sign

s="  -4012 with words"
print(myAtoi(s))
