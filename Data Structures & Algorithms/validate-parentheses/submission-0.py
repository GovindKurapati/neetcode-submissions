class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(" : ")", "{" : "}", "[" : "]"}
        stack = []

        for i in s:
            if i in pairs:
                stack.append(i)
            else:
                if not stack:
                    return False
                
                if pairs[stack.pop()] != i:
                    return False
        return not stack