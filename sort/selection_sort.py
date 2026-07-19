

def selection_sort(nums: list[int]):
    """
    选择排序
    ---------------------
    时间复杂度: O(n^2)
    空间复杂度: O(1)
    非自适应排序
    非稳定排序
    原地排序
    """

    n = len(nums)
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if nums[j] < nums[k]:
                k = j
        nums[i], nums[k] = nums[k], nums[i]


if __name__ == '__main__':
    nums = [5, 6, 2, 1, 8, 0, 4, 3]
    selection_sort(nums)
    print(nums)
    