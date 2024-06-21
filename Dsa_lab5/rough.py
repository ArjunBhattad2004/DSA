# MetroStop class
class MetroStop:
    def __init__(self, name, metro_line, fare):
        self.stop_name = name
        self.next_stop = None
        self.prev_stop = None
        self.line = metro_line
        self.fare = fare

    def get_stop_name(self):
        return self.stop_name

    def get_next_stop(self):
        return self.next_stop

    def get_prev_stop(self):
        return self.prev_stop

    def get_line(self):
        return self.line

    def get_fare(self):
        return self.fare

    def set_next_stop(self, next_stop):
        self.next_stop = next_stop

    def set_prev_stop(self, prev_stop):
        self.prev_stop = prev_stop

# MetroLine class
class MetroLine:
    def __init__(self, name):
        self.line_name = name
        self.node = None

    def get_line_name(self):
        return self.line_name

    def get_node(self):
        return self.node

    def set_node(self, node):
        self.node = node

    def print_line(self):
        stop = self.node
        while stop is not None:
            print(stop.get_stop_name())
            stop = stop.get_next_stop()

    def get_total_stops(self):
        temp=self.node
        i=0
        while temp is not None:
            temp=temp.get_next_stop()
            i+=1

        return i      # Implement this method

    def populate_line(self, filename):
         with open(filename,'r') as file:
            for line in file:
                
                line=line.strip(',')
                data=line.split(' ')
                fare=data[-1]
                name=data[0]
                for i in range(1,len(data)-1):
                    name= name + ' ' + data[i]

                new_node=MetroStop(name,self,fare) # Implement this method
                if(self.node==None):
                    self.set_node(new_node)
                else:
                    temp=self.get_node()
                    while(temp.get_next_stop()!=None):
                        temp=temp.get_next_stop()
                    temp.set_next_stop(new_node)
                    new_node.set_prev_stop(temp)  

# AVLNode class
class AVLNode:
    def __init__(self, name):
        self.stop_name = name
        self.stops = []
        self.left = None
        self.right = None
        self.parent = None

    def get_stop_name(self):
        return self.stop_name

    def get_stops(self):
        return self.stops

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_parent(self):
        return self.parent

    def add_metro_stop(self, metro_stop):
        self.stops.append(metro_stop)

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_parent(self, parent):
        self.parent = parent

# AVLTree class
class AVLTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root

    def height(self, node):
        if node is None:
           return 0

        # Recursively calculate the height of the left and right subtrees
        left_height = self.height(node.get_left())
        right_height = self.height(node.get_right())

        # The height of the tree is the maximum of the left and right subtree heights
        return max(left_height, right_height) + 1 # Implement this method

    def string_compare(self, s1, s2):
        if (s1 > s2): return 1
        if (s1 == s2): return 0
        if (s1 < s2 ): return -1

    def balance_factor(self, node):
       if node is None:
           return 0  # Implement this method
       else:
           return (self.height(node.get_left()) - self.height(node.get_right()))

    def rotate_left(self, node):
        new_root = node.get_right()
        T2 = new_root.get_left()

        new_root.set_left(node)
        node.set_right(T2)

        new_root.set_parent(node.get_parent())
        node.set_parent(new_root)
        if T2!=None:
            T2.set_parent(node)

        return new_root  # Implement this method

    def rotate_right(self, node):
        new_root = node.get_left()
        T2 = new_root.get_right()

        new_root.set_right(node)
        node.set_left(T2)

        new_root.set_parent(node.get_parent())
        node.set_parent(new_root)
        if T2!=None:
            T2.set_parent(node)

        return new_root# Implement this method

    def balance(self, node):
        # Balance the tree starting from the given node
        if node is None:
            return None

        # Calculate the balance factor for the current node
        balance_factor = self.balance_factor(node)

        # Left-heavy subtree (LL or LR)
        if balance_factor > 1:
            # Left-Left (LL) case
            if self.balance_factor(node.get_left()) >= 0:
                return self.rotate_right(node)
            # Left-Right (LR) case
            else:
                new_node=self.rotate_left(node.get_left())
                node.set_left(new_node)
                new_node.set_parent(node)
                
                return self.rotate_right(node)

        # Right-heavy subtree (RR or RL)
        elif balance_factor < -1:
            # Right-Right (RR) case
            if self.balance_factor(node.get_right()) <= 0:
                return self.rotate_left(node)
            # Right-Left (RL) case
            else:
                new_nd=self.rotate_right(node.get_right())
                node.set_right(new_nd)
                new_nd.set_parent(node)
                return self.rotate_left(node)

        return node  # No rotation needed  # Implement this method

    def insert(self, node, metro_stop):
       temp=self.get_root()

       if temp is None:
            self.set_root(node)
            return node
            
       while(True):     
            
        compare_result = self.string_compare(node.get_stop_name(), temp.get_stop_name())
        
        if compare_result == 0:
            node.add_metro_stop(metro_stop)
            return self.get_root()
            
            
            
        elif compare_result < 0:
            if(temp.get_left()==None):
                temp.set_left(node)
                node.set_parent(temp)
                return self.balance(temp)
            else:
                temp=temp.get_left()    
            
            
        else:
            if(temp.get_right()==None):
                temp.set_right(node)
                node.set_parent(temp)
                return self.balance(temp)
            else:
                temp=temp.get_right()
            

        
        # Implement this method

    def populate_tree(self, metro_line):

        metro_stop=metro_line.get_node()
        while(metro_stop!=None):
            nn=AVLNode(metro_stop.get_stop_name())
            nn.add_metro_stop(metro_stop)
            self.set_root(self.insert(nn,metro_stop))
            metro_stop=metro_stop.get_next_stop()
              # Implement this method

    def in_order_traversal(self, node):
        if node is None:
            return
        self.in_order_traversal(node.get_left())
        print(node.get_stop_name())
        self.in_order_traversal(node.get_right())

    def get_total_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.get_total_nodes(node.get_left()) + self.get_total_nodes(node.get_right())

    def search_stop(self, stop_name):
        current = self.root

        while current is not None:
            compare_result = self.string_compare(stop_name, current.get_stop_name())

            if compare_result == 0:
                return current
            elif compare_result < 0:
                current = current.get_left()
            else:
                current = current.get_right()

        return None
  # Implement this method

