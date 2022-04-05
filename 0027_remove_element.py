# https://leetcode.com/problems/remove-element/description/


class Solution1:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


nums, val = [0, 1, 2, 2, 3, 0, 4, 2], 2
s1 = Solution1()
print(nums, s1.removeElement(nums, val))


class Solution2:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1

        return i


nums, val = [0, 1, 2, 2, 3, 0, 4, 2], 2
s2 = Solution2()
print(nums, s2.removeElement(nums, val))
