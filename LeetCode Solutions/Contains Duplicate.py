#https://leetcode.com/problems/contains-duplicate/description/

def containsDuplicate(nums):
    seen = set(nums)
    if len(seen) != len(nums):
        return True
    return False


def containsDuplicate1(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False

