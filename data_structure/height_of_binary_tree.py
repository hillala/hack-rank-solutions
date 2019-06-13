

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    if not root: 
        return -1
    else:  
        lDepth = height(root.left) 
        rDepth = height(root.right) 
        if (lDepth > rDepth): 
            return lDepth+1
        else: 
            return rDepth+1 
