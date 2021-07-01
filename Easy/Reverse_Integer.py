class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        num = x
        while x!= 0:
            temp = abs(x)%10
            rev = rev*10 + temp
            x = abs(x)//10
        if rev in range(pow(-2, 31), pow(2, 31)-1):
            if num < 0:
                return -rev
            else: 
                return rev
        return 0
