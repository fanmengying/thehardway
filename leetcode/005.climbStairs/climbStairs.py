# leetcode: https://leetcode.com/problems/climbing-stairs/#/description
class Solution(object):
    def climbStairs(self, n):
        """
        : type n: int
        : rtype: int
        """
        # second solution
        # to make solution time complexity O(n), space complexity: O(n)
        # f(n) = f(n -1) + f(n-2)
        # use a list to memorize previous solution
        # python2: range is a list so the space complexity is O(n) , xrange is an xrange object that will always take the same amount of memory
        result = [1, 1]
        for i in xrange(2, n + 1):
            result.append(result[i - 2] + result[i - 1])
        return result[n]

    def climbStairs2(self, n):
        # initial solution
        # n = 1, one solution
        # n >= 2, two categories: 1, last step: 2  or 2, last step: 1
        # f(n) = f(n-1) + f(n-2) fibonacci
        # time complexity: O(2^n) space complexity: O(n)
        if n == 0:
            return 1
        elif n == 1:
            return 1
        return self.climbStairs2(n - 1) + self.climbStairs2(n - 2)

    def climbStairs3(self, n):
        # time complexity O(n) and space complexity O(1)
        prev = cur = 1
        for i in xrange(2, n + 1):
            temp = cur
            cur = prev + cur
            prev = temp
        return cur

solution = Solution()
print "solution1"
for i in xrange(0, 60):
    print solution.climbStairs(i)
for i in xrange(0, 60):
    print solution.climbStairs3(i)
print "solution2"
for i in xrange(0, 60):
    print solution.climbStairs2(i)
