from typing import Sequence, Any
def __init__(self, iterable: Sequence[Any]):
    """
    :param iterable: 有序数组初始化
    """
    self.iterable = list(iterable)
    self.len = len(self.iterable)


def insert(self, element: Any) -> None:
    """
    插入元素
    :param element: 待插入的元素
    """
    insert_index: int = 0

    # 找到插入位置
    for index, value in enumerate(self.iterable):
        if element > value:  # 找到第一个大于element的位置
            insert_index = index + 1
        else:
            break

    # 在找到的位置插入元素
    self.iterable.insert(insert_index, element)
    self.len += 1