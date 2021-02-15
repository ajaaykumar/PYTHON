
class Solution:
    def solve(self, s):
        var = ""
        if s:
            for i in s:
                if i not in var:
                    var += i
                else:
                    return False
            else:
                return True
        else:
            return True

s = Solution()
s.solve('aabcd')


