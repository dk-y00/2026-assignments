"""
B-Tree 作业
3阶B-Tree (m=3)
插入序列: [10, 20, 5, 6, 12, 30, 25]
"""

class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf          # 是否为叶子结点
        self.keys = []            # 键值列表
        self.children = []        # 子结点列表


class BTree:
    def __init__(self, m=3):
        self.root = BTreeNode(leaf=True)
        self.m = m                # 阶数
        self.max_keys = m - 1     # 最多键数: 2
        self.min_keys = (m // 2) - 1 if m > 2 else 1  # 最少键数: 1

    def insert(self, key):
        root = self.root
        if len(root.keys) == self.max_keys:
            # 根结点已满，需要分裂
            new_root = BTreeNode(leaf=False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
            self._insert_non_full(self.root, key)
        else:
            self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            # 叶子结点：直接插入
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            # 非叶子：找到合适的子结点
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == self.max_keys:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent, i):
        # 分裂子结点
        m = self.m
        child = parent.children[i]
        new_child = BTreeNode(leaf=child.leaf)

        # 中间键的位置
        mid = m // 2 - 1 if m % 2 == 0 else m // 2
        # 对于 m=3，mid = 1（第2个键上升）

        # 将右半部分键移到新结点
        parent.keys.insert(i, child.keys[mid])
        new_child.keys = child.keys[mid + 1:]
        child.keys = child.keys[:mid]

        # 处理子结点
        if not child.leaf:
            new_child.children = child.children[mid + 1:]
            child.children = child.children[:mid + 1]

        parent.children.insert(i + 1, new_child)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            for i in range(len(node.keys)):
                if not node.leaf:
                    self._inorder(node.children[i], result)
                result.append(node.keys[i])
            if not node.leaf:
                self._inorder(node.children[-1], result)

    def print_tree(self):
        lines = []
        self._build_tree_string(self.root, 0, "", lines)
        for line in lines:
            print(line)

    def _build_tree_string(self, node, depth, prefix, lines):
        if not node:
            return

        # 当前结点的字符串表示
        node_str = "[" + ", ".join(str(k) for k in node.keys) + "]"

        # 打印当前结点
        if depth == 0:
            lines.append(node_str)
        else:
            lines.append(prefix + "├── " + node_str)

        # 递归打印子结点
        if not node.leaf:
            for i, child in enumerate(node.children):
                if i == len(node.children) - 1:
                    self._build_tree_string(child, depth + 1, prefix + "    ", lines)
                else:
                    self._build_tree_string(child, depth + 1, prefix + "│   ", lines)


# ==================== 执行 ====================
if __name__ == "__main__":
    btree = BTree(m=3)
    seq = [10, 20, 5, 6, 12, 30, 25]

    print("=" * 50)
    print("3阶B-Tree构建过程")
    print("插入序列:", seq)
    print("=" * 50)

    for i, key in enumerate(seq, 1):
        print(f"\n第{i}步: 插入 {key}")
        print("-" * 40)
        btree.insert(key)
        btree.print_tree()

    print("\n" + "=" * 50)
    print("最终B-Tree")
    print("=" * 50)
    btree.print_tree()

    print("\n中序遍历:", btree.inorder())
    print("BST性质验证:", btree.inorder() == sorted(btree.inorder()))