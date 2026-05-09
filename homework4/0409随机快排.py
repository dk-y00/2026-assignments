import random
from collections.abc import Sequence


class QuickSortRandom:
    """随机化快速排序，避免最坏情况"""

    def __init__(self, arr: Sequence[int | float]):
        self.arr: list[int | float] = list(arr)
        self.length: int = len(arr)

    def partition(self, left_index: int, right_index: int) -> int:
        """随机选择 pivot，将数组分成 [< pivot] [pivot] [> pivot]"""
        # 随机选择 pivot 索引
        pivot_idx = random.randint(left_index, right_index)
        pivot = self.arr[pivot_idx]

        # 将 pivot 暂时移到最左边（方便处理）
        self.arr[left_index], self.arr[pivot_idx] = self.arr[pivot_idx], self.arr[left_index]

        # 分区指针
        i = left_index + 1  # 当前扫描位置
        j = left_index  # 小于区的右边界

        while i <= right_index:
            if self.arr[i] < pivot:
                j += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            i += 1

        # 将 pivot 放回正确位置
        self.arr[left_index], self.arr[j] = self.arr[j], self.arr[left_index]
        return j

    def sort(self, left_index: int | None = None, right_index: int | None = None):
        """递归快速排序"""
        if left_index is None:
            left_index = 0
        if right_index is None:
            right_index = self.length - 1

        if right_index - left_index <= 0:
            return self.arr

        pivot_pos = self.partition(left_index, right_index)
        self.sort(left_index, pivot_pos - 1)
        self.sort(pivot_pos + 1, right_index)
        return self.arr


# 测试代码
if __name__ == "__main__":
    # 最坏情况测试（原本已排序的数组）
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    qs = QuickSortRandom(arr)
    print("原数组:", arr)
    print("排序后:", qs.sort())

    # 随机数组测试
    arr2 = [64, 25, 12, 22, 11, 33, 45, 78, 90, 5]
    qs2 = QuickSortRandom(arr2)
    print("随机数组排序后:", qs2.sort())