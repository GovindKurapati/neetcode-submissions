class Solution:
    def checkValidString(self, s: str) -> bool:
        openBrackets = []
        wildcard = []

        for i, ch in enumerate(s):
            if ch == "(":
                openBrackets.append(i)
            elif ch == "*":
                wildcard.append(i)
            else:
                if not openBrackets and not wildcard:
                    return False
                if openBrackets:
                    openBrackets.pop()
                else:
                    wildcard.pop()
        
        while openBrackets and wildcard:
            if wildcard.pop() < openBrackets.pop():
                return False
        return not openBrackets
