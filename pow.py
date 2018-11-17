

class Solution:
    def power(self,base,power):
        if power==0:
            return 1
        
    def pow(self, x, n, d):        
        res = 1  # Cover case d == 1
        while n > 0:         
            if n % 2:  # Odd?            
                res = (res * x) % d
            x = x**2 % d
            n -= 1
        return res

print(pow(5,2,3))
