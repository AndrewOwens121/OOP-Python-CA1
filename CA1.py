class Student:
    # initialise Student Class, assigning the required parameters to attributes as per below
    def __init__(self, new_fname, new_lname, new_dob, new_address, new_email, new_mobilenum, new_studentnum,
                 new_status):
        self.fname = new_fname
        self.lname = new_lname
        self.dob = new_dob
        self.address = new_address
        self.email = new_email
        self.mobile = new_mobilenum
        self.studentnumber = new_studentnum
        self.status = new_status

    # Method to return status of individual student
    def get_status(self):
        return self.status


class Course:
    def __init__(self, new_title, new_code, new_chair, new_studentlist):
        self.title = new_title
        self.coursecode = new_code
        self.chairperson = new_chair
        self.studentlist = new_studentlist

    # Method to return the course title
    def get_course_title(self):
        return self.title

    # Method to return course code
    def get_course_code(self):
        return self.coursecode

    # Method to return number of registerd on course
    def get_course_count(self):
        return len(self.studentlist)

    # Method to return number of registered on course
    def get_re_count(self):
        count = 0
        for student in self.studentlist:
            if student.status == "RE":
                count += 1
        return count

    # Method to return number of eligible on course
    def get_el_count(self):
        count = 0
        for student in self.studentlist:
            if student.status == "EL":
                count += 1
        return count

    # Method to return full detailed list of registered students
    def student_full_list(self):
        return self.studentlist

    # Methond to return List of registered students, first/last name and status
    def student_status_list(self):
        return self.studentlist


def main_menu():
    print("Please Choose from one of the below options\n"
          "1: Register Student\n"
          "2. Search Registered Students\n"
          "3. Queries\n"
          "0. Exit Program")
    userinput = int(input(": "))
    if userinput == 0:
        print("Program Terminated")
        return
    elif userinput == 1:
        menu_option1()
    elif userinput == 2:
        menu_option2()
    elif userinput == 3:
        menu_option3()
    else:
        print("Invalid Input!")


def menu_option1():
    print("Please enter the students info below, and hit enter\n")
    fname = input("First Name : ")
    lname = input("Last Name : ")
    dob = input("Date of Birth : ")
    address = input("Address : ")
    email = input("Email Address : ")
    phone = input("Phone Number : ")
    studentnum = input("Student Number : ")
    status = input("Registration Status (EL/RE only) : ")

    course1.studentlist.append(Student(fname, lname, dob, address, email, phone, studentnum, status))

    print("*** Student Successfully Registered ***")


def menu_option2():
    print("Please Choose from one of the search options below\n"
          "1: Email Address\n"
          "2. Student Number\n"
          "0. Go Back to Main Menu\n")

    userinput = int(input(": "))

    if userinput == 0:
        print("Main Menu Selected")
        main_menu()

    if userinput == 1:
        print("Email Search Selected")
        email = input("Please enter email address: ")
        # Add function to search for email

    if userinput == 2:
        print("Student Number Search Selected")
        studentnum = input("Please enter Student Number: ")
        # Add function to search for email


def menu_option3():
    print("Please Choose from one of the Queries Below:\n"
          "1: Number of Students Registered\n"
          "2. Number of Students with status RE\n"
          "3. Number of Students with status EL\n"
          "4. List of Registered students and Status\n"
          "5. Full Student Details\n"
          "0. Go Back to Main Menu")
    userinput = int(input(": "))
    if userinput == 0:
        print("Main Menu Selected")
        main_menu()
    elif userinput == 1:
        print(course1.get_course_count())
        # add functionality
    elif userinput == 2:
        print(course1.get_re_count())
        # add functionality
    elif userinput == 3:
        print(course1.get_el_count())
        # add functionality
    elif userinput == 4:
        for i in course1.student_status_list():
            print(i)
    elif userinput == 5:
        for student in course1.student_full_list():
            print(student.fname, student.lname, student.dob, student.address, student.email,
                  student.mobile, student.studentnumber, student.status, sep="\t")


# initialising empty student list
course1_student_list = []

# TESTING
student1 = Student("Andrew", "Owens", "08/06/96", "Celbridge", "andrew.owens121@gmail.com", "0874556013", "C14363641",
                   "EL")
student2 = Student("MaryAnn", "Jones", "18/09/96", "Leixlip", "MJones55@gmail.com", "0873164013", "C15363641", "EL")
student3 = Student("Patrick", "Peterson", "14/07/95", "Lucan", "PPLucan@gmail.com", "0874553845", "C16363641", "EL")
student4 = Student("Janet", "O'Reilly", "15/10/84", "Blanch", "JOrielly@gmail.com", "0862232134", "C17363641", "RE")
course1_student_list = [student1, student2, student3, student4]

# Creating a course object
course1 = Course("Fund. of Data Science", "TU257", "Jon McCarthy", course1_student_list)

# loop to continue until course is full
while len(course1.studentlist) < 30:
    main_menu()
# else displays that course is full when list reaches 30
else:
    print("Course at Full Capacity!")
