#https://leetcode.com/problems/top-k-frequent-elements/description/
from collections import defaultdict
from doctest import debug
from email.policy import default


class Solution:
    def topKFrequent(self, nums, k):
        ans=defaultdict(int)
        final=set()
        for i in nums:
            ans[i]+=1
        return final




solution = Solution()
num=[1,1,1,2,2,3]
k=2
print(solution.topKFrequent(num,k))