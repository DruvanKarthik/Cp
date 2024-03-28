class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
def preorderTraversal(root):
    if root:
        print(root.data,end=" ")
        preorderTraversal(root.left)
        preorderTraversal(root.right)
def InorederTraversal(root):
    if root:
        InorederTraversal(root.left)
        print(root.data,end=" ")
        InorederTraversal(root.right)
def PostorderTraversal(root):
    if root:
        PostorderTraversal(root.left)
        PostorderTraversal(root.right)
        print(root.data,end=" ")
        
#driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right=Node(5)
root.right.left = Node(6)

print("Inorder Traversal:",end=' ')
InorederTraversal(root)
print("\nPost Order Traversal:",end=" ")
PostorderTraversal(root)
print("\nPreorder traversal",end=" ")
preorderTraversal(root)

#LEvel order Traversal

class TreeNode:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right=None

def level_order_traversal(root):
    if root is None:
        return 
    queue = [root]
    while queue:
        current_level = []
        level_size = len(queue)
        for _ in range(level_size):
            node  = queue.pop(0)
            current_level.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(*current_level,end=" ")
root  = TreeNode(1)
root.left=TreeNode(2)
root.right = TreeNode(3)
root.left.left =TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right =TreeNode(7)
 
print("\nLevel Order Traversal:",end=" ")
level_order_traversal(root)