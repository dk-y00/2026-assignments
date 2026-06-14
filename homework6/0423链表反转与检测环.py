class DNode:
    """双向链表结点"""

    def __init__(self, data: str | int | float):
        self.data = data
        self.prev: DNode | None = None
        self.next: DNode | None = None


class DoublyLinkedList:
    """双向链表"""

    def __init__(self):
        self.first: DNode | None = None
        self.last: DNode | None = None

    def insert_at_end(self, value: str | int | float) -> None:
        """在末尾插入"""
        new_node = DNode(value)
        if not self.first:
            self.first = self.last = new_node
        else:
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node

    def remove_from_front(self) -> str | int | float | None:
        """从开头删除"""
        if not self.first:
            return None
        data = self.first.data
        self.first = self.first.next
        if self.first:
            self.first.prev = None
        else:
            self.last = None
        return data

    def reverse(self) -> None:
        """
        反转双向链表
        """
        if not self.first:
            return

        current = self.first
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev

        self.first, self.last = self.last, self.first

    def has_cycle(self) -> bool:
        """
        检测链表中是否存在环
        """
        if not self.first:
            return False

        slow = self.first
        fast = self.first

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False