class InsertItem:
    def __init__(self, iterable: Iterable[Any]):
        self.iterable = list(iterable)

    def insert(self, element: Any, index_to_insert: int) -> list[Any]:
        length_of_iterable = len(self.iterable)
        self.iterable.append("")
        for i in range(length_of_iterable, index_to_insert, -1):
            self.iterable[i] = self.iterable[i - 1]
        self.iterable[index_to_insert] = element
        return self.iterable

    def delete(self, index_to_delete: int) -> list[Any]:
        """
        删除指定索引的元素
        :param index_to_delete: 要删除的元素的索引
        :return: 删除后的列表
        """
        length_of_iterable = len(self.iterable)
        for i in range(index_to_delete, length_of_iterable - 1):
            self.iterable[i] = self.iterable[i + 1]
        self.iterable.pop()
        return self.iterable