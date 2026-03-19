from typing import Any, Iterable


class MySet:
    """自定义集合类，实现查询、插入、删除功能"""

    def __init__(self, iterable: Iterable[Any] = None):
        """
        初始化集合
        :param iterable: 可迭代对象，用于初始化集合元素
        """
        if iterable is None:
            self.elements = []
        else:
            # 去重
            self.elements = []
            for item in iterable:
                if item not in self.elements:
                    self.elements.append(item)

    def search(self, element: Any) -> bool:
        """
        查询元素是否在集合中
        :param element: 要查询的元素
        :return: 存在返回True，不存在返回False
        """
        return element in self.elements

    def insert(self, element: Any) -> bool:
        """
        向集合中插入元素
        :param element: 要插入的元素
        :return: 插入成功返回True，元素已存在返回False
        """
        if element not in self.elements:
            self.elements.append(element)
            return True
        return False

    def delete(self, element: Any) -> bool:
        """
        从集合中删除元素
        :param element: 要删除的元素
        :return: 删除成功返回True，元素不存在返回False
        """
        if element in self.elements:
            self.elements.remove(element)
            return True
        return False

