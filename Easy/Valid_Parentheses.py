class Solution:
    def isValid(self, s: str) -> bool:
        check = {"(":")","[":"]","{":"}"}
    
        stack = []
        for i in s:
            if i in check:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                if i is check[stack[-1]]:
                    del stack[-1]
                else:
                    return False
        if len(stack)>0:
            return False
        else:
            return True
