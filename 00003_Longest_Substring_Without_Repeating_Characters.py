# from collections import Counter
# from itertools import combinations
# from random import shuffle

# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
        # """
        # :type s: str
        # :rtype: int
        # """
# My Solution
#         # all possible pairs of slice indices
#         cbin = list(combinations(range(len(s) + 1), r=2))
#         shuffle(cbin)
        
#         # list of substring without repeated chars
#         substrings = [
#             s[x:y] for x, y in cbin if len(set(s[x:y])) == len(s[x:y])
#         ]

#         # len of longest substring
#         longest_length = 0
#         if len(substrings) != 0:
#             longest_length = max(map(len, substrings))

#         return longest_length


# Leetcode solution 1
# In the naive approaches, we repeatedly check a substring to see if it has duplicate character. But it is unnecessary. If a substring s_{ij}s 
# ij
#   from index ii to j - 1j−1 is already checked to have no duplicate characters. We only need to check if s[j]s[j] is already in the substring s_{ij}s 
# ij
#  .
#         chars = [0] * 128
#         left = right = 0
#         res = 0
#         while right < len(s):
#             r = s[right]
#             chars[ord(r)] += 1

#             while chars[ord(r)] > 1:
#                 l = s[left]
#                 chars[ord(l)] -= 1
#                 left += 1

#             res = max(res, right - left + 1)

#             right += 1
#         return res


# Leetcode solution 2
# The above solution requires at most 2n steps. In fact, it could be optimized to require only n steps. Instead of using a set to tell if a character exists or not, we could define a mapping of the characters to its index. Then we can skip the characters immediately when we found a repeated character.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans


# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.