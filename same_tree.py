'''

@author: Eric

Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if (p == None) | (q == None):
            if (p == None) & (q == None):
                return True
            else:
                return False
        
        if (p.val == q.val):
            if (self.isSameTree(p.left, q.left)):
                if (self.isSameTree(p.right, q.right)):
                    return True
        
        return False

if __name__ == '__main__':
    nodeValue = [1,3,5,6]
    tree1 = []
    tree2 = []
    
    for val in nodeValue:
        tree1.append(TreeNode(val))
        tree2.append(TreeNode(val))

    tree1[0].left = tree1[1]
    tree1[0].right = tree1[3]
    tree1[1].right = tree1[2]

    tree2[0].left = tree2[1]
    tree2[0].right = tree2[3]
    tree2[1].right = tree2[2]
    
    solution = Solution()
    
    print solution.isSameTree(tree1[0], tree2[0])