def sort_the_list(arr):
    nums = arr.copy()
    for i in range(len(nums)):
        for j in range(0, len(nums)-i-1):
            if nums[j] < nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


def find_nth_largest(list, n):
    largest_number = sort_the_list(list)
    return largest_number[n-1]

nums = [10, 2, 8, 6, 7]
n = 2
print(f"{n}th largest element is:", find_nth_largest(nums, n))
