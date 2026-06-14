class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert(node.left, val)
        elif val > node.val:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert(node.right, val)

    def find_min(self, node):
        current = node
        while current and current.left:
            current = current.left
        return current

    def find_max(self, node):
        current = node
        while current and current.right:
            current = current.right
        return current

    def delete(self, val, strategy="successor"):
        self.root = self._delete(self.root, val, strategy)

    def _delete(self, node, val, strategy):
        if node is None:
            return None

        if val < node.val:
            node.left = self._delete(node.left, val, strategy)
        elif val > node.val:
            node.right = self._delete(node.right, val, strategy)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            if strategy == "predecessor":
                predecessor = self.find_max(node.left)
                node.val = predecessor.val
                node.left = self._delete(node.left, predecessor.val, strategy)
            else:
                successor = self.find_min(node.right)
                node.val = successor.val
                node.right = self._delete(node.right, successor.val, strategy)

        return node

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)

    def draw_tree(self):
        if self.root is None:
            print("树为空")
            return
        lines = []
        self._build_tree_string(self.root, 0, True, [], lines)
        for line in lines:
            print(line)

    def _build_tree_string(self, node, depth, is_right, prefix, lines):
        if node is None:
            return

        if node.right:
            self._build_tree_string(node.right, depth + 1, True,
                                    prefix + ("        " if is_right else "│       "), lines)

        connector = "└── " if is_right else "┌── "
        node_str = f"{prefix}{connector}{node.val}"
        lines.append(node_str)

        if node.left:
            self._build_tree_string(node.left, depth + 1, False,
                                    prefix + ("        " if is_right else "│       "), lines)


# ==================== 作业题1 ====================
print("=" * 50)
print("作业题1：构建 BST")
print("=" * 50)

bst = BST()
insert_seq = [50, 30, 70, 20, 40, 60, 80]

for val in insert_seq:
    bst.insert(val)

print("\n最终 BST 形态：")
bst.draw_tree()
print(f"\n中序遍历结果: {bst.inorder()}")

# ==================== 作业题2 ====================
print("\n" + "=" * 50)
print("作业题2：删除根结点 50")
print("=" * 50)

# 策略一：前驱
print("\n【策略一：中序前驱】")
bst1 = BST()
for val in insert_seq:
    bst1.insert(val)

print("\n删除前的树：")
bst1.draw_tree()

predecessor = bst1.find_max(bst1.root.left)
print(f"\n前驱: {predecessor.val}（左子树的最右结点）")

bst1.delete(50, strategy="predecessor")

print("\n删除后的树：")
bst1.draw_tree()
print(f"中序遍历: {bst1.inorder()}")

# 策略二：后继
print("\n【策略二：中序后继】")
bst2 = BST()
for val in insert_seq:
    bst2.insert(val)

print("\n删除前的树：")
bst2.draw_tree()

successor = bst2.find_min(bst2.root.right)
print(f"\n后继: {successor.val}（右子树的最左结点）")

bst2.delete(50, strategy="successor")

print("\n删除后的树：")
bst2.draw_tree()
print(f"中序遍历: {bst2.inorder()}")