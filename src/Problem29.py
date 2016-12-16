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
            while quotient < sys.maxint:
                sign = 1
                if dividend < 0:
                    sign *= -1
                    dividend *= -1
                if divisor < 0:
                    sign *= -1
                    divisor *= -1
                if divisor == 1:
                    return dividend * sign
                while dividend > 0 and dividend >= divisor:
                    dividend -= divisor
                    quotient += 1
                print(sys.maxint)
                print(quotient)
                return quotient * sign
            return sys.maxint
        except OverflowError as e:
            # print(e)
            return sys.maxint
