"""
AVL树作业
插入序列: [30, 20, 10, 25, 40, 35, 50]
"""


class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


def get_height(node):
    return node.height if node else 0


def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0


def update_height(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))


def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    update_height(y)
    update_height(x)
    return x


def left_rotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    update_height(x)
    update_height(y)
    return y


def insert(node, val, log):
    if not node:
        return AVLNode(val)

    if val < node.val:
        node.left = insert(node.left, val, log)
    elif val > node.val:
        node.right = insert(node.right, val, log)
    else:
        return node

    update_height(node)
    balance = get_balance(node)

    if balance > 1 and val < node.left.val:
        log.append(('LL', node.val))
        return right_rotate(node)

    if balance < -1 and val > node.right.val:
        log.append(('RR', node.val))
        return left_rotate(node)

    if balance > 1 and val > node.left.val:
        log.append(('LR', node.val))
        node.left = left_rotate(node.left)
        return right_rotate(node)

    if balance < -1 and val < node.right.val:
        log.append(('RL', node.val))
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node


def print_tree(node, prefix="", is_left=True):
    if not node:
        return
    bf = get_balance(node)
    print(prefix + ("├── " if is_left else "└── ") + f"{node.val}(BF={bf})")
    child_prefix = prefix + ("│   " if is_left else "    ")
    if node.left or node.right:
        print_tree(node.left, child_prefix, True)
        print_tree(node.right, child_prefix, False)


def inorder(node, res):
    if node:
        inorder(node.left, res)
        res.append(node.val)
        inorder(node.right, res)


seq = [30, 20, 10, 25, 40, 35, 50]
root = None

print("=" * 50)
print("插入序列:", seq)
print("=" * 50)

for i, val in enumerate(seq, 1):
    print(f"\n第{i}步：插入 {val}")
    print("-" * 40)
    log = []
    root = insert(root, val, log)

    if log:
        rtype, axis = log[0]
        print(f"失衡类型：{rtype}")
        print(f"旋转轴：{axis}")
        print("旋转后树形：")
    else:
        print("未发生失衡")
        print("当前树形：")

    print_tree(root)

print("\n" + "=" * 50)
print("最终AVL树")
print("=" * 50)
print_tree(root)

res = []
inorder(root, res)
print(f"\n中序遍历：{res}")
print(f"BST性质验证：{res == sorted(res)}")