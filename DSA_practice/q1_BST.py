class BSTNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.left=None
        self.right=None
        self.parent=None

    def get_key(self):
        return self.key

    def set_key(self,key):
        self.key=key

    def get_value(self):
        return self.value

    def set_value(self,value):
        self.value=value

    def get_left(self):
        return self.left

    def set_left(self,node):
        self.left=node

    def get_right(self):
        return self.right

    def set_right(self,node):
        self.right=node        
    
    def get_parent(self):
        return self.parent

    def set_parent(self,node):
        self.parent=node

class BST:
    def __init__(self,root):
        self.root=root

    def insert_node(self,key):
        node=BSTNode(key,None)
        
        temp=self.root
        while temp is not None:
            if(key<temp.get_key()):
                temp=temp.get_left()
            elif(key>temp.get_key()):
                temp=temp.get_right()
            else:
                return
        temp=node        

if __name__=="__main__":
    T=BST(None)
    nn,nq=input(int())








        