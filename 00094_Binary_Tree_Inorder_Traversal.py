# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        result = []

        # Keep checking left node, append any values available, then right node, until everything is None. 
        def transverse(node):        
            if not node:
                return
            transverse(node.left)
            result.append(node.val)
            transverse(node.right)
            return
        
        transverse(root)
        
        return result

    
# Approach 1: Recursive Approach
# The first method to solve this problem is using recursion. This is the classical method and is straightforward. We can define a helper function to implement recursion.
# class Solution {
#     public List<Integer> inorderTraversal(TreeNode root) {
#         List<Integer> res = new ArrayList<>();
#         helper(root, res);
#         return res;
#     }

#     public void helper(TreeNode root, List<Integer> res) {
#         if (root != null) {
#             helper(root.left, res);
#             res.add(root.val);
#             helper(root.right, res);
#         }
#     }
# }  

# Approach 2: Iterating method using Stack
# The strategy is very similiar to the first method, the different is using stack.
# Keep stacking left node, and then right node. If no child, pop the stack to get value. Until node and stack are empty
# public class Solution {
#     public List<Integer> inorderTraversal(TreeNode root) {
#         List<Integer> res = new ArrayList<>();
#         Stack<TreeNode> stack = new Stack<>();
#         TreeNode curr = root;
#         while (curr != null || !stack.isEmpty()) {
#             while (curr != null) {
#                 stack.push(curr);
#                 curr = curr.left;
#             }
#             curr = stack.pop();
#             res.add(curr.val);
#             curr = curr.right;
#         }
#         return res;
#     }
# }


# Approach 3: Morris Traversal
# In this method, we have to use a new data structure-Threaded Binary Tree, and the strategy is as follows:
# If current node has left node, put the current node at the rightmost child of the left node.  


# Step 1: Initialize current as root

# Step 2: While current is not NULL,
# If current does not have left child
#     a. Add current’s value
#     b. Go to the right, i.e., current = current.right
# Else
#     a. In current's left subtree, make current the right child of the rightmost node
#     b. Go to this left child, i.e., current = current.left


    
# class Solution {
#     public List<Integer> inorderTraversal(TreeNode root) {
#         List<Integer> res = new ArrayList<>();
#         TreeNode curr = root;
#         TreeNode pre;
#         while (curr != null) {
#             if (curr.left == null) {
#                 res.add(curr.val);
#                 curr = curr.right; // move to next right node
#             } else { // has a left subtree
#                 pre = curr.left;
#                 while (pre.right != null) { // find rightmost
#                     pre = pre.right;
#                 }
#                 pre.right = curr; // put cur after the pre node
#                 TreeNode temp = curr; // store cur node
#                 curr = curr.left; // move cur to the top of the new tree
#                 temp.left = null; // original cur left be null, avoid infinite loops
#             }
#         }
#         return res;
#     }
# }
    
