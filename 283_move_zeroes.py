# https://leetcode.com/problems/move-zeroes/description/
class Solution1:
    # Space Complexity : O(n)
    # Time Complexity: O(n)
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ans = []
        for num in nums:
            if num != 0:
                ans.append(num)

        for _ in range(len(ans), len(nums)):
            ans.append(0)

        for i in range(len(nums)):
            nums[i] = ans[i]


nums = [0, 1, 0, 3, 12]
s1 = Solution1()
s1.moveZeroes(nums)
print(nums)


class Solution2:
    # Space Complexity : O(1)
    # Time Complexity: O(n)
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        last_non_zero_found_at = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_found_at] = nums[i]
                last_non_zero_found_at += 1

        for i in range(last_non_zero_found_at, len(nums)):
            nums[i] = 0


nums = [0, 1, 0, 3, 12]
s2 = Solution2()
s2.moveZeroes(nums)
print(nums)


class Solution3:
    # Space Complexity : O(1)
    # Time Complexity: O(n)
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        last_non_zero_found_at = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != last_non_zero_found_at:
                    nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
                last_non_zero_found_at += 1


nums = [0, 1, 0, 3, 12]
s3 = Solution3()
s3.moveZeroes(nums)
print(nums)
