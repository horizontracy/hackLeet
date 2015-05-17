'''
@author: Eric

Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == '__main__':
    nodeValue = [1,3,5,6]
    nodeList = []
    
    for val in nodeValue:
        nodeList.append(TreeNode(val))

    nodeList[0].left = nodeList[1]
    nodeList[0].right = nodeList[3]
    nodeList[1].right = nodeList[2]
    
    solution = Solution()
    
    print solution.maxDepth(nodeList[0])
    assert 3 == solution.maxDepth(nodeList[0])