#https://leetcode.com/problems/group-anagrams/description/
from collections import defaultdict
from itertools import count

class Solution:
    def groupAnagrams(self, strs):
        ans = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
               count[ord(c)-ord('a')] =+1

            ans[tuple(count)].append(s)

        return ans.values()


solution = Solution()
arr=["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams(arr))