class SchoolSystem:
    def __init__(self):
        self.universities = []

    def add_university(self, university):
        self.universities.append(university)

    def remove_university(self, university):
        self.universities.remove(university)

    def allocate_slot(self, student):
        for uni in self.universities:
            if uni.is_slot_available() and uni.is_eligible(student):
                uni.add_student(student)
                break


class University:
    def __init__(self, name, grade, capacity, cutoff_score):
        self.name = name
        self.grade = grade
        self.capacity = capacity
        self.slots_filled = 0
        self.students = []
        self.cutoff_score = cutoff_score

    def get_name(self):
        return self.name

    def get_grade(self):
        return self.grade

    def get_capacity(self):
        return self.capacity

    def get_slots_filled(self):
        return self.slots_filled

    def add_student(self, stud):
        self.students.append(stud)
        self.slots_filled += 1

    def remove_student(self, stud):
        self.students.remove(stud)
        self.slots_filled -= 1

    def is_slot_available(self):
        return self.slots_filled < self.capacity

    def is_eligible(self, stud):
        return stud.get_grade() >= self.cutoff_score


class Student:
    def __init__(self, name, program, grade):
        self.name = name
        self.program = program
        self.grade = grade

    def get_name(self):
        return self.name

    def get_program(self):
        return self.program

    def get_grade(self):
        return self.grade


# Sample use cases
system = SchoolSystem()

# Create universities
university1 = University("University of Ghana", 'A', 6, 80)
university2 = University("University of Winneba", 'B', 3, 75)
university3 = University("Methodist University", 'C', 1, 70)

system.add_university(university1)
system.add_university(university2)
system.add_university(university3)

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
system.allocate_slot(student1)
system.allocate_slot(student2)
system.allocate_slot(student3)
system.allocate_slot(student4)
system.allocate_slot(student5)
system.allocate_slot(student6)
system.allocate_slot(student7)
system.allocate_slot(student8)
system.allocate_slot(student9)
system.allocate_slot(student10)

# Print allocated slots for each university
for uni in system.universities:
    print(f"University: {uni.get_name()}")
    print(f"Grade: {uni.get_grade()}")
    print(f"Capacity: {uni.get_capacity()}")
    print(f"Slots Filled: {uni.get_slots_filled()}")
    print("Students:")
    for student in uni.students:
        print(
            f"- Name: {student.get_name()} | Program: ({student.get_program()}) | Score: ({student.get_grade()})")
    print("\n")



