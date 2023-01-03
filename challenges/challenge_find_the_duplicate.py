def find_duplicate(nums):
    n = len(nums)
    if not all(isinstance(item, int) for item in nums) or not nums or n < 2:
        return False

    nums.sort()
    for index in range(n - 1):
        if nums[index] == nums[index + 1] and nums[index] >= 0:
            return nums[index]
    return False
