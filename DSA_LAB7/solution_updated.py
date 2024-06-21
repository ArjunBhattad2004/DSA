# from scratch max heap
class MaxHeap:
    def __init__(self):
        pass
    
    def parent(self, i):
        pass

    def left(self, i):
        pass

    def right(self, i):
        pass
    
    def get_max(self):
        pass
    
    def extract_max(self):
        pass
        return max_item
    
    def max_heapify(self, i):
        pass
    
    def insert(self, item):
        pass

    def is_empty(self):
        pass


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, source, destination, min_freight_cars_to_move, max_parcel_capacity):
        # creates vertices if they don't exist
        # add destination to source's neighbors
        # add source to destination's neighbors
        # each vertex should have a min_freight_cars_to_move and max_parcel_capacity data fields (# this is optional, but recommended for ideal solution)
        if source not in self.vertices.keys():
            self.vertices[source]=Vertex(source,min_freight_cars_to_move,max_parcel_capacity)
        if destination not in self.vertices.keys():
            self.vertices[destination]=Vertex(destination,min_freight_cars_to_move,max_parcel_capacity)
        self.vertices[source].add_neighbor(destination)
        self.vertices[destination].add_neighbor(source)        

    def print_graph(self): #optional
        pass

    def bfs(self, source, destination):
        # returns a list of vertices in the path from source to destination using BFS
        # actual move might only use next vertex in the path though (careful understanding required)
        pass

    def dfs(self, source, destination):
        # returns a list of vertices in the path from source to destination using DFS
        # actual move might only use next vertex in the path though (careful understanding required)
        # ordering of vertices is important, create vertices in the order they are seen in the input file
        pass

    def groupFreightCars(self):
        # group freight cars at every vertex based on their destination
        return

    def moveTrains(self):
        # move trains  (constitutes one time tick)
        # a train should move only if has >= min_freight_cars_to_move freight cars to link (link is a vertex, obtained from bfs or dfs)
        # once train moves from the source vertex, all the freight cars should be sealed and cannot be unloaded (at any intermediate station) until they reach their destination
        return


class Vertex:
    def __init__(self, name, min_freight_cars_to_move, max_parcel_capacity):


        self.name = name
        self.freight_cars = []
        self.neighbors = []
        self.trains_to_move = None
        self.min_freight_cars_to_move = min_freight_cars_to_move
        self.max_parcel_capacity = max_parcel_capacity
        self.parcel_destination_heaps = {}
        self.sealed_freight_cars = []
        self.all_parcels = []

    def add_neighbor(self, neighbor):
        # add neighbor to self.neighbors
        self.neighbors.append(neighbor)
    
    def get_all_current_parcels(self):
        return self.all_parcels
        # return all parcels at the current vertex
    
    def clean_unmoved_freight_cars(self):
        # remove all freight cars that have not moved from the current vertex
        # add all parcels from these freight cars back to the parcel_destination_heaps accoridingly
        pass

    def loadParcel(self, parcel):
        # load parcel into parcel_destination_heaps based on parcel.destination
        pass


    def loadFreightCars(self):
        # load parcels onto freight cars based on their destination
        # remember a freight car is allowed to move only if it has exactly max_parcel_capacity parcels
        return    


    def print_parcels_in_freight_cars(self):
        # optional method to print parcels in freight cars
        for car in self.freight_cars:
            for parcel in car.parcels:
                print(parcel)
        

class FreightCar:
    def __init__(self, max_parcel_capacity):

        self.max_parcel_capacity = max_parcel_capacity
        self.parcels = []
        self.destination_city = None
        self.next_link = None
        self.current_location = None
        self.sealed = False

    def load_parcel(self, parcel):
        # load parcel into freight car
        self.parcels.append(parcel)

    def can_move(self):
        # return True if freight car can move, False otherwise
        if(len(self.parcels)==self.max_parcel_capacity and self.next_link!=None):
            return True
        else:
            return False
    def move(self, destination):
        # update current_location
        # empty the freight car if destination is reached, set all parcels to delivered
        self.current_location=destination
        if(destination==self.destination_city):
            while len(self.parcels)>0:
                parcel=self.parcels.pop(0)
                parcel.delivered=True



class Parcel:
    def __init__(self, time_tick, parcel_id, origin, destination, priority):
        self.time_tick = time_tick
        self.parcel_id = parcel_id
        self.origin = origin
        self.destination = destination
        self.priority = priority
        self.delivered = False
        self.current_location = origin

class PRC:
    def __init__(self, min_freight_cars_to_move=5, max_parcel_capacity=5):
        self.graph = Graph()
        self.freight_cars = []
        self.parcels = {}
        self.parcels_with_time_tick = {}
        self.min_freight_cars_to_move = min_freight_cars_to_move
        self.max_parcel_capacity = max_parcel_capacity
        self.time_tick = 1

        self.old_state = None
        self.new_state = None

        self.max_time_tick = 10

        self.create_graph('samples/1/graph.txt')
        self.process_parcels('samples/5/bookings.txt')

    
    def get_state_of_parcels(self):
        return {x.parcel_id:x.current_location for x in self.parcels.values()}
        

    def process_parcels(self, booking_file_path):
        # read bookings.txt and create parcels, populate self.parcels_with_time_tick (dict with key as time_tick and value as list of parcels)
        # and self.parcels (dict with key as parcel_id and value as parcel object)
        with open(booking_file_path,'r') as file:
            for line in file:
                data=line.split(' ')
                if data[0] not in self.parcels_with_time_tick.keys():
                    self.parcels_with_time_tick[data[0]]=[]
                self.parcels_with_time_tick[data[0]].append(Parcel(data[0],data[1],data[2],data[3],data[4]))    


    
    def getNewBookingsatTimeTickatVertex(self, time_tick, vertex):
        # return all parcels at time tick and vertex
        return bookings


    def run_simulation(self, run_till_time_tick=None):
        # run simulation till run_till_time_tick if provided, if not run till max_time_tick
        # if convergence is achieved (before run_till_time_tick or max_time_tick), stop simulation
        # convergence is state of parcels in the system does not change from one time tick to the next, and there are no further incoming parcels in next time ticks
        pass

    def convergence_check(self, previous_state, current_state):
        # return True if convergence achieved, False otherwise
        pass

    def all_parcels_delivered(self):
        return all(parcel.delivered for _,parcel in self.parcels.items())
    
    def delivered_parcels(self):
        return [parcel.parcel_id for parcel in self.parcels.values() if parcel.delivered]
    
    def get_stranded_parcels(self):
        return [parcel.parcel_id for parcel in self.parcels.values() if not parcel.delivered]

    def status_of_parcels_at_time_tick(self, time_tick):
        return [parcel.parcel_id for parcel in self.parcels.values() if parcel.time_tick <= time_tick and not parcel.delivered]
    
    def status_of_parcel(self, parcel_id):
        return self.parcels[parcel_id].delivered, self.parcels[parcel_id].current_location
    
    def create_graph(self, graph_file_path):
        # read graph.txt and create graph
        pass


if __name__ == "__main__":
    
    min_freight_cars_to_move = 2
    max_parcel_capacity = 2

    prc = PRC(min_freight_cars_to_move, max_parcel_capacity)

    prc.run_simulation()

    print(f'All parcels delivered: {prc.all_parcels_delivered()}')
    print(f'Delivered parcels: {prc.delivered_parcels()}')
    print(f'Stranded parcels: {prc.get_stranded_parcels()}')