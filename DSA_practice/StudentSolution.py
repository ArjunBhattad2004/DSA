l=[]
class BTNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.parent=None

    def get_key(self):
        return self.key

    def set_key(self,key):
        self.key=key

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

class BT:
    def __init__(self):
        self.root=None

    def add(self,key):
        node=BTNode(key)
        
        if(self.root==None):
            self.root=node
            l.append([node.get_key()])
            return
        
        temp=self.root
        if(len(l)==1):
            l.append([node.get_key()])
            temp.set_left(node)
        if(len(l)==2):
            if(len(l[1])==1):
                temp.set_right(node)
                l[1].append(node.get_key())
            else:
                l.append([node.get_key])

    def get_cousins(self,node,c):
        for w in l:
            for w_ in w:
                



            
            

        

    def LCA(self,node1,node2):
        t1=node1
        t2=node2
        while t1!=t2:
            t3=t1
            t4=t2
            if(t1!=None):
                t1=t1.get_parent()
            if(t1==t4):
                return t4
            if(t1==node2):
                return node2
            if(t2!=None):
                t2=t2.get_parent()
            if(t2==t3):
                return t3
            if(t2==node1):
                return node1
        return t1            

        




if __name__=="__main__":
    T=BT()        
    n=int(input())        
    a=input()
    b=input()
    keys=a.split(' ')
    nd=b.split(' ')
    node1=BTNode(nd[0])
    node2=BTNode(nd[1])
    for key in keys:
       T.add(key)
    c=T.LCA(node1,node2)

    print(c)
    print(T.get_cousins(node1,c))
    print(T.get_cousins(node2,c))


    

                




