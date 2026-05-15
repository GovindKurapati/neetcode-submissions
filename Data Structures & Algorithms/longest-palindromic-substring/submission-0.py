class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        sLen = 0
        def expand(l,r):
            nonlocal sLen, res
            while l >=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > sLen:
                    res = s[l:r+1]
                    sLen = max(sLen, r-l+1)
                l-=1
                r+=1
        
        for i in range(len(s)):
            expand(i,i) #odd length

            expand(i,i+1) #even length
        
        return res