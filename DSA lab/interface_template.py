

EntityArray = []
Students = []

class StudentRecord:
    def __init__(self):
        self.studentName = ""
        self.rollNumber = ""

    def get_studentName(self):
        return self.studentName 

    def set_studentName(self, name):
        self.studentName=name

    def get_rollNumber(self):
        return self.rollNumber

    def set_rollNumber(self, rollnum):
        self.rollNumber=rollnum


class Node:
    def __init__(self):
        self.next = None
        self.element = None

    def get_next(self):
        return self.next

    def get_element(self):
        return self.element

    def set_next(self, value):
        self.next=next

    def set_element(self, student):
        self.element=student


class Entity:
    def __init__(self):
        self.name = ""
        self.iterator = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name=name

    def get_iterator(self):
        return self.iterator

    def set_iterator(self, iter):
        self.iterator=iter



class LinkedList(Entity):
    def __init__(self):
        super().__init__()

    def add_student(self, student_record):
        new_node = Node(student_record)
        if not self.iterator:
            self.iterator = new_node
        else:
            current_node = self.iterator
            while current_node.get_next():
                current_node = current_node.get_next()
            current_node.set_next(new_node)

    def delete_student(self, student_name):
        current_node = self.iterator
        prev_node = None
        while current_node:
            if current_node.get_element().get_studentName() == student_name:
                if prev_node:
                    prev_node.set_next(current_node.get_next())
                else:
                    self.iterator = current_node.get_next()
                return
            prev_node = current_node
            current_node = current_node.get_next()

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            studentName, rollNumber, department, courses_str, hostel, clubs_str = data
            courses = courses_str.strip('[]').split(',')
            clubs = clubs_str.strip('[]').split(',')

            # Create a StudentRecord object
            student_record = StudentRecord()
            student_record.set_studentName(studentName)
            student_record.set_rollNumber(rollNumber)

            # Check if the department entity already exists in EntityArray
            department_entity = None
            for entity in EntityArray:
                if entity.get_name() == department:
                    department_entity = entity
                    break

            # If not, create a new department entity and add it to EntityArray
            if department_entity is None:
                department_entity = LinkedList()
                department_entity.set_name(department)
                EntityArray.append(department_entity)

            # Add the student record to the department entity
            department_entity.add_student(student_record)

            # Iterate through the courses and add them to EntityArray
            for course_name in courses:
                course_entity = None
                for entity in EntityArray:
                    if entity.get_name() == course_name:
                        course_entity = entity
                        break

                if course_entity is None:
                    course_entity = LinkedList()
                    course_entity.set_name(course_name)
                    EntityArray.append(course_entity)

                course_entity.add_student(student_record)

# def read_input_file(file_path):
   
#     with open('Details.txt', 'r') as file:
#          for line in file:
#                  data=line.strip().split(',')
#                  Students.append(data[0])
#                  Students.append(data[1])

#                  if data[2] not in EntityArray:
#                      EntityArray.append(data[2])

#                  courses=data[3].strip('[]').split(',')    
#                  if courses not in EntityArray:
#                      EntityArray.append(courses)   

#                  if data[4] not in EntityArray:
#                      EntityArray.append(data[4])    

#                  clubs=data[5].strip('[]').split(',')     
#                  if clubs not in EntityArray:
#                      EntityArray.append(clubs)   















        # with open(file_path, 'r') as file:
        #  for line in file:
        #     data = line.strip().split(',')
        #     studentName = data[0]
        #     rollNumber = data[1]
        #     department = data[2]
        #     courses = data[3].strip('[]').split(',')
        #     hostel = data[4]
        #     clubs = data[5].strip('[]').split(',')

        #     student_record = StudentRecord(studentName, rollNumber)

        #     # Check if the department entity already exists
        #     department_entity = None
        #     for entity in EntityArray:
        #         if entity.get_name() == department:
        #             department_entity = entity
        #             break

        #     # If the department entity doesn't exist, create it and add to EntityArray
        #     if not department_entity:
        #         department_entity = LinkedList()
        #         department_entity.set_name(department)
        #         EntityArray.append(department_entity)

        #     # Add the student record to the department entity
        #     department_entity.add_student(student_record)

        #     # Check if the course entities already exist
        #     for course_name in courses:
        #         course_entity = None
        #         for entity in EntityArray:
        #             if entity.get_name() == course_name:
        #                 course_entity = entity
        #                 break

        #         # If the course entity doesn't exist, create it and add to EntityArray
        #         if not course_entity:
        #             course_entity = LinkedList()
        #             course_entity.set_name(course_name)
        #             EntityArray.append(course_entity)

        #         # Add the student record to the course entity
        #         course_entity.add_student(student_record)

        #     # Check if the hostel entity already exists
        #     hostel_entity = None
        #     for entity in EntityArray:
        #         if entity.get_name() == hostel:
        #             hostel_entity = entity
        #             break

        #     # If the hostel entity doesn't exist, create it and add to EntityArray
        #     if not hostel_entity:
        #         hostel_entity = LinkedList()
        #         hostel_entity.set_name(hostel)
        #         EntityArray.append(hostel_entity)

        #     # Add the student record to the hostel entity
        #     hostel_entity.add_student(student_record)

        #     # Check if the club entities already exist
        #     for club_name in clubs:
        #         club_entity = None
        #         for entity in EntityArray:
        #             if entity.get_name() == club_name:
        #                 club_entity = entity
        #                 break

        #         # If the club entity doesn't exist, create it and add to EntityArray
        #         if not club_entity:
        #             club_entity = LinkedList()
        #             club_entity.set_name(club_name)
        #             EntityArray.append(club_entity)

        #         # Add the student record to the club entity
        #         club_entity.add_student(student_record)
             


             



       
           
    




