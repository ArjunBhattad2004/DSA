class HybridNode:
    def __init__(self, key, element):
        self.key = key
        self.element = element
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.next_node = None
        self.colour = None

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

    def get_colour(self):
        return self.colour  

    def set_colour(self,colour):
        self.colour=colour 
         
    def recolour(self):
        if(self.colour=='red'):
            self.colour='black'
        if(self.colour=='black'):
            self.colour='red' 

class RedBlackTree:
    def __init__(self):
        self.root = None
        

    def insert(self, key, element):
        new_node = HybridNode(key, element)
        if self.root is None:
            # Case 1: Inserting the root node
            new_node.colour = 'black'
            self.root = new_node
        else:
            # Case 2: Insert as a red node
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
        while node != self.root and node.get_parent().get_colour() == 'red':
            if node.get_parent() == node.get_parent().get_parent().get_left_child():
                uncle = node.get_parent().get_parent().get_right_child()
                if uncle and uncle.get_colour() == 'red':
                    # Case 1: Recoloring
                    node.get_parent().set_colour('black')
                    uncle.set_colour('black')
                    node.get_parent().get_parent.set_colour('red')
                    node = node.get_parent().get_parent()
                else:
                    if node == node.get_parent().get_right_child():
                        # Case 2: Left rotation
                        node = node.get_parent()
                        self.left_rotate(node)
                    # Case 3: Right rotation and recoloring
                    node.get_parent().set_colour('black')
                    node.get_parent().get_parent().set_colour('red')
                    self.right_rotate(node.get_parent().get_parent())
            else:
                uncle = node.get_parent().get_parent().get_left_child()
                if uncle and uncle.get_colour() == 'red':
                    # Case 1: Recoloring
                    node.get_parent().set_colour('black')
                    uncle.set_colour('black')
                    node.get_parent().get_parent().set_colour('red')                   
                    node = node.get_parent().get_parent()
                else:
                    if node == node.get_parent().left_child:
                        # Case 2: Right rotation
                        node = node.get_parent()
                        self.right_rotate(node)
                    # Case 3: Left rotation and recoloring
                    node.get_parent().set_colour('black')
                    node.get_parent().get_parent().set_colour('red')                   
                    self.left_rotate(node.get_parent().get_parent())
        self.root.colour = 'black'
    
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
            node.get_parent.set_right_child(right_child)
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
            

        # Implement Red-Black Tree insertion
        

    def delete(self, key):
        # Implement Red-Black Tree deletion
        if self.root is None:
            return

        # Find the node to delete and replace it with its successor
        node_to_delete = self._search(self.root, key)
        if node_to_delete is None:
            return False # Key not found

        if node_to_delete.get_left_child() is not None and node_to_delete.get_right_child() is not None:
            successor = self.get_successor(node_to_delete)
            node_to_delete.set_key(successor.get_key())
            node_to_delete.set_element(successor.get_element())
            node_to_delete = successor

        # Now node_to_delete has at most one child (or none)
        child = node_to_delete.get_right_child() if node_to_delete.get_right_child() is not None else node_to_delete.get_left_child()

        if node_to_delete.get_colour() == 'black':
            if child is None or child.get_colour() == 'black':
                self.fix_double_black(node_to_delete)

        self.delete_node(node_to_delete)
        return True
    
    def delete_node(self, node):
        if node.get_parent() is None:
            if node == self.root:
                self.root = None
        else:
            if node == node.get_parent().get_left_child():
                node.get_parent().set_left_child(None)
            else:
                node.get_parent().set_right_child(None)

    def fix_double_black(self, node):
        if node == self.root:
            return

        sibling = self.get_sibling(node)
        if sibling is None:
            self.fix_double_black(node.get_parent())
        else:
            if sibling.get_colour() == 'red':
                sibling.set_colour('black')
                node.get_parent().set_colour('red')
                if node == node.get_parent().get_left_child():
                    self.left_rotate(node.get_parent())
                else:
                    self.right_rotate(node.get_parent())
                sibling = self.get_sibling(node)

            if (sibling.get_left_child() is None or sibling.get_left_child().get_colour() == 'black') and \
                    (sibling.get_right_child() is None or sibling.get_right_child().get_colour() == 'black'):
                sibling.set_colour('red')
                if node.get_parent().get_colour() == 'black':
                    self.fix_double_black(node.get_parent())
                else:
                    node.get_parent().set_colour('black')
            else:
                if node == node.get_parent().get_left_child() and (sibling.get_right_child() is None or sibling.get_right_child().get_colour() == 'black'):
                    sibling.set_colour('red')
                    sibling.get_left_child().set_colour('black')
                    self.right_rotate(sibling)
                elif node == node.get_parent().get_right_child() and (sibling.get_left_child() is None or sibling.get_left_child().get_colour() == 'black'):
                    sibling.set_colour('red')
                    sibling.get_right_child().set_colour('black')
                    self.left_rotate(sibling)

                sibling.set_colour(node.get_parent().get_colour())
                node.get_parent().set_colour('black')
                if node == node.get_parent().get_left_child():
                    if sibling.get_right_child():
                        sibling.get_right_child().set_colour('black')
                    self.left_rotate(node.get_parent())
                else:
                    if sibling.get_left_child():
                        sibling.get_left_child().set_colour('black')
                    self.right_rotate(node.get_parent())

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

    def traverse_up(self, node):#vector node
        # Traverse up the tree from the given node to the root
        tr_up=[]
        temp=node
        while temp:
            tr_up.append(temp)
            temp=temp.get_parent()
        return tr_up    

    def traverse_down(self, node, bit_sequence):#vector node
        # Traverse down the tree based on the bit sequence
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


    def preorder_traversal(self, node, depth, result):#vector string
        # Perform in-order traversal staying within specified depth
        pass

    def black_height(self, node):
        # Initialize the black height to 0
        black_height = 0

        # Traverse from the given node to a leaf node while counting black nodes
        current = node
        while current:
            if current.get_colour() == 'black':
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
        self.red_black_tree = RedBlackTree()

    def read_chapter(self, chapter_name, words):
        # Process words from a chapter and update the Red-Black Tree
        with open(chapter_name,'r') as file:
            for line in file:
                for word in line:
                    if ord(word)>=65 and ord(word)<=90:
                        word=chr(ord(word)+32)
                        continue
                    elif ord(word)>=97 and ord(word)<=122:
                        continue
                    else:
                        word=' '

                words=line.split(' ')
                for word in words:        




    def prune_red_black_tree(self):
        # Prune the Red-Black Tree by deleting common words
        pass

    def build_index(self):
        # Build the index using the remaining words in the Red-Black Tree
        pass


class IndexEntry:
    def __init__(self, word):
        self.word = word
        self.chapter_word_counts = []  # List of (chapter, word_count) tuples

    def add_occurrence(self, chapter, word_count):
        # Add a chapter's word count for this word
        pass

    def __str__(self):
        # Return a string representation of the IndexEntry
        pass