# My first solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        # return early
        if not root:
            return []
        
        # initial node
        count = 0
        stock = {count: [root]}
        
        # transverse nodes level by level 
        while True:            
            # Get all nodes in a certain level in left to right order                
            nodes = stock.get(count, [])
            # print(nodes)
            
            # If no more nodes, the previous level was the deepest. We are done
            if len(nodes) == 0:
                break
            
            # If at least one node exist, Get their children from left to right
            count += 1
            stock[count] = []  # for the last level, we will have a redundent empty node list here
            for node in nodes:
                if node.left:
                    stock.update({count: stock[count] + [node.left]})
                if node.right:
                    stock.update({count: stock[count] + [node.right]})
        
        # get the node value in stock order
        result = []
        for level, nodes in stock.items():
            if len(nodes) != 0:
                result.append([n.val for n in nodes])

        return result
                
# My second solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def levelOrder(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#         """
        
#         # return early
#         if not root:
#             return []
        
#         # initialize
#         count = 0
#         result = []
#         queue = [[root]]
        
#         # transverse nodes level by level 
#         while True:            
#             # Get all nodes in a certain level in left to right order                
#             try:
#                 nodes = queue.pop(0)
#             except:
#                 nodes = []
#             # print(nodes)
            
#             # If no more nodes, the previous level was the deepest. We are done
#             if len(nodes) == 0:
#                 break
            
#             # If at least one node exist, Get their children from left to right
#             count += 1
#             node_values_this_level = []
#             nodes_next_level = []
#             for node in nodes:
#                 node_values_this_level.append(node.val)
#                 if node.left:
#                     nodes_next_level.append(node.left)
#                 if node.right:
#                     nodes_next_level.append(node.right)
                    
#             # append node values to result
#             if len(node_values_this_level) > 0:
#                 result.append(node_values_this_level)
            
#             if len(nodes_next_level) > 0:
#                 queue.append(nodes_next_level)

#         return result


            

