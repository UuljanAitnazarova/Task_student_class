
class Student:
    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance

    def get_student_info(self):
        return '{self.name} {self.lastname} studies at {self.department} department from year {self.year_of_entrance}'.format(self=self)

student1 = Student('Vasya', 'Ivanov', 'Software engineering', 2017)
student2 = Student('Anna', 'Petrova', 'Data Science', 2020)
print(student1.get_student_info())
print(student2.get_student_info())