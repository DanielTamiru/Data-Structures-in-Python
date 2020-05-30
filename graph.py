###- Iterative Depth First Traversal -###

def dfs_iterative(root) :
    nodes, visited = [root], set()
    while nodes != [] :
        top = nodes.pop()
        print(top.val)
        visited.add(top)

        for node in reversed(top.children) :
            if node not in visited :
                nodes.append(node)

#######- Breadth First/Level Order Traversals -#######

def bfs_iterative(root) :
    nodes, visited = Queue(), set()
    nodes.put(root)
    while nodes != [] :
        front = nodes.get()
        print(front.val)
        visited.add(front)

        for node in front.children :
            if node not in visited :
                nodes.put(node)