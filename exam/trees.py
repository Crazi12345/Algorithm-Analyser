class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def arrayToTree(arr):
    root= TreeNode(arr[0])
    
