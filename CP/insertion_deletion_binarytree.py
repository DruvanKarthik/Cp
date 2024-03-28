# create a queue and dequeue the root node, while the queue is not empty do the following
#dequeue  anode form the queue if the left child of the node is empty then insert it into the left node
#if the right node is empty then inset it into right node
#repeat the process untill the key is insrted int the binary tree
from collections import deque
class TreeNode:
    def __init__(self,key):
        self.left= None
        self.right = None
        self.key = key
def InorederTraversal(root):
    if root:
        InorederTraversal(root.left)
        print(root.key,end=" ")
        InorederTraversal(root.right)
def insert(root,key):
    if not root:
        return TreeNode(key)
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if not node.left:
            node.left = TreeNode(key)
            break
        else:
            queue.append(node.left)
        if not node.right:
            node.right = TreeNode(key)
            break
        else:
            queue.append(node.right)   
def delete_deepest(root,d_node):
    q = [root]
    while q:
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                 temp.right =None
                 return 
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                 temp.left =None
                 return 
            else:
                q.append(temp.left)
                
def deletion(root,key):
    if root is None:
        return None
    if root.left is None and root.right is None:
        if root.key == key:
            return None
        else:
            return root
    key_node = None
    q = [root]
    temp =None
    while q:
        temp = q.pop(0)
        if temp.key == key :
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x  = temp.key   
        delete_deepest(root,temp)
        key_node.key=x
    return root  
root = TreeNode(50)
root.left = TreeNode(30)
root.left.left =TreeNode(20)
root.left.right=TreeNode(90)
root.right = TreeNode(70)
root.right.right =TreeNode(80)
insert(root,60)
print("The indoder Traversal after insertion :")
InorederTraversal(root)
deletion(root,90)
print("\nAfter deletion:")
InorederTraversal(root)