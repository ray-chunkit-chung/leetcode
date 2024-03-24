# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    # third trial
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # Check nodes one by one. Then recursive check children.
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p and q:
            if p.val != q.val:
                return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return 'wtf?!?!?'


# first trial fails
#     def isSameTree(self, a, b):
#         """
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: bool
#         """

#         if a is None and b is None:
#             return True
#         if a is None and b is not None:
#             return False
#         if a is not None and b is None:
#             return False
        
#         if a is not None and b is not None:
#             if a.left is None and b.left is not None:
#                 return False
#             if a.left is not None and b.left is None:
#                 return False
#             if a.left is not None and b.left is not None:
#                 return self.isSameTree(a.left, b.left)

#             if a.val != b.val:
#                 return False

#             if a.right is None and b.right is not None:
#                 return False
#             if a.right is not None and b.right is None:
#                 return False
#             if a.right is not None and b.right is not None:
#                 return self.isSameTree(a.right, b.right)
            
#             return True
        
#         return 'wtf?!?!?'

# second trial in a stupid way, still fails
#     def isSameTree(self, p, q):
    
#         # Keep checking left node, append any values available, then right node, until everything is None. 
#         def transverse(node, result):        
#             if not node:
#                 return
#             transverse(node.left, result)
#             result.append(node.val)
#             transverse(node.right, result)
#             return
        
#         # Check if the whole lists equal
#         result_p = []
#         result_q = []
#         transverse(p, result_p)
#         transverse(q, result_q)
        
#         return result_p == result_q
        