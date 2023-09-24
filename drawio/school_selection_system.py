class SchoolSystem:
    def __init__(self):
        self.universities = []

    def addUniversity(self, university):
        self.universities.append(university)

    def removeUniversity(self, university):
        self.universities.remove(university)

    def allocateSlot(self, student):
        for university in self.universities:
            if university.isSlotAvailable() and university.isEligible(student):
                university.addStudent(student)
                break


class University:
    def __init__(self, name, grade, capacity, cutoffScore):
        self.name = name
        self.grade = grade
        self.capacity = capacity
        self.slotsFilled = 0
        self.students = []
        self.cutoffScore = cutoffScore

    def getName(self):
        return self.name

    def getGrade(self):
        return self.grade

    def getCapacity(self):
        return self.capacity

    def getSlotsFilled(self):
        return self.slotsFilled

    def addStudent(self, student):
        self.students.append(student)
        self.slotsFilled += 1

    def removeStudent(self, student):
        self.students.remove(student)
        self.slotsFilled -= 1

    def isSlotAvailable(self):
        return self.slotsFilled < self.capacity

    def isEligible(self, student):
        return student.getGrade() >= self.cutoffScore


class Student:
    def __init__(self, name, program, grade):
        self.name = name
        self.program = program
        self.grade = grade

    def getName(self):
        return self.name

    def getProgram(self):
        return self.program

    def getGrade(self):
        return self.grade


# Sample use cases
system = SchoolSystem()

# Create universities
university1 = University("University A", 'A', 6, 80)
university2 = University("University B", 'B', 3, 75)
university3 = University("University C", 'C', 1, 70)

system.addUniversity(university1)
system.addUniversity(university2)
system.addUniversity(university3)

# Create students
student1 = Student("John", "Computer Science", 85)
student2 = Student("Sarah", "Mathematics", 78)
student3 = Student("Michael", "Physics", 73)
student4 = Student("Emily", "Chemistry", 81)
student5 = Student("David", "Biology", 77)
student6 = Student("Sophia", "English", 88)
student7 = Student("Daniel", "History", 83)
student8 = Student("Olivia", "Art", 76)
student9 = Student("James", "Economics", 79)
student10 = Student("Emma", "Sociology", 82)

# Allocate slots to students
system.allocateSlot(student1)
system.allocateSlot(student2)
system.allocateSlot(student3)
system.allocateSlot(student4)
system.allocateSlot(student5)
system.allocateSlot(student6)
system.allocateSlot(student7)
system.allocateSlot(student8)
system.allocateSlot(student9)
system.allocateSlot(student10)

# Print allocated slots for each university
for university in system.universities:
    print(f"University: {university.getName()}")
    print(f"Grade: {university.getGrade()}")
    print(f"Capacity: {university.getCapacity()}")
    print(f"Slots Filled: {university.getSlotsFilled()}")
    print("Students:")
    for student in university.students:
        print(
            f"- Name: {student.getName()} | Program: ({student.getProgram()}) | Score: ({student.getGrade()})")
    print("\n")
