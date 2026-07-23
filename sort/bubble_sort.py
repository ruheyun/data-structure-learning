

def bubble_sort(nums: list[int]):
    """
    冒泡排序
    ---------------------
    时间复杂度: O(n^2)
    空间复杂度: O(1)
    自适应排序
    稳定排序
    原地排序
    """

    n = len(nums)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    
def bubble_sort_with_flag(nums: list[int]):
    """
    冒泡排序--标志优化
    """

    n = len(nums)
    for i in range(n - 1, 0, -1):
        flag = True
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = False
        if flag:
            break


if __name__ == '__main__':
    nums = [5, 6, 2, 1, 8, 0, 4, 3]
    bubble_sort_with_flag(nums)
    print(nums)
    