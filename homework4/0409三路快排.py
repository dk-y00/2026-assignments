def partition_three_way(self, left_index: int, right_index: int) -> tuple[int, int]:
    """
    将 arr[left:right+1] 分成三部分
    返回 (lt, gt) 其中：
    - [left, lt-1]  < pivot
    - [lt, gt]      == pivot
    - [gt+1, right] > pivot
    """
    if left_index >= right_index:
        return (left_index, right_index)

    pivot = self.arr[left_index]  # 选第一个作为pivot
    lt = left_index  # arr[left+1 ... lt] < pivot
    i = left_index + 1  # 当前扫描位置
    gt = right_index  # arr[gt ... right] > pivot

    while i <= gt:
        if self.arr[i] < pivot:
            self.arr[lt], self.arr[i] = self.arr[i], self.arr[lt]
            lt += 1
            i += 1
        elif self.arr[i] > pivot:
            self.arr[i], self.arr[gt] = self.arr[gt], self.arr[i]
            gt -= 1
        else:  # == pivot
            i += 1

    return (lt, gt)