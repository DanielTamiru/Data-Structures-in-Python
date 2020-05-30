from queue import Queue

class TreeNode :
    def __init__(self, val, children=[]) :
        self.val = val
        self.children = children
    
    def __repr__(self) :# recursive dfs traversal
        preorder_node_list = "<"
        def traverse(root):
            nonlocal preorder_node_list
            preorder_node_list += str(root.val) + ", "
            for node in root.children : 
                traverse(node)
        traverse(self)
        preorder_node_list = preorder_node_list[:-2]
        preorder_node_list += ">"
        return preorder_node_list

class BinTreeNode(TreeNode) :
    def __init__(self, val, left=None, right=None) :
            nodes = []
            if left :
                nodes.append(left) 
            if right :
                nodes.append(right) 
            super().__init__(val, nodes)


# Sample Binary Tree
four = BinTreeNode(4)
five = BinTreeNode(5)
two = BinTreeNode(2, four, five)
three =  BinTreeNode(3)
sample_bt = BinTreeNode(1, two, three)

###- Iterative Depth First Traversal -###

def dfs_iterative(root) :
    nodes = [root]
    while nodes != [] :
        top = nodes.pop()
        print(top.val)

        for node in reversed(top.children) :
            nodes.append(node)

#######- Breadth First/Level Order Traversals -#######

def bfs_iterative(root) :
    nodes = Queue()
    nodes.put(root)
    while nodes != [] :
        front = nodes.get()
        print(front.val)

        for node in front.children :
            nodes.put(node)