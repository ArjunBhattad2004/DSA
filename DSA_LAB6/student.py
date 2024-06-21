class HybridNode:
    def __init__(self, key, element):
        self.key = key  # Key
        self.element = element  # Element
        self.parent = None  # Parent node
        self.left_child = None  # Left child node
        self.right_child = None  # Right child node
        self.next_node = None  # Next node in the linked list
        self.color = 'black' # "red" or "black"
        self.mru_objs= [MRU(key,"Chapter1",0),MRU(key,"Chapter2",0),MRU(key,"Chapter3",0)]
        

    def get_key(self):
        return self.key
    
    def set_key(self,key):
        self.key=key

    def get_element(self):
        return self.element
    
    def set_element(self,element):
        self.element=element

    def get_parent(self):
        return self.parent
    
    def set_parent(self,node):
        self.parent=node

    def get_left_child(self):
        return self.left_child
    
    def set_left_child(self,node):
        self.left_child=node

    def get_right_child(self):
        return self.right_child
    
    def set_right_child(self,node):
        self.right_child=node

    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self,node):
        self.next_node=node

    def get_color(self):
        return self.color  

    def set_color(self,color):
        self.color=color 
         
    def recolor(self):
        if(self.color=='red'):
            self.color='black'
        if(self.color=='black'):
            self.color='red' 

    def get_mru_objs(self):
        return self.mru_objs

    def append_mru_obj(self,mru_obj):
        self.mru_objs.append(mru_obj)               


