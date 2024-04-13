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
        hd= curr_node.hd 
        m[hd] = curr_node.val
        if curr_node.left:
            curr_node.left.hd=hd-1
            q.append(curr_node.left)
        if curr_node.right:
            curr_node.right.hd=hd+1
            q.append(curr_node.right)
    print("Bottom View")
    for k in sorted(m):
        print(m[k],end=",")
        
#Driver code
node_list = ["1","2","3","4","5","6","7"]
root = construct_Tree(node_list)
topview(root)