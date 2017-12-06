# leetcode: https://leetcode.com/problems/encode-and-decode-strings/description/

# use a number and a sign(any char can work) to get the length of following string
    # then we can get the begining of next string

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for string in strs:
            res = res + ('%d:' %len(string)) + string
        return res


    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        res = []
        i = 0
        while i < len(s):
            len_index = s.find(":", i)
            i = len_index + int(s[i:len_index]) + 1
            res.append(s[len_index+1:i])
        return res