class RedBlackTree:
    def __init__(self):
        self.root = None  # Root node
        

    def insert(self, key, element):  
        # Implement Red-Black Tree insertion
        new_node = HybridNode(key, element)
        if(element=="Chapter1"):           
            a=new_node.get_mru_objs()[0]
            a.set_count(a.get_count()+1)
        if(element=="Chapter2"):
            b=new_node.get_mru_objs()[1]
            b.set_count(b.get_count()+1)
        if(element=="Chapter3"):
            c=new_node.get_mru_objs()[2]
            c.set_count(c.get_count()+1)        
        exist_node=self.search(key)
        if((exist_node!=None)):
            if(element=="Chapter1"):
              a=exist_node.get_mru_objs()[0]
              a.set_count(a.get_count()+1)
            if(element=="Chapter2"):
              b=exist_node.get_mru_objs()[1]
              b.set_count(b.get_count()+1)
            if(element=="Chapter3"):
              c=exist_node.get_mru_objs()[2]
              c.set_count(c.get_count()+1)


            # if exist_node.get_element()!=element:
            #     new_mru_obj=MRU(key,element,1)
            #     exist_node.append_mru_obj(new_mru_obj)
            # else:
            #     exmru_objs=exist_node.get_mru_objs()
            #     for mru_obj in exmru_objs:
            #         if(mru_obj.get_chapter_name()==element):
            #             mru_obj.set_count(mru_obj.get_count()+1)
            #         else:
            #             continue    
       
        else:
            if self.root is None:
            # Case 1: Inserting the root node
              new_node.color = 'black'
              self.root = new_node
            else:
            # Case 2: Insert as a red node
              new_node.color='red'
              self._insert_recursive(self.root, new_node)
              self._fix_violation(new_node)
    
    def _insert_recursive(self, current, new_node):        
        if new_node.get_key() < current.get_key():
            if current.get_left_child() is None:
                new_node.set_parent(current)
                current.set_left_child(new_node)
            else:
                self._insert_recursive(current.get_left_child(), new_node)
        else:
            if current.get_right_child() is None:
                new_node.set_parent(current)
                current.set_right_child(new_node)
            else:
                self._insert_recursive(current.get_right_child(), new_node)

    def _fix_violation(self, node):
        while node != self.root and node.get_parent().get_color() == 'red':
            if node.get_parent() == node.get_parent().get_parent().get_left_child():
                uncle = node.get_parent().get_parent().get_right_child()
                if uncle and uncle.get_color() == 'red':
                    # Case 1: Recoloring
                    node.get_parent().set_color('black')
                    uncle.set_color('black')
                    node.get_parent().get_parent().set_color('red')
                    node = node.get_parent().get_parent()
                else:
                    if node == node.get_parent().get_right_child():
                        # Case 2: Left rotation
                        node = node.get_parent()
                        self.left_rotate(node)
                    # Case 3: Right rotation and recoloring
                    node.get_parent().set_color('black')
                    node.get_parent().get_parent().set_color('red')
                    self.right_rotate(node.get_parent().get_parent())
            else:
                uncle = node.get_parent().get_parent().get_left_child()
                if uncle and uncle.get_color() == 'red':
                    # Case 1: Recoloring
                    node.get_parent().set_color('black')
                    uncle.set_color('black')
                    node.get_parent().get_parent().set_color('red')                   
                    node = node.get_parent().get_parent()
                else:
                    if node == node.get_parent().get_left_child():
                        # Case 2: Right rotation
                        node = node.get_parent()
                        self.right_rotate(node)
                    # Case 3: Left rotation and recoloring
                    node.get_parent().set_color('black')
                    node.get_parent().get_parent().set_color('red')                   
                    self.left_rotate(node.get_parent().get_parent())
        self.root.color = 'black'
    
    def left_rotate(self, node):
        right_child = node.get_right_child()
        node.set_right_child(right_child.get_left_child())
        if right_child.get_left_child():
            right_child.get_left_child().set_parent(node)
        right_child.set_parent(node.get_parent())
        if not node.get_parent():
            self.root = right_child
        elif node == node.get_parent().get_left_child():
            node.get_parent().set_left_child(right_child)
        else:
            node.get_parent().set_right_child(right_child)
        right_child.set_left_child(node)
        node.set_parent(right_child)

    def right_rotate(self, node):
        left_child = node.get_left_child()
        node.set_left_child(left_child.get_right_child())
        if left_child.get_right_child():
            left_child.get_right_child().set_parent(node)
        left_child.set_parent(node.get_parent())
        if not node.get_parent():
            self.root = left_child
        elif node == node.get_parent().get_right_child():
            node.get_parent().set_right_child(left_child)
        else:
            node.get_parent().set_left_child(left_child)
        left_child.set_right_child(node)
        node.set_parent(left_child)

    def delete(self, key):
        # Implement Red-Black Tree deletion
        
        node_to_delete = self._search(self.root, key)
        if node_to_delete:
            self._delete_node(node_to_delete)

    def _delete_node(self, node):
        if node == None:
            return

        # Fix tree properties after deleting the node
        if node.get_color() == 'red':
            self._replace_node(node, None)
        else:
            self._delete_node_fixup(node)
            if node == self.root:
                self.root = None
            else:
                self._replace_node(node, None)

    def _replace_node(self, node, replacement):
        if node.get_parent() is None:
            self.root = replacement
        else:
            if node == node.get_parent().left:
                node.get_parent().left = replacement
            else:
                node.get_parent().right = replacement
        if replacement:
            replacement.parent = node.get_parent()

    def _delete_node_fixup(self, node):
        while node != self.root and node.get_color() == 'black':
            if node == node.get_parent().left:
                sibling = node.get_parent().right
                if sibling.get_color() == 'red':
                    sibling.color = 'black'
                    node.get_parent().color = 'red'
                    self._left_rotate(node.get_parent())
                    sibling = node.get_parent().right
                if sibling.left.get_color() == 'black' and sibling.right.get_color() == 'black':
                    sibling.color = 'red'
                    node = node.get_parent()
                else:
                    if sibling.right.get_color() == 'black':
                        sibling.left.color = 'black'
                        sibling.color = 'red'
                        self._right_rotate(sibling)
                        sibling = node.get_parent().right
                    sibling.color = node.get_parent().get_color()
                    node.get_parent().color = 'black'
                    sibling.right.color = 'black'
                    self._left_rotate(node.get_parent())
                    node = self.root
            else:
                sibling = node.get_parent().left
                if sibling.get_color() == 'red':
                    sibling.color = 'black'
                    node.get_parent().color = 'red'
                    self._right_rotate(node.get_parent())
                    sibling = node.get_parent().left
                if sibling.right.get_color() == 'black' and sibling.left.get_color() == 'black':
                    sibling.color = 'red'
                    node = node.get_parent()
                else:
                    if sibling.left.get_color() == 'black':
                        sibling.right.color = 'black'
                        sibling.color = 'red'
                        self._left_rotate(sibling)
                        sibling = node.get_parent().left
                    sibling.color = node.get_parent().get_color()
                    node.get_parent().color = 'black'
                    sibling.left.color = 'black'
                    self._right_rotate(node.get_parent())
                    node = self.root
        node.color = 'black'



    def _search(self, current, key):
        if current is None or current.get_key() == key:
            return current

        if key < current.get_key():
            return self._search(current.get_left_child(), key)
        return self._search(current.get_right_child(), key)

    def get_successor(self, node):
        current = node.get_right_child()
        while current.get_left_child():
            current = current.get_left_child()
        return current

    def get_sibling(self, node):
        if node.get_parent() is None:
            return None
        if node == node.get_parent().get_left_child():
            return node.get_parent().get_right_child()
        return node.get_parent().get_left_child()

    def traverse_up(self, node):
        # Traverse up the tree from the given node to the root
        # return the list of the nodes in the path
        tr_up=[]
        temp=node
        while temp:
            tr_up.append(temp)
            temp=temp.get_parent()
        return tr_up

    def traverse_down(self, node, bit_sequence):
        # Traverse down the tree based on the bit sequence
        # return the list of nodes in the path
        temp=node
        tr_down=[]
        tr_down.append(node)
        for bit in bit_sequence:
            if(bit=='0'):
                temp=temp.get_right_child()
            if(bit=='1'):
                temp=temp.get_left_child()
            tr_down.append(temp)
        return tr_down      

    def preorder_traversal(self, node, depth, result):
        # Perform in-order traversal staying within specified depth
        # return the list of nodes in the path
        if node is None:
          return []
        
        if(self.get_depth(node)<=depth):
           result = [node]
        else:
           result = []  

        left_subtree = self.preorder_traversal(node.get_left_child(),depth,result)
        right_subtree = self.preorder_traversal(node.get_right_child(),depth,result)

        result.extend(left_subtree)
        result.extend(right_subtree)

        return result
    
    def get_depth(self,node):
        temp=self.root
        depth=0
        while temp:
            if(temp.get_key()==node.get_key()):
                return depth
            elif(node.get_key()<temp.get_key()):
                temp=temp.get_left_child()
                depth+=1
            else:
                temp=temp.get_right_child()
                depth+=1 
        return depth           

    def inorder_traversal(self,node):
        if node is None:
          return []

        # Recursive inorder traversal
        left_subtree = self.inorder_traversal(node.get_left_child())
        right_subtree = self.inorder_traversal(node.get_right_child())

        return left_subtree + [node] + right_subtree


    def black_height(self, node):  
        # Return the black height of the node
        # Initialize the black height to 0
        black_height = 0

        # Traverse from the given node to a leaf node while counting black nodes
        current = node
        while current:
            if current.get_color() == 'black':
                black_height += 1
            current = current.get_left_child()

        # Return the black height of the tree
        return black_height

    def search(self, key):
        # Search for a node with the given key
        temp=self.root
        while temp:
            if(temp.get_key()==key):
              return temp
            elif(key<temp.get_key()):
              temp=temp.get_left_child()
            else:
              temp=temp.get_right_child()    
        return None


