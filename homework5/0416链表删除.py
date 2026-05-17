def delete_at_index(self, index: int) -> bool:
    """
    删除指定索引位置的节点

    时间复杂度：
    - 索引0（开头）：O(1)
    - 其他位置：O(N)

    :param index: 要删除的节点索引
    :return: 删除成功返回True，索引越界返回False
    """
    # 空链表情况
    if self.first_node is None:
        return False

    # 在开头删除
    if index == 0:
        self.first_node = self.first_node.next_node
        return True

    # 找到插入位置的前一个结点
    current_node = self.first_node
    current_index = 0

    # 每一轮while循环向右移动一个node
    # while循环结束的时候正好停在index-1
    while current_index < index - 1:
        if not current_node.next_node:
            return False  # 索引越界
        current_node = current_node.next_node
        current_index += 1

    # 循环结束后补充检查一次索引越界
    if not current_node.next_node:
        return False

    # 删除结点
    current_node.next_node = current_node.next_node.next_node

    return True


# 绑定方法
LinkedList.delete_at_index = delete_at_index