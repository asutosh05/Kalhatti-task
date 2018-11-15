class Node:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B):
        paths = []

        def pathSum_(root,sum_,path):
            if root.left is None and root.right is None:
                if sum_ - root.val==0:
                    paths.append(path+[root.val])
                return
            
            sum_-=root.val
            path=path+[root.val]
            if root.left is not None:
                pathSum_(root.left,sum_,path)
            if root.right is not None:
                pathSum_(root.right,sum_,path)
            
        
        if A is not None:
            pathSum_(A, B, [])
            
        return paths

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
sol= Solution()
print(sol.pathSum(root,7))
