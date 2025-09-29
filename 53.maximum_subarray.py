def max_subarray(nums):
    if not nums:
            return 0

    current_max = nums[0]
    global_max = nums[0]

    for num in nums[1:]:
        current_max = max(num, current_max + num)
        global_max = max(global_max, current_max)

    return global_max

# Example usage
if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Maximum Subarray Sum:", max_subarray(nums))
