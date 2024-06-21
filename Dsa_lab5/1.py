class MetroStop:
    def __init__(self, name, metroLine, fare):
        self.stopName = name
        self.nextStop = None
        self.prevStop = None
        self.line = metroLine
        self.fare = fare

    def getStopName(self):
        return self.stopName

    def getNextStop(self):
        return self.nextStop

    def getPrevStop(self):
        return self.prevStop

    def getLine(self):
        return self.line

    def getFare(self):
        return self.fare

    def setNextStop(self, next):
        self.nextStop = next

    def setPrevStop(self, prev):
        self.prevStop = prev


class MetroLine:
    def __init__(self, name):
        self.lineName = name
        self.node = None

    def getLineName(self):
        return self.lineName

    def getNode(self):
        return self.node

    def setNode(self, node):
        self.node = node

    def printLine(self):
        stop = self.node
        while stop is not None:
            print(stop.getStopName())
            stop = stop.getNextStop()

    def getTotalStops(self):
        temp=self.node
        i=0
        while temp is not None:
            temp=temp.getNextStop()
            i+=1

        return i    


    def populateLine(self, filename):
        with open(filename,'r') as file:
            for line in file:
                line=line.strip(',')
                data=line.split(' ')
                fare=data[-1]
                name=data[0]
                for i in range(1,len(data)-1):
                    name= name + ' ' + data[i]

                new_node=MetroStop(name,self,fare)    


class AVLNode:
    def __init__(self, name):
        self.stopName = name
        self.stops = []
        self.left = None
        self.right = None
        self.parent = None

    def getStopName(self):
        return self.stopName

    def getStops(self):
        return self.stops

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getParent(self):
        return self.parent

    def addMetroStop(self, metroStop):
        self.stops.append(metroStop)


class AVLTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def setRoot(self, root):
        self.root = root

    def height(self, node):
        pass

    def balanceFactor(self, node):
        pass

    def rotateLeft(self, node):
        pass

    def rotateRight(self, node):
        pass

    def balance(self, node):
        pass

    def stringCompare(self, s1, s2):
        if(s1<s2):
            return -1
        elif(s1>s2):
            return 1
        else:
            return 0

    def insert(self, node, metroStop):
        pass

    def populateTree(self, metroLine):
        pass

    def inOrderTraversal(self, node):
        pass

    def getTotalNodes(self, node):
        pass


class Exploration:
    def __init__(self, metroStop):
        self.node = metroStop

    def getNode(self):
        return self.node


class Trip:
    def __init__(self, metroStop, previousTrip):
        self.node = metroStop
        self.prev = previousTrip

    def getNode(self):
        return self.node

    def getPrev(self):
        return self.prev


class PathFinder:
    def __init__(self, avlTree, metroLines):
        self.tree = avlTree
        self.lines = metroLines

    def getTree(self):
        return self.tree

    def getLines(self):
        return self.lines

    def createAVLTree(self):
        pass

    def searchPath(self, origin, destination):
        pass
