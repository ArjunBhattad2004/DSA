class Vehicle:
    def __init__(self, vehicle_number, seating_capacity):
        self.vehicle_number = vehicle_number
        self.seating_capacity = seating_capacity
        self.trips = []

    def get_vehicle_number(self):
        return self.vehicle_number

    def set_vehicle_number(self, new_vehicle_number):
        self.vehicle_number = new_vehicle_number

    def get_seating_capacity(self):
        return self.seating_capacity

    def set_seating_capacity(self, new_seating_capacity):
        self.seating_capacity = new_seating_capacity

    def get_trips(self):
        return self.trips

    def add_trip(self, trip):
        self.trips.append(trip)


class Trip:
    def __init__(self, vehicle, pick_up_location, drop_location, departure_time):
        self.vehicle = vehicle
        self.pick_up_location = pick_up_location
        self.drop_location = drop_location
        self.departure_time = departure_time
        self.booked_seats = 0

    def get_vehicle(self):
        return self.vehicle

    def get_pick_up_location(self):
        return self.pick_up_location

    def set_pick_up_location(self, new_pick_up_location):
        self.pick_up_location = new_pick_up_location

    def get_drop_location(self):
        return self.drop_location

    def set_drop_location(self, new_drop_location):
        self.drop_location = new_drop_location

    def get_departure_time(self):
        return self.departure_time

    def set_departure_time(self, new_departure_time):
        self.departure_time = new_departure_time

    def get_booked_seats(self):
        return self.booked_seats

    def set_booked_seats(self, new_booked_seats):
        self.booked_seats = new_booked_seats


class Location:
    def __init__(self, name):
        self.name = name
        self.service_ptrs = []
        self.trips = []
        

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_service_ptr(self, drop_location):
        # Find and return the service_ptr associated with the specified droplocation
        for service_ptr in self.service_ptrs:
            if service_ptr.get_name() == drop_location:
                return service_ptr
        return None  # Return None if not found

    def set_service_ptr(self, drop_location):
         # Update the service_ptr associated with the specified droplocation
        sp=TransportService(drop_location)
        self.service_ptrs.append(sp)

    def add_trip(self, trip):
        if trip.get_pick_up_location() != self.name:
            return
        else:
            self.trips.append(trip)


        

class BinaryTreeNode:
    def __init__(self, departure_time=0, trip_node_ptr=None, parent_ptr=None):
        self.left_ptr = None
        self.right_ptr = None
        self.parent_ptr = parent_ptr
        self.departure_time = departure_time
        self.trip_node_ptr = trip_node_ptr

    def get_left_ptr(self):
        return self.left_ptr

    def set_left_ptr(self, new_left_ptr):
        self.left_ptr = new_left_ptr

    def get_right_ptr(self):
        return self.right_ptr

    def set_right_ptr(self, new_right_ptr):
        self.right_ptr = new_right_ptr

    def get_parent_ptr(self):
        return self.parent_ptr

    def set_parent_ptr(self, new_parent_ptr):
        self.parent_ptr = new_parent_ptr

    def get_departure_time(self):
        return self.departure_time

    def set_departure_time(self, new_departure_time):
        self.departure_time = new_departure_time

    def get_trip_node_ptr(self):
        return self.trip_node_ptr

    def set_trip_node_ptr(self, new_trip_node_ptr):
        self.trip_node_ptr = new_trip_node_ptr



class BinaryTree:
    def __init__(self):
        self.root = None

    def get_height(self):
        if self.root is None:
          return 0

    # Recursively calculate the height of the left and right subtrees
        left_height = self.get_height(self.root.get_left_ptr())
        right_height = self.get_height(self.root.get_right_ptr())

    # The height of the tree is the maximum of the left and right subtree heights
        return max(left_height, right_height) + 1
        # Return the height of the tree 
        

    def get_number_of_nodes(self):
        if self.root is None:
          return 0

    # Recursively count nodes in the left and right subtrees
        left_count = self.get_number_of_nodes(self.root.get_left_ptr())
        right_count = self.get_number_of_nodes(self.root.get_right_ptr())

    # Add 1 for the current node
        return left_count + right_count + 1

        # Return the number of nodes in the tree
        