# Trip class
class Trip:
    def __init__(self, metro_stop, previous_trip):
        self.node = metro_stop
        self.prev = previous_trip

    def get_node(self):
        return self.node

    def get_prev(self):
        return self.prev

# Exploration class
class Exploration:
    def __init__(self):
        self.trips = []

    def get_trips(self):
        return self.trips

    def enqueue(self, trip):
        self.trips.append(trip)

    def dequeue(self):
        if not self.trips:
            return None
        trip = self.trips.pop(0)
        print("Dequeued:", trip.get_node().get_stop_name())
        return trip

    def is_empty(self):
        return not bool(self.trips)

# Path class
class Path:
    def __init__(self):
        self.stops = []
        self.total_fare = 0

    def get_stops(self):
        return self.stops

    def get_total_fare(self):
        return self.total_fare

    def add_stop(self, stop):
        self.stops.append(stop)

    def set_total_fare(self, fare):
        self.total_fare = fare

    def print_path(self):
        for stop in self.stops:
            print(stop.get_stop_name())

# PathFinder class
class PathFinder:
    def __init__(self, avl_tree, metro_lines):
        self.tree = avl_tree
        self.lines = metro_lines

    def get_tree(self):
        return self.tree

    def get_lines(self):
        return self.lines

    def create_avl_tree(self):
        for line in self.lines:
            self.tree.populate_tree(line)
  # Implement this method
    
    def searching_trip(trip, result):
       for t in result:
          if t.get_node() == trip.get_node():
            return True
       return False

    def find_path(self, origin, destination):
        
        check_jun = None
        origin_stop = self.tree.search_stop(origin)
        
        destination_stop = self.tree.search_stop(destination)

        if origin_stop is None or destination_stop is None:
            return None  # One or both stops do not exist

        exp = Exploration()
        result = []
        
        for stop in origin_stop.get_stops():
            triph = Trip(stop, None)
            tripf = Trip(stop, None)
            
            if not self.searching_trip(triph,result):
                exp.enqueue(triph)
                result.append(triph)
                
            exp.enqueue(tripf)
            #result.append(tripf)

        flagt = 1
        q = exp.get_trips()
        
        search_forward = q[0].get_node()
        search_backward = q[0].get_node()
        mpp = {}
        
        while q and (search_forward.get_stop_name() != destination and search_backward.get_stop_name() != destination):
            if flagt == 1:
                flagt = 0
            else:
                flagt = 1
            
            search_backward = q[0].get_node()
            search_forward = q[0].get_node()

            if flagt == 1:
                q[0].set_trav(False)

                while search_backward and search_backward.get_stop_name() != destination:
                    jun = self.tree.search_stop(search_backward.get_stop_name())
                    v = jun.get_stops()

                    if len(v) > 1:
                        for stop in v:
                            trip = Trip(stop, q[0])

                            if stop != search_backward and not self.searching_trip(trip,result):
                                mpp[trip] = search_backward
                                q.append(trip)
                                exp.enqueue(trip)
                                q.append(trip)
                                exp.enqueue(trip)
                                result.append(trip)
                    
                    search_backward = search_backward.get_prev_stop()
                
            elif flagt == 0:
                while search_forward and search_forward.get_stop_name() != destination:
                    q[0].set_trav(True)
                    jun = self.tree.search_stop(search_forward.get_stop_name())
                    v = jun.get_stops()

                    if len(v) > 1:
                        for stop in v:
                            trip = Trip(stop, q[0])

                            if stop != search_forward and not self.searching_trip(trip,result):
                                mpp[trip] = search_forward
                                q.append(trip)
                                exp.enqueue(trip)
                                q.append(trip)
                                exp.enqueue(trip)
                                result.append(trip)

                    search_forward = search_forward.get_next_stop()

            if not search_backward:
                search_backward = search_forward
            
            if not search_forward:
                search_forward = search_backward

            if search_backward.get_stop_name() == destination or search_forward.get_stop_name() == destination:
                check_jun = q[0]
                exp.dequeue()
                q.pop(0)

        if not search_backward and not search_forward:
            return None

        path = Path()
        ptr = None

        if search_backward.get_stop_name() == destination:
            ptr = search_backward
        else:
            ptr = search_forward

        fare = 0
        f1 = 0
        f2 = 0
        chalo = check_jun

        while chalo.get_prev() is not None:
            f1 = ptr.get_fare()

            while ptr != chalo.get_node():
                path.add_stop(ptr)

                if chalo.get_trav():
                    ptr = ptr.get_prev_stop()
                else:
                    ptr = ptr.get_next_stop()

            f2 = ptr.get_fare()
            fare = fare + abs(f1 - f2)
            ptr = mpp[chalo]
            chalo = chalo.get_prev()

        f1 = ptr.get_fare()

        while ptr.get_stop_name() != origin:
            path.add_stop(ptr)

            if chalo.get_trav():
                ptr = ptr.get_prev_stop()
            else:
                ptr = ptr.get_next_stop()

        path.add_stop(ptr)
        f2 = ptr.get_fare()
        fare = fare + abs(f1 - f2)
        path.set_total_fare(fare)
        return path

lines = []