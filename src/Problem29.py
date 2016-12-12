"""
https://leetcode.com/problems/divide-two-integers/
 Divide two integers without using multiplication, division and mod operator.
 If it is overflow, return MAX_INT.
"""
class Problem29(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        try:
            quotient = 0
            
        except OverflowError as e:
            print(e)
            return sys.maxint
