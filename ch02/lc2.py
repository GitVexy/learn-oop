class Student:
    def __init__(self, name):
        self.__courses = {}
        self.name = name

    def calculate_letter_grade(self, score):
        if score < 60:
            return "F"
        elif score < 70:
            return "D"
        elif score < 80:
            return "C"
        elif score < 90:
            return "B"
        return "A"

    def add_course(self, course_name, score):
        self.__courses[course_name] = self.calculate_letter_grade(score)

    def get_courses(self):
        return self.__courses
