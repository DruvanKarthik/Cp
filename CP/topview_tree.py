class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.hd= 0 
def construct_Tree(node_list):
    root = Node(node_list[0])
    root.left = Node(node_list[1])
    root.right= Node(node_list[2])    
    root.left.left= Node(node_list[3])
    root.left.right= Node(node_list[4])
    root.right.left = Node(node_list[5])
    root.right.right = Node(node_list[6])
    return root

def topview(root):
    m = {}
    q=[]
    q.append(root)
    while len(q)>0:
        curr_node = q.pop(0)
        if curr_node.hd not in m:
            m[curr_node.hd] = curr_node.val
        if curr_node.left:
            curr_node.left.hd=curr_node.hd-1
            q.append(curr_node.left)
        if curr_node.right:
            curr_node.right.hd= curr_node.hd+1
            q.append(curr_node.right)
    print("Top View")
    for k in sorted(m):
        print(m[k],end=",")
        
#Driver code
node_list = ["A","B","C","D","E","F","G"]
root = construct_Tree(node_list)
topview(root)