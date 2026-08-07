
nums = [7, 3, 9, 1]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-2, -1, -1):

        for j in range(0, i+1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

bubble_sort(nums)
print(nums)