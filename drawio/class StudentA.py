class Student:
    def __init__(self, student_id, student_name, student_grade, student_score):
        self.student_id = student_id
        self.student_name = student_name
        self.student_grade = student_grade
        self.student_score = student_score
        self.chosen_program = None

class University:
    def __init__(self, university_id, university_name, university_grade, total_slots):
        self.university_id = university_id
        self.university_name = university_name
        self.university_grade = university_grade
        self.total_slots = total_slots
        self.slots_filled = 0

class SchoolSelectionSystem:
    def __init__(self):
        self.students = []
        self.universities = []

    def add_student(self, student):
        self.students.append(student)

    def add_university(self, university):
        self.universities.append(university)

    def assign_universities(self):
        for student in self.students:
            if student.chosen_program:
                continue  # Skip students who have already been assigned.

            suitable_universities = [u for u in self.universities if u.university_grade == student.student_grade]
            suitable_universities.sort(key=lambda u: u.slots_filled)

            if suitable_universities:
                university = suitable_universities[0]
                if university.slots_filled < university.total_slots:
                    student.chosen_program = "Your Chosen Program"  # Replace with actual program logic.
                    university.slots_filled += 1
                    print(f"Assigned {student.student_name} to {university.university_name} for {student.chosen_program}.")
                else:
                    print(f"No available slots in suitable universities for {student.student_name}.")
            else:
                print(f"No suitable universities found for {student.student_name}.")

# Example usage:
system = SchoolSelectionSystem()

# Add universities
system.add_university(University(1, "University A", "A", 2))
system.add_university(University(2, "University B", "B", 3))
system.add_university(University(3, "University C", "C", 1))

# Add students
system.add_student(Student(101, "Alice", "A", 95))
system.add_student(Student(102, "Bob", "B", 85))
system.add_student(Student(103, "Charlie", "C", 75))

# Assign universities to students
system.assign_universities()
