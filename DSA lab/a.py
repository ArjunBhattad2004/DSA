EntityArray = []

class StudentRecord:
    def __init__(self):
        self.studentName = ""
        self.rollNumber = ""

    def get_studentName(self):
        return self.studentName

    def set_studentName(self, name):
        self.studentName = name

    def get_rollNumber(self):
        return self.rollNumber

    def set_rollNumber(self, rollnum):
        self.rollNumber = rollnum

class Node:
    def __init__(self):
        self.next = None
        self.element = None

    def get_next(self):
        return self.next

    def get_element(self):
        return self.element

    def set_next(self, value):
        self.next = value

    def set_element(self, student):
        self.element = student

class Entity:
    def __init__(self):
        self.name = ""
        self.iterator = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_iterator(self):
        return self.iterator

    def set_iterator(self, iter):
        self.iterator = iter

class LinkedList(Entity):
    def add_student_record(self, record):
        new_node = Node()
        new_node.set_element(record)

        if self.iterator is None:
            self.iterator = new_node
        else:
            it = self.iterator
            while it.get_next() is not None:
                it = it.get_next()
            it.set_next(new_node)

    def delete_student_record(self, recordName):
        current = self.iterator

        # Case 1: If the node to be deleted is the head
        if current and current.get_element().get_studentName() == recordName:
            self.iterator = current.get_next()
            del current
            return

        # Case 2: Search for the node to be deleted
        prev = None
        while current and current.get_element().get_studentName() != recordName:
            prev = current
            current = current.get_next()

        # If the node is not found
        if current is None:
            return

        # Case 3: Node found, update the links to delete it
        prev.set_next(current.get_next())
        del current

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            
            # Extract data
            studentName = data[0]
            rollNumber = data[1]
            department = data[2]
            courses = [course.strip() for course in data[3].strip('[]').split(',')]
            hostel = data[4]
            clubs = [club.strip() for club in data[5].strip('[]').split(',')]

            # Create a new StudentRecord object
            student = StudentRecord()
            student.set_studentName(studentName)
            student.set_rollNumber(rollNumber)

            # Add the student to the appropriate entities
            for entity in EntityArray:
                if entity.get_name() == department:
                    entity.add_student_record(student)

                if hostel == entity.get_name():
                    entity.add_student_record(student)

                for course in courses:
                    if course == entity.get_name():
                        entity.add_student_record(student)

                for club in clubs:
                    if club == entity.get_name():
                        entity.add_student_record(student)