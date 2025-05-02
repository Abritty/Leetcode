def remove_duplicates(nums):
    if not nums:
        return 0

    n = len(nums)
    current_index = 0

    for i in range(1, n):
        if nums[i] != nums[i-1]:
            current_index +=1
            nums[current_index] = nums[i]

    return current_index + 1

# Example usage
nums = [1, 1, 2, 2, 2,3, 3, 8, 8, 9]
length = remove_duplicates(nums)
print(f"Array after removing duplicates: {nums[:length]}") #[1, 2]
print(f"New length of the array: {length}") #2
