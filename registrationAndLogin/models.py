from django.db import models


class SchoolSystem(models.Model):
    universities = models.ManyToManyField('University')

    def add_university(self, university):
        self.universities.add(university)

    def remove_university(self, university):
        self.universities.remove(university)

    def allocate_slot(self, student):
        for uni in self.universities.all():
            if uni.is_slot_available() and uni.is_eligible(student):
                uni.add_student(student)
                break


class University(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    capacity = models.IntegerField()
    slots_filled = models.IntegerField(default=0)
    cutoff_score = models.IntegerField()

    def __str__(self):
        return (f"name: {self.get_name()} | grade: {self.get_grade()} | slots available: {self.get_capacity()} "
                f"| slots filled: {self.get_slots_filled()} | cutoff score: {self.cutoff_score}")

    def get_name(self):
        return self.name

    def get_grade(self):
        return self.grade

    def get_capacity(self):
        return self.capacity

    def get_slots_filled(self):
        return self.slots_filled

    def add_student(self, student):
        self.students.append(student)
        self.slots_filled += 1

    def remove_student(self, student):
        self.students.remove(student)
        self.slots_filled -= 1

    def is_slot_available(self):
        return self.slots_filled < self.capacity

    def is_eligible(self, student):
        return student.get_grade() >= self.cutoff_score


class Student(models.Model):
    name = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} | {self.program} | {self.grade}"

    def get_name(self):
        return f"{self.name}"

    def get_program(self):
        return f"{self.program}"

    def get_grade(self):
        return f"{self.grade}"
