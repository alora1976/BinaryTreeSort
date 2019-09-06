# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:19:42 2019

@author: Lori
"""
#Binary Tree

class BTNode:
    def __init__(self, val=None, left=None, right= None):
        self.val=val
        self.left=left
        self.right=right
    def grow_left(self, val=None):
        if self.left != None:
            print ("This Node Already has Left Child")
        else:
            self.left = BTNode(val)
    def grow_right(self, val = None):
        if self.right != None:
            print("This Node Already has Right Child")
        else:
            self.right =BTNode(val)
    def print_tree(self):
        print('(', end='')
        if self.left != None:
            self.left.print_tree()
        print(self.val, end='')
        if self.right != None:
            self.right.print_tree()
        print(')', end= '')
    
class BTree:
    def __init__(self):
        self.root=None
def build_tree(tree,values):
        if tree.root != None:
            print("The Tree is not Empty")
        else:
            if len(values)== 0:
                print("The List is empty")
            else:
                tree.root =BTNode(values[0])
                for value in values [1:]:
                    current_node = tree.root
                    while current_node != None:
                        if value < current_node.val:
                            if current_node.left == None:
                                current_node.left = BTNode(value)
                                current_node=None
                            else:
                                current_node = current_node.left
                        else:
                            if current_node.right== None:
                                current_node.right = BTNode(value)
                                current_node=None
                            else:
                                current_node=current_node.right    
                                
                            
                            
                            
                            
                            
                            
my_tree = BTree()

build_tree(my_tree, [4,9,2,3,11,0,6,12])

my_tree.root.print_tree()