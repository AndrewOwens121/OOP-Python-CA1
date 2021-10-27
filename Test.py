class Student:
    # initialise Student Class, assigning the required parameters to attributes as per below
    def __init__(self, new_fname, new_lname):
        self.fname = new_fname
        self.lname = new_lname

class Course:
    def __init__(self, new_studentlist):
        self.studentlist = new_studentlist


student1 = Student("Andrew", "Owens")
student2 = Student("MaryAnn", "Jones")
student3 = Student("Patrick", "Peterson")
student4 = Student("Janet", "O'Reilly")

TU257_student_list = [student1, student2, student3, student4]

TU257 = Course(TU257_student_list)

print(TU257_student_list)
