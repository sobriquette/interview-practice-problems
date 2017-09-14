class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def getRemainder(self, dividend, divisor):
        if dividend % divisor == 0:
            return divisor
        else:
            return self.getRemainder(divisor, dividend%divisor)
                
    def gcd(self, A, B):
            divisor = min(A, B)
            dividend = max(A, B)
            if divisor == 0:
                return A
            else:
                return self.getRemainder(dividend, divisor)