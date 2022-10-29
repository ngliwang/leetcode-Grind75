# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        # base case / STOP condition 
        # when we reach the leaf node, then there's nothing to invert
        if root is None:
            return None

        # recurring case
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # swap the left and right subtree once its at bottom
        root.left = right
        root.right = left
        

    def printTree(self, root: TreeNode) -> None:
        if root is None:
            return
        print(root.val, end=' ')
        self.printTree(root.left)
        self.printTree(root.right)

if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    # print(root)
    # print(Solution().invertTree(root))
    Solution().printTree(Solution().invertTree(root))

