# -*- coding: utf-8 -*-
"""
CECS 451: Lab #3: Tree Class
@author: James Rozsypal
"""

class Tree(object):
    
    def __init__(self):
        self.node_dict = {}
        self.num_node = 0
        self.root = None
    
    def add_node(self, node_id, parent_id):
        
        if len(parent_id) == 0:
            parent = None
            new_n = Node(node_id, parent)
            self.root = new_n
        else:
            parent = self.node_dict[parent_id]
            new_n = Node(node_id, parent)
            parent.add_child(node_id, new_n)
            
        self.node_dict[node_id] = new_n
        self.num_node += 1
            
    
    def get_node(self, node_id):
        if node_id in self.node_dict:
            return self.node_dict[node_id]
        else:
            return None
    
    
    def get_nodes(self):
        return self.node_dict.keys()
    
    
    def DFS_Helper(self, root):
        for n in root.children:
            if n.visited == False:
                self.DFS_Helper(n)
                n.visited == True
        
        print(root.get_id())
        
        return 
    
    
    def DFS_Traversal(self):
        self.DFS_Helper(self.root)

# =============================================================================
# END OF TREE/START OF NODE
# =============================================================================

class Node:
    
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.visited = False
        self.children = []
    
    
    def add_child(self, child_id, child_node):    
        if child_id not in self.children:
            self.children.append(child_node)
    
    
    def get_children_node(self):
        return self.children
    
    
    def get_parent(self):
        return self.parent
    
    
    def get_id(self):
        return self.name
    
    
# =============================================================================
# END OF NODE/START OF MAIN
# =============================================================================


class main():
    
    t = Tree()
    
    t.add_node('X', "")
    t.add_node('Q', 'X')
    t.add_node('F', 'X')
    t.add_node('D', 'X')
    t.add_node('C', 'Q')
    t.add_node('N', 'Q')
    t.add_node('R', 'Q')
    
    t.DFS_Traversal()
    