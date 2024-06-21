import sys

EntityArray = []

class StudentRecord:
    def __init__(self, studentName, rollNumber):
        self.studentName = studentName
        self.rollNumber = rollNumber

    def get_studentName(self):
        return self.studentName

    def set_studentName(self, name):
        self.studentName = name

    def get_rollNumber(self):
        return self.rollNumber

    def set_rollNumber(self, rollnum):
        self.rollNumber = rollnum


class Node:
    def __init__(self, element):
        self.next = None
        self.element = element

    def get_next(self):
        return self.next

    def get_element(self):
        return self.element

    def set_next(self, value):
        self.next = value

    def set_element(self, student):
        self.element = student


class Entity:
    def __init__(self, name):
        self.name = name
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


def read_input_file():
    with open('details.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            studentName = data[0]
            rollNumber = data[1]
            department = data[2]
            courses = data[3].strip('[]').split(',')
            hostel = data[4]
            clubs = data[5].strip('[]').split(',')

            student_record = StudentRecord(studentName, rollNumber)

            # Check if the department entity already exists
            department_entity = None
            for entity in EntityArray:
                if entity.get_name() == department:
                    department_entity = entity
                    break

            # If the department entity doesn't exist, create it and add to EntityArray
            if not department_entity:
                department_entity = LinkedList()
                department_entity.set_name(department)
                EntityArray.append(department_entity)

            # Add the student record to the department entity
            department_entity.add_student(student_record)

            # Check if the course entities already exist
            for course_name in courses:
                course_entity = None
                for entity in EntityArray:
                    if entity.get_name() == course_name:
                        course_entity = entity
                        break

                # If the course entity doesn't exist, create it and add to EntityArray
                if not course_entity:
                    course_entity = LinkedList()
                    course_entity.set_name(course_name)
                    EntityArray.append(course_entity)

                # Add the student record to the course entity
                course_entity.add_student(student_record)

            # Check if the hostel entity already exists
            hostel_entity = None
            for entity in EntityArray:
                if entity.get_name() == hostel:
                    hostel_entity = entity
                    break

            # If the hostel entity doesn't exist, create it and add to EntityArray
            if not hostel_entity:
                hostel_entity = LinkedList()
                hostel_entity.set_name(hostel)
                EntityArray.append(hostel_entity)

            # Add the student record to the hostel entity
            hostel_entity.add_student(student_record)

            # Check if the club entities already exist
            for club_name in clubs:
                club_entity = None
                for entity in EntityArray:
                    if entity.get_name() == club_name:
                        club_entity = entity
                        break

                # If the club entity doesn't exist, create it and add to EntityArray
                if not club_entity:
                    club_entity = LinkedList()
                    club_entity.set_name(club_name)
                    EntityArray.append(club_entity)

                # Add the student record to the club entity
                club_entity.add_student(student_record)


if __name__ == "__main__":
    # try:
    #     read_input_file("details.txt")
    # except:
    #     print("Could not read Sample Input File! Ensure that the file 'details.txt' is in the folder and try again!")
    #     sys.exit(1)
    read_input_file()

    failed_tests = 0

def test1():
    entity_name = "CSE"
    entity = ""
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    ite = entity.get_iterator()
    student = ""
    
    while(ite != None):
        if ite.get_element().studentName == "JohnDoe":
            student = ite.get_element()
            break
        ite = ite.get_next()

    assert student.studentName == "JohnDoe", "Student JohnDoe is not present in the CSE Entity"

def test2():
    entity_name = "EE"
    entity = ""
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    ite = entity.get_iterator()
    student = ""
    
    while(ite != None):
        if ite.get_element().studentName == "SanyaSharma":
            student = ite.get_element()
            break
        ite = ite.get_next()

    assert student.studentName == "SanyaSharma", "Student SanyaSharma is not present in the EE Entity"

def test3():
    entity_name = "DSA"
    entity = ""
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    ite = entity.get_iterator()
    size = 0
    
    while(ite != None):
        size += 1
        ite = ite.get_next()

    assert size == 20, "Incorrect count of records in DSA course"

def test4():
    entity_name = "Programming"
    entity = ""
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    ite = entity.get_iterator()
    size = 0
    
    while(ite != None):
        size += 1
        ite = ite.get_next()

    assert size == 20, "Incorrect count of records in Programming Club"

def test5():
    entity_name = "Toastmasters"
    entity = ""
    studentname = "RaviKumar"
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    entity.delete_student(studentname)
    ite = entity.get_iterator()
    
    if_exists = 0
    while(ite != None):
        if ite.get_element().studentName == studentname:
            if_exists = 1
            break
        ite = ite.get_next()

    assert if_exists == 0, "Record still exists, Delete function not working!"

def test6():
    entity_name = "Maths"
    entity = ""
    studentname = "UzumakiNaruto"
    studentroll = "B20CS011"
    student = StudentRecord()
    student.studentName = studentname
    student.rollNumber = studentroll

    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    entity.add_student(student)
    ite = entity.get_iterator()
    
    if_exists = 0
    while(ite != None):
        if ite.get_element().studentName == studentname:
            if_exists = 1
            break
        ite = ite.get_next()

    assert if_exists == 1, "Record is not added, Add Student Record function not working!"

def test7():
    entity_name = "PRML"
    entity = ""
    studentname = "HimashuGupta"
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    entity.delete_student(studentname)
    ite = entity.get_iterator()
    
    if_exists = 0
    while(ite != None):
        if ite.get_element().studentName == studentname:
            if_exists = 1
            break
        ite = ite.get_next()

    assert if_exists == 0, "Record still exists, Delete function not working!"

def test8():
    entity_name = "G5"
    entity = ""
    studentname = "UchihaSasuke"
    studentroll = "B20ES011"
    student = StudentRecord()
    student.studentName = studentname
    student.rollNumber = studentroll

    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    entity.add_student(student)
    ite = entity.get_iterator()
    
    if_exists = 0
    while(ite != None):
        if ite.get_element().studentName == studentname:
            if_exists = 1
            break
        ite = ite.get_next()

    assert if_exists == 1, "Record is not added, Add Student Record function not working!"

if __name__ == "__main__":
    
    unit_tests_list = [
        test1, test2, test3, test4, test5, test6,
        test7, test8
    ]
    total = len(unit_tests_list)
    try:
        read_input_file("Details.txt")
    except:
        print("Could not read Sample Input File! Ensure that the file 'details.txt' is in the folder and try again!")
        sys.exit(1)
        
    for i, test_fn in enumerate(unit_tests_list):
        try:
            test_fn()
        except Exception as e:
            failed_tests += 1
            print(f"Unit test #{i+1} failure: {str(e)}")

    if failed_tests == 0:
        print("All tests have passed successfully!")
    else:
        print(f"{failed_tests} tests failed!")
    sys.exit(failed_tests)
