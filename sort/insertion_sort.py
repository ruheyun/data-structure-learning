

def insertion_sort(nums: list[int]):
    """
    插入排序
    ---------------------
    时间复杂度: O(n^2)
    空间复杂度: O(1)
    自适应排序
    稳定排序
    原地排序
    """

    n = len(nums)
    for i in range(1, n):
        temp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > temp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = temp


if __name__ == '__main__':
    nums = [5, 6, 2, 1, 8, 0, 4, 3]
    insertion_sort(nums)
    print(nums)
