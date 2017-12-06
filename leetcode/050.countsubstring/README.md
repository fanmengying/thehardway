https://leetcode.com/problems/count-binary-substrings/description/

1. my method:
   check all substrings
   use a helper function to check whether the substring is a valid substring
   1. whether the length of substring is an even
   2. whether start and end are 0, 1 or 1, 0
   3. whether char at the symmetrical position are the same
   it will be O(n ^ 3) time complexity as the helper function will use O(n)
   check all substrings will take O(n ^ 2)
   space complexity: O(n ^ 2)

2. other's method:
   after testing, I found input string will contain 1 and 0.
   Then I learned from other's method, which use a cur_len and pre_len to track the adjacent two group of 0s or 1s. If the previous group's length >= cur_group, then a valid substring can be generated. 
time complexity: O(n)
