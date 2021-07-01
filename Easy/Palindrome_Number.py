class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x%10 == 0 and x != 0):
            return False   
        rev = 0
        while rev < x:
            pop = x % 10
            rev = rev*10 + pop
            x = x//10
        if rev in range(pow(-2, 31), pow(2, 31)-1) and (x == rev or x == rev//10):
            return True
        return False
