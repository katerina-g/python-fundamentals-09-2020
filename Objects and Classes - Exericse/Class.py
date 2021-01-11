class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if Class.__students_count > len(self.students):
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)

    def __repr__(self):
        student_as_str = ', '.join(self.students)
        grade = self.get_average_grade()
        return f"The students in {self.name}: {student_as_str}. Average grade: {grade:.2f}"



