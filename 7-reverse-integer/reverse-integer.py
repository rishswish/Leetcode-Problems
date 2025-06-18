class Solution:
    def reverse(self, x: int) -> int:
            rev=0
      
            if x>0:
                while x>0:
                    digit=x%10
                    rev=rev*10+digit
                    x=x//10
                if -2**31 <= rev <= 2**31 - 1:
                    return rev
                else:
                    return 0
            else:
                x=x*-1
                while x>0:
                    digit=x%10
                    rev=rev*10+digit
                    x=x//10
                if -2**31 <= rev*-1 <= 2**31 - 1:
                    return rev*-1
                else:
                    return 0



        