class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def get_element_with_minimum_key(self):
        if self.root is None:
            return None

        temp = self.root
        while temp.get_left_ptr()!=None:
            temp = temp.get_left_ptr()

        return temp

        # Return the element with the minimum key (not implemented here)
        

    def get_element_with_maximum_key(self):
        if self.root is None:
            return None
        
        temp = self.root
        while temp.get_right_ptr()!=None:
            temp = temp.get_right_ptr()

        return temp    
        # Return the element with the maximum key (not implemented here)
        

    def search_node_with_key(self, key):
        if self.root is None:
            return None
        
        temp=self.root
        if temp.get_departure_time()==key:
            return temp
        while temp.get_departure_time()!=key:
            if key>temp.get_departure_time():
                temp=temp.get_right_ptr()

            if key<temp.get_departure_time():
                temp=temp.get_left_ptr()  

        return temp         


        # Search for a node with the given key (not implemented here)
        

    def get_successor_node(self, node):
        # Find the successor node of the given node (not implemented here)
        successor = None  # Initialize the successor to None
        current = self.root  # Start at the root
        target_key=node.get_departure_time()

        while current is not None:
            if target_key < current.get_departure_time():
               successor = current  # Update the successor to the current node
               current = current.get_left_ptr()  # Move to the left subtree
            elif target_key > current.get_departure_time():
               current = current.get_right_ptr()  # Move to the right subtree
            else:
            # Node with the target key is found
               if current.get_right_ptr():
                # If there's a right subtree, find the leftmost node in it
                   temp=current.get_right_ptr()
                   while temp.get_left_ptr()!=None:
                      temp=temp.get_left_ptr()
                   successor=temp    
               break

        return successor
        
    def get_predecessor_node(self, node):
        # Find the predecessor node of the given node (not implemented here)
         predecessor = None
         current = self.root  # Start at the root
         target_key=node.get_departure_time()


    # Search for the target node in the BST
         while current is not None:
            if target_key < current.get_departure_time():
               current = current.get_left_ptr()  # Move to the left subtree
            elif target_key > current.get_departure_time():
               predecessor = current  # Update the predecessor to the current node
               current = current.get_right_ptr()  # Move to the right subtree
            else:
            # Node with the target key is found
               if current.get_left_ptr():
                # If there's a left subtree, find the rightmost node in it
                   temp=current.get_left_ptr()
                   while temp.get_right_ptr()!=None:
                       temp=temp.get_right_ptr()
                   predecessor = temp
               break

         return predecessor
        

class TransportService:
    def __init__(self,name, location_ptr=None, bst_head=None):
        self.location_ptr = location_ptr
        self.bst_head = bst_head
        self.name = name

    def get_name(self):
        return self.name
    
    def set_name(self,name):
        self.name=name


    def get_location_ptr(self):
        return self.location_ptr

    def set_location_ptr(self, new_location_ptr):
        self.location_ptr = new_location_ptr

    def get_bst_head(self):
        return self.bst_head

    def set_bst_head(self, new_bst_head):
        self.bst_head = new_bst_head

    def add_trip(self, key, trip):
        # Add the trip to the BST (not implemented here)
        new_node=BinaryTreeNode(key,trip,parent_ptr=None)
        w=None
        v=self.bst_head
        while v!=None:
            w=v
            if(key<v.get_departure_time()):
                v=v.get_left_ptr()
            else:
                v=v.get_right_ptr()

        new_node.set_parent_ptr(w)
        if w==None:
            self.set_bst_head(new_node)

        elif(key<w.get_departure_time()):
            w.set_left_ptr(new_node)

        else:
            w.set_right_ptr(new_node) 

   

class TravelDesk:
    def __init__(self):
        self.vehicles = []
        self.locations = []

    def add_trip(self, vehicle_number, seating_capacity, pick_up_location, drop_location, departure_time):
        # Check if the vehicle already exists, if not, create a new one with the seating capacity
        vehicle = None
        for v in self.vehicles:
            if v.get_vehicle_number() == vehicle_number:
                vehicle = v
                break
        if vehicle is None:
            vehicle = Vehicle(vehicle_number, seating_capacity)
            self.vehicles.append(vehicle)

        # Create a new trip and add it to the appropriate objects
        trip = Trip(vehicle, pick_up_location, drop_location, departure_time)
        vehicle.add_trip(trip)

        # Create or retrieve the Location object and associated pick-up location
        pick_up_location_obj = None
        

        for loc in self.locations:
            if loc.get_name() == pick_up_location:
                pick_up_location_obj = loc
            

        if pick_up_location_obj is None:
            pick_up_location_obj = Location(pick_up_location)
            self.locations.append(pick_up_location_obj)

        

        # Add the trip to the TransportService's BST
        service_ptr = pick_up_location_obj.get_service_ptr(drop_location)
        if service_ptr is None:
            service_ptr = TransportService(drop_location,pick_up_location_obj)
            pick_up_location_obj.set_service_ptr(drop_location)

        service_ptr.add_trip(departure_time, trip)

    def show_trips(self, pick_up_location, after_time, before_time):
       trips_matching_criteria = []

        # Convert time strings to datetime objects for comparison
       

       for vehicle in self.vehicles:
            for trip in vehicle.get_trips():
                if (
                    trip.get_pick_up_location() == pick_up_location
                    and after_time <= trip.get_departure_time()
                    and trip.get_departure_time() < before_time
                ):
                    trips_matching_criteria.append(trip)

       return trips_matching_criteria

       


    def show_tripsbydestination(self, pick_up_location, destination, after_time, before_time):
        trips_matching_criteria = []

        for vehicle in self.vehicles:
            for trip in vehicle.get_trips():
                if (trip.get_pick_up_location() == pick_up_location and trip.get_drop_location() == destination and after_time <= trip.get_departure_time() and trip.get_departure_time() <= before_time):
                    trips_matching_criteria.append(trip)

        return trips_matching_criteria

    def book_trip(self, pick_up_location, drop_location, vehicle_number, departure_time):
       
        # Find the specified vehicle based on its number
        selected_vehicle = None
        for vehicle in self.vehicles:
            if vehicle.get_vehicle_number() == vehicle_number:
                selected_vehicle = vehicle
                break

        if selected_vehicle is None:
            return None

        # Find the trip matching the criteria
        matching_trip = None
        for trip in selected_vehicle.get_trips():
            if (
                trip.get_pick_up_location() == pick_up_location
                and trip.get_drop_location() == drop_location
                and trip.get_departure_time() == departure_time
            ):
                matching_trip = trip
                break

        if matching_trip is None:
            return None

        # Check if there are available seats on the selected trip
        if matching_trip.get_booked_seats() < selected_vehicle.get_seating_capacity():
            # Book the trip and update the number of booked seats
            matching_trip.set_booked_seats(matching_trip.get_booked_seats() + 1)

            # If all seats are booked, remove the trip node from the BST
            if matching_trip.get_booked_seats() == selected_vehicle.get_seating_capacity():
                service_location = matching_trip.get_pick_up_location()
                drop_location = matching_trip.get_drop_location()

                for location in self.locations:
                    if location.get_name() == service_location:
                        service = location.get_service_ptr(drop_location)
                        if service is not None:
                            bst_head = service.get_bst_head()
                            bst_head = self._remove_trip_node(bst_head, matching_trip)
                            service.set_bst_head(bst_head)

            return matching_trip
        else:
            return None

    def _remove_trip_node(self, root, trip):
       
        if root is None:
            return root

        if trip.get_departure_time() < root.get_departure_time():
            root.set_left_ptr(self._remove_trip_node(root.get_left_ptr(), trip))
        elif trip.get_departure_time() > root.get_departure_time():
            root.set_right_ptr(self._remove_trip_node(root.get_right_ptr(), trip))
        else:
            if root.get_left_ptr() is None:
                return root.get_right_ptr()
            elif root.get_right_ptr() is None:
                return root.get_left_ptr()

            min_node = self._find_min_node(root.get_right_ptr())
            root.set_departure_time(min_node.get_departure_time())
            root.set_trip_node_ptr(min_node.get_trip_node_ptr())
            root.set_right_ptr(self._remove_trip_node(root.get_right_ptr(), min_node.get_trip_node_ptr()))

        return root

    def _find_min_node(self, node):
        while node.get_left_ptr() is not None:
            node = node.get_left_ptr()
        return node
        
         