def count_binary_substrings(s):
    n=len(s)
    ans=prev=0
    curr=1
    for i in range(1,n):
        if s[i-1]!=s[i]:
            ans+=min(prev,curr)
            prev=curr
            curr=1
        else:
            curr+=1

    return ans+min(prev,curr)

s="00011100"
print(count_binary_substrings(s))
