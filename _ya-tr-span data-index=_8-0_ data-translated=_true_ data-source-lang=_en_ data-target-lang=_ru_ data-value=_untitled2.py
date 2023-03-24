class Student:
    def __init__(self, name, surname, age, address, phone):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.phone = phone
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def get_courses(self):
        return self.courses

class Course:
    def __init__(self, name, teacher, description, duration):
        self.name = name
        self.teacher = teacher
        self.description = description
        self.duration = duration
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_students(self):
        return self.students

class Curriculum:
    def __init__(self, courses):
        self.courses = courses
        self.students = []

    def add_student_to_course(self, student, course):
        course.add_student(student)
        student.add_course(course)
        self.students.append(student)

    def get_all_students(self):
        return self.students
