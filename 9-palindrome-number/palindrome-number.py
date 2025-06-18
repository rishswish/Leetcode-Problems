class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        original=x
        if x>0:
            while x>0:
                digit=x%10
                rev=rev*10+digit
                x=x//10

        # else:
        #     x=x*-1
        #     while x>0:
        #         digit=x%10
        #         rev=rev*10+digit
        #         x=x//10
        #     rev=rev*-1
        
        return rev==original



