

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
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

def print_given_level(root,d):
    if root:
        if d==1:
            print(root.info),
        else:
            print_given_level(root.left,d-1)
            print_given_level(root.right,d-1)

def levelOrder(root):
	#Write code Here
    high=height(root)
    for i in range(high+2):
        print_given_level(root,i)


