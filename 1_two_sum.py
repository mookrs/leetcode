# https://leetcode.com/problems/two-sum/description/
class Solution1:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


s1 = Solution1()
print(s1.twoSum([2, 7, 11, 15], 9))


class Solution2:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for idx, num in enumerate(nums):
            nums_dict[num] = idx
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in nums_dict and nums_dict[complement] != idx:
                return [idx, nums_dict[complement]]


s2 = Solution2()
print(s2.twoSum([2, 7, 11, 15], 9))


class Solution3:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in nums_dict:
                return [nums_dict[complement], idx]
            nums_dict[num] = idx


s3 = Solution3()
print(s3.twoSum([2, 7, 11, 15], 9))
