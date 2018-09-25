class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        if left < 10:
            result = [x for x in range(left, min(right+1, 10))]

        if right > 10:
            for x in range(max(11, left), right+1):
                selfDivid = True
                v = x
                while x > 0:
                    r = x % 10
                    if r == 0 or v % r > 0:
                        selfDivid = False
                        break
                    x /= 10
                if selfDivid:
                    result.append(v)
        return result
