import heapq


class MedianFinder:
    def __init__(self):
        self.left = []   # 大顶堆（存负数）
        self.right = []  # 小顶堆

    def addNum(self, num: int) -> None:
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        # 平衡两堆大小
        if len(self.left) > len(self.right) + 1:
            moved = -heapq.heappop(self.left)
            heapq.heappush(self.right, moved)
        elif len(self.right) > len(self.left):
            moved = heapq.heappop(self.right)
            heapq.heappush(self.left, -moved)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        else:
            return float(-self.left[0])


# 测试
mf = MedianFinder()
nums = [3, 1, 4, 1, 5]

for num in nums:
    mf.addNum(num)
    print(f"插入 {num}, 中位数: {mf.findMedian()}")