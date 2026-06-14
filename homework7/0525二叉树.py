class TreeNode:
    """二叉树结点（链表结构）"""

    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def build_tree_from_level_order(arr):
    """构建二叉树"""
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = [root]
    i = 1

    while queue and i < len(arr):
        node = queue.pop(0)

        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root


def print_tree(node, level=0, prefix="根: "):
    """打印树的形态"""
    if node is None:
        return
    print(" " * (level * 4) + prefix + str(node.val))
    if node.left or node.right:
        if node.left:
            print_tree(node.left, level + 1, "左子: ")
        else:
            print(" " * ((level + 1) * 4) + "左子: None")
        if node.right:
            print_tree(node.right, level + 1, "右子: ")
        else:
            print(" " * ((level + 1) * 4) + "右子: None")


# 执行
arr = [10, 5, 15, 3, 7, None, 20]
root = build_tree_from_level_order(arr)
print_tree(root)