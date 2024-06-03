import sys

N = int(sys.stdin.readline())
binary_tree = dict()
parent = dict()
for _ in range(N):
    node, left, right = map(int, sys.stdin.readline().split())
    binary_tree[node] = [left, right]
    if left != -1:
        parent[left] = node
    if right != -1:
        parent[right] = node

last_node = 1
while binary_tree[last_node][1] != -1:
    last_node = binary_tree[last_node][1]

node = 1
cnt = 0
visited = set([1])
while True:
    left = binary_tree[node][0]
    right = binary_tree[node][1]
    if left != -1 and left not in visited:
        visited.add(left)
        node = left
    elif right != -1 and right not in visited:
        visited.add(right)
        node = right
    elif node == last_node:
        break
    elif node in parent:
        node = parent[node]
    cnt += 1
print(cnt)