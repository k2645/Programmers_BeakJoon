import sys

N = int(sys.stdin.readline())
binary_tree = dict()

for _ in range(N):
    node, left, right = sys.stdin.readline().split()
    binary_tree[node] = [left, right]

def preorder(tree, node):
    if node in tree:
        print(node, end='')
        for n in tree[node]:
            preorder(tree, n)

def inorder(tree, node):
    if node in tree:
        inorder(tree, tree[node][0])
        print(node, end='')
        inorder(tree, tree[node][1])

def postorder(tree, node):
    if node in tree:
        for n in tree[node]:
            postorder(tree, n)
        print(node, end='')

preorder(binary_tree, 'A')
print()
inorder(binary_tree, 'A')
print()
postorder(binary_tree, 'A')