# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # get height of left sub tree
        left_height = self.height(root.left)
        # get height of right sub tree
        right_height = self.height(root.right)

        # if the difference between left and right sub tree is greater than 1
        # then the tree is not balanced
        if abs(left_height - right_height) > 1:
            print("Tree is not balanced")
            return False
        
        # if the difference between left and right sub tree is less than 1
        # then the tree is balanced
        print("Tree is balanced")
        return True
    
    def height(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def printTree(self, root: TreeNode) -> None:
        if root is None:
            return
        print(root.val, end=' ')
        self.printTree(root.left)
        self.printTree(root.right)

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    # root.right.right.right = TreeNode(99)

    # new solution class
    sol = Solution()
    sol.isBalanced(root)

