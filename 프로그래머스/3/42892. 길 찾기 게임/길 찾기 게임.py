'''
연결 리스트를 통한 이진 트리 구현
x: value
y: level
z: key
'''
from sys import setrecursionlimit
setrecursionlimit(10000)

class Node:
    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
    
class BinaryTree():
    def __init__(self):
        self.root = None
    
    def add(self, key, value): # 이진 트리 노드 추가 코드
        def add_node(node, key, value):
            if value < node.value:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
                    
            
        if self.root is None:
            self.root = Node(key, value, None, None)
        else:
            add_node(self.root, key, value)
    
    def preorder(self, node, array): # 전위 순회
        if node != None:
            array.append(node.key)
            if node.left:
                self.preorder(node.left, array)
            if node.right:
                self.preorder(node.right, array)
    
    def postorder(self, node, array): # 후위 순회
        if node != None:
            if node.left:
                self.postorder(node.left, array)
            if node.right:
                self.postorder(node.right, array)
            array.append(node.key)

def solution(nodeinfo):
    
    for i in range(len(nodeinfo)): # key값 추가
        nodeinfo[i].append(i + 1)    
    
    nodeinfo.sort(key = lambda x: -x[1])
    tree = BinaryTree()
    for node in nodeinfo:
        key, value = node[2], node[0]
        tree.add(key, value)
    
    preorder_arr = []
    tree.preorder(tree.root, preorder_arr)
    postorder_arr = []
    tree.postorder(tree.root, postorder_arr)
    
    return [preorder_arr, postorder_arr]