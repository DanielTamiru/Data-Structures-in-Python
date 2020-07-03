from queue import Queue

class TreeNode :
    #Requires no repeated nodes. Otherwise, this doubles as a general graph type
    def __init__(self, val, children=[]) :
        self.val = val
        self.children = children
    
    def __repr__(self) :# recursive dfs traversal
        node_list, nodes = [], [self]
        while nodes != [] :
            top = nodes.pop()
            node_list.append(top)

            for node in reversed(top.children) :
                nodes.append(node)
        return node_list

class BinTreeNode(TreeNode) :
    def __init__(self, val, left=None, right=None) :
            nodes = []
            if left :
                nodes.append(left) 
            if right :
                nodes.append(right) 
            TreeNode.__init__(self, val, nodes)


#// Sample Binary Tree
#//four = BinTreeNode(4)
#//five = BinTreeNode(5)
#//two = BinTreeNode(2, four, five)
#//three =  BinTreeNode(3)
#//sample_bt = BinTreeNode(1, two, three)

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

######- Useful Functions -########

def displayRows(root) :
        res = []
        queue, level_size = Queue(), 0
        queue.put(root)
        #traverse while keeping track of layers with counter
        while not queue.empty() :
            node = queue.get() 
            if level_size == 0:
                res.append([node.val])
                level_size = queue.qsize()
            else :
                res[-1].append(node.val)
                level_size -= 1
            
            for child in node.children :
                queue.put(child)

        print(res)

def tree_average(root) :
    '''
    requires numeric node values
    '''
    nodes, node_total, val_total = [root], 0, 0
    while nodes :
        curnode = nodes.pop()
        node_total += 1
        val_total += curnode.val

        for child in curnode.children :
            nodes.append(child)
    return val_total / node_total

def levelAverages(root) :
    '''
    requires numeric node values
    '''
    lvl_averages = []

    q = Queue()
    q.put(root)
    lvl_size, lvl_total = 1, 0
    while not q.empty() :
        for _ in range(lvl_size) :
            node = q.get()
            lvl_total += node.val

            for child in node.children :
                q.put(child)
                
        lvl_averages.append(lvl_total / lvl_size)
        lvl_size, lvl_total = q.qsize(), 0 #next levels size and reset level sum
        
    return lvl_averages

def tree_paths(root) :
    #trees are acyclic so each node in a tree represents its own path
    #this function retuns all paths that end with leaf nodes
    res = []
    if not root :
        return res
    
    nodes = [(root, str(root.val))] # (0: node, 1: string path to node)
    while nodes:
        curnode = nodes.pop()
        
        if not curnode[0].children : #if leaf node
            res.append(curnode[1])
        else : # otherwise
            for child in reversed(curnode[0].children) :
                nodes.append((child, curnode[1] + "->" + str(child.val)))
    return res

def maxDepth(root) :
    if not root:
        return 0
    depth = 1

    def traverse(node, level) :
        nonlocal depth
        if level > depth :
            depth = level
        for child in node.children:
            traverse(child, level + 1)
    traverse(root, 1)
    return depth