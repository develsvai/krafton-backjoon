class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(node):
    if node is None:
        return
    print(node.value, end="")
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value, end="")
    inorder(node.right)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value, end="")

def build_tree(n, node_info):
    tree = {}
    for info in node_info:
        root, left, right = info
        if root not in tree:
            tree[root] = Node(root)
        if left != '.':
            tree[left] = Node(left)
            tree[root].left = tree[left]
        if right != '.':
            tree[right] = Node(right)
            tree[root].right = tree[right]
    return tree['A']  # 'A'가 항상 루트 노드임

# 입력 처리
n = int(input())
node_info = [input().split() for _ in range(n)]

# 트리 구성
root = build_tree(n, node_info)

# 전위 순회, 중위 순회, 후위 순회 출력
preorder(root)
print()
inorder(root)
print()
postorder(root)
print()
