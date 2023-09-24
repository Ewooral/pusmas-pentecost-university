class Student:
    def __init__(self, student_id, student_name, student_score, chosen_program=None):
        self.student_id = student_id
        self.student_name = student_name
        self.student_score = student_score
        self.chosen_program = chosen_program

    def determine_grade(self):
        """Determines the student's grade based on their score."""
        if self.student_score >= 90:
            return "A"
        elif self.student_score >= 80:
            return "B"
        elif self.student_score >= 70:
            return "C"
        elif self.student_score >= 60:
            return "D"
        else:
            return "F"

class University:
    def __init__(self, university_id, university_name, university_grade, total_slots):
        self.university_id = university_id
        self.university_name = university_name
        self.university_grade = university_grade
        self.total_slots = total_slots
        self.slots_filled = 0

class StudentUniversityAssignment:
    def __init__(self, assignment_id, student, university, program_id):
        self.assignment_id = assignment_id
        self.student = student
        self.university = university
        self.program_id = program_id

def assign_student_to_university(student, universities):
    """Assigns a student to a university based on their grade and the grade of the university, taking into account the availability of slots."""
    student_grade = student.determine_grade()

    suitable_universities = [u for u in universities if u.university_grade == student_grade]
    suitable_universities.sort(key=lambda u: u.slots_filled)

    if not suitable_universities:
        suitable_universities = [u for u in universities if u.university_grade == chr(ord(student_grade) + 1)]

    if suitable_universities:
        assigned_university = suitable_universities[0]
        if assigned_university.slots_filled < assigned_university.total_slots:
            student_university_assignment = StudentUniversityAssignment(None, student, assigned_university, student.chosen_program)
            assigned_university.slots_filled += 1
            return assigned_university, student_university_assignment

    return None, None

def main():
    print("School Selection System")
    
    student_id = int(input("Enter Student ID: "))
    student_name = input("Enter Student Name: ")
    student_score = float(input("Enter Student Score: "))
    chosen_program = input("Enter Chosen Program: ")

    student = Student(student_id, student_name, student_score, chosen_program)

    universities = [
        University(1, "Harvard", "A", 100),
        University(2, "Stanford", "A", 100),
        University(3, "Yale", "D", 100),
        # Add more universities as needed.
    ]

    assigned_university, student_university_assignment = assign_student_to_university(student, universities)

    if assigned_university:
        print(f"Assigned {student.student_name} to {assigned_university.university_name} for {student.chosen_program}.")
    else:
        print(f"No available slots in suitable universities for {student.student_name}.")

if __name__ == "__main__":
    main()
