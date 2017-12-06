https://leetcode.com/problems/encode-and-decode-strings/description/

method:
use a number index to record the length of the following string
use a char to track the begining of the following string and separate the string
we can use the separation char and the length index to get the begining of next string

encode:
Time: O(n) n is the length of string list

decode:
Time: O(n) n is the length of string