class Lexicon:
    def __init__(self):
        self.red_black_tree = RedBlackTree()  # Red-Black Tree

    def read_chapters(self, chapter_names):
        # Process words from a chapters and build the tree
        # chapter_names is the chapter names list
        # This function should do the pruning fo the Red-Black Tree
        # You can design your own function and call it for the pruning strategy
        for chapter_name in chapter_names:
            with open(chapter_name,'r') as file:
                for line in file:
                    for word in line:
                        if ord(word)>=65 and ord(word)<=90:
                          word=chr(ord(word)+32)
                          continue
                        elif ((ord(word)>=97 and ord(word)<=122) or (word=="'") or (word=='-') or (word=='_')):
                          continue
                        else:
                          word=' '

                    words=line.split(' ')
                    for word in words:
                        self.red_black_tree.insert(word,chapter_name[:-4])
        nodes=self.red_black_tree.inorder_traversal(self.red_black_tree.root)
        print(len(nodes))                
        self.prune_red_black_tree()
        nds=self.red_black_tree.inorder_traversal(self.red_black_tree.root)
        print(len(nds))
        
            

    def prune_red_black_tree(self):
        # Prune the Red-Black Tree by deleting common words
        l=[]
        nodes=self.red_black_tree.inorder_traversal(self.red_black_tree.root)
        
        for node in nodes:
            mru_obs=node.get_mru_objs()
            if((mru_obs[0].get_count()!=0) and (mru_obs[1].get_count()!=0) and (mru_obs[2].get_count()!=0)):
                l.append(node)
            else:
                continue
        print(len(l))        
        for n in l:
            self.red_black_tree.delete(n.get_key())

    def build_index(self):
        # Build the index using the remaining words in the Red-Black Tree
        index=[]
        nodes=self.red_black_tree.inorder_traversal(self.red_black_tree.root)
        for node in nodes:
            index_entry=IndexEntry(node.get_key())
            mruobjs=node.get_mru_objs()
            for mruobj in mruobjs:
                index_entry.chapter_word_counts.append((mruobj.get_word(),mruobj.get_count()))
            index.append(index_entry)
        return index        
            
            



class IndexEntry:
    def __init__(self, word):
        self.word = word  # Word
        self.chapter_word_counts = []  # List of (chapter, word_count) tuples


class MRU:
    def __init__(self,word,chapter_name,count):
        self.word=word
        self.chapter_name=chapter_name
        self.count=count

    def get_word(self):
        return self.word
    
    def set_word(self,word):
        self.word=word
    
    def get_chapter_name(self):
        return self.chapter_name
    
    def set_chapter_name(self,chapter_name):
        self.chapter_name=chapter_name

    def get_count(self):
        return self.count
    
    def set_count(self,count):
        self.count=count
        
