# leetcode: https://leetcode.com/problems/count-binary-substrings/description/

def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev_len = 0
        cur_len = 1
        res = 0
        for i in xrange(len(s) - 1):
            if s[i+1] == s[i]:
                cur_len += 1
            else:
                prev_len = cur_len
                cur_len = 1
            if prev_len >= cur_len:
                res += 1
        return res

def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in xrange(len(s)-1):
            for j in xrange(i+1, len(s)):
                if self.validSubstring(s[i:j+1]):
                    res += 1
        return res

    def validSubstring(self, s):
        i = 0
        start = s[i]
        j = len(s) - 1
        end = s[j]
        if not(start == '0' and end == '1') and not(start == '1' and end == '0'):
            return False
        if len(s) % 2 != 0:
            return False
        while i < j:
            if s[i] != start or s[j] != end:
                return False
            i += 1
            j -= 1
        return True
