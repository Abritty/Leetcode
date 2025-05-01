def remove_duplicates(nums):
    if not nums:
        return 0

    n = len(nums)
    current_index = 1

    for i in range(1, n):
        if nums[i] != nums[i-1]:
            nums[current_index] = nums[i]
            current_index += 1
        print(current_index, i)

    return current_index  

# Example usage
nums = [1, 1, 2, 2, 2]
length = remove_duplicates(nums)
print(f"Array after removing duplicates: {nums[:length]}") #[1, 2]
print(f"New length of the array: {length}") #2
