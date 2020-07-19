from queue import Queue
from math import log

#generators
def nodes_sorted(root) :
    if not root :
        raise StopIteration
    nodes = []

    while True :
        while root:
            nodes.append(root)
            root = root.left

        if not nodes : break
        curnode = nodes.pop()
        yield curnode.val
        root = curnode.right

def nodes_byLevel(root) :
    if not root: 
        raise StopIteration
    nodes = [root]
    while nodes :
        curnode = nodes.pop()
        if curnode :
            yield curnode.val
            nodes.append(curnode.right)
            nodes.append(curnode.left)
        else :
            yield False # no node

#functions
def toSortedList(root):
    lst = []
    for node_value in nodes_sorted(root) : lst.append(node_value)
    return lst

def balance(root) :
    lst = toSortedList(root)

    def place_node(front, back) :
        if front == back : return None
        #nonlocal lst
        middle = (front + back) // 2
        
        new_node = BST_Node(lst[middle], place_node(front, middle), place_node(middle + 1, back), back - front)
        return new_node
    return place_node(0, len(lst))

def left_balance(root) :
    lst = toSortedList(root)

    def place_node(front, back) :
        count = back - front
        node = None
        
        if count == 0 : pass
        elif count == 1 : 
            node = BST_Node(lst[front])
        elif count == 2 :
            node = BST_Node(lst[back - 1], None, None, 2)
            node.left = place_node(front, back - 1)
        else :
            max_middle_count = 2**(int(log(count, 2))) - 1 # node count of complete levels
            middle_count = (count - max_middle_count) + (max_middle_count//2) # middle count is half of complete + last incomplete level count
            if middle_count > max_middle_count: middle_count = max_middle_count

            middle = front + middle_count
            node = BST_Node(lst[middle], None, None, count)
            
            node.left = place_node(front, middle)
            node.right = place_node(middle + 1, back)

        return node
    return place_node(0, len(lst))
            
#----------------------

class BST_Node:
    #the root node represents the whole tree
    def __init__(self, val=0, left=None, right=None, count=1) :
        self.val = val
        self.left = left
        self.right = right
        self.count = count
    
class BST:
    def __init__(self, root=None) :
        self.root = root
    # Poor attempt. Printing vertically is difficult because numbers take up an unpredictable amount of space
    # It is useful for debuggging when used with just numbers 0 through 9
    #// def __repr__(self) :
    #//     levels = int(log(self.root.count, 2)) + 1
    #//     row_count, max_count = 2*levels - 1, 2**levels - 1

    #//     diagram = []
    #//     for _ in range(row_count): diagram.append(max_count * [" "])

    #//     def draw_nodes(node, level, front, back) :
    #//         if node and front <= back:
    #//             #nonlocal diagram
    #//             middle = (front + back) // 2
    #//             if level == 0 or level % 2 == 0 :
    #//                 diagram[level][middle] = str(node.val)
    #//                 draw_nodes(node.left, level + 1, front, middle - 1)
    #//                 draw_nodes(node.right, level + 1, middle + 1, back)
    #//             else :
    #//                 draw_nodes(node, level + 1, front, back)
    #//     draw_nodes(self.root, 0, 0, max_count)
        
    #//     drawing = ''
    #//     for i, row in enumerate(diagram) :
    #//         line = "".join(row)
    #//         if i < len(diagram) - 1 : line += '\n'
    #//         drawing += line
    #//     return drawing
    

    def contains(self, target) :
        root = self.root
        while root :
            if root.val == target :
                return True
                
            if root.val < target :
                root = root.right
            else :
                root = root.left
        return False
    
    def insert(self, k) :
        if self.contains(k) : return
        
        depth = 1
        parent, node = None, self.root
        while node :
            if node.val == k : return
            
            parent = node
            parent.count += 1
            node = node.left if k < node.val else node.right
            depth += 1
            
        if parent == None : return
        elif k < parent.val :
            parent.left = BST_Node(k)
        else :
            parent.right = BST_Node(k)

        #balance
        min_height = int(log(self.root.count, 2)) + 1
        if depth > min_height : 
            self.root = balance(self.root)
    
    def remove(self, k) :
        parent, node = None, self.root
        depth, height = 1, int(log(self.root.count, 2)) + 1
        isLeftChild = None
        #find it
        while node :
            if node.val == k : break
            parent = node
            depth += 1
            if node.val < k :
                node = node.right
                isLeftChild = False
            else :
                node = node.left
                isLeftChild = True
        if not node : return
        
        
        if not node.right : #check if missing a left child
            if isLeftChild : parent.left = node.left
            else :  parent.right = node.left
        #check if missing a right child
        elif not node.left :
            if isLeftChild : parent.left = node.right
            else :  parent.right = node.right  
        #find next largest node and it's parent
        else :
            next_node, parent_of_next = node.right, None
            depth += 1
            while next_node.left:
                next_node.count -= 1
                parent_of_next = next_node
                next_node = next_node.left
                depth += 1
            node.val = next_node.val #replace value
            node.count -= 1
            #remove next largest
            if parent_of_next :
                parent_of_next.left = next_node.right 
            else : node.right = next_node.right
            depth += 1
        
        #balance
        if depth < height : 
            self.root = balance(self.root)   


