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


def main_menu():
    print("Please Choose from one of the below options\n"
          "1: Register Student\n"
          "2. Search Registered Students\n"
          "3. Queries\n"
          "0. Exit Program")
    userinput=int(input(": "))
    if userinput == 0:
        print("Program Terminated")
        return
    elif userinput ==1:
        print("Menu Option 1")
    elif userinput ==2:
        print("Menu Option 2")
    elif userinput ==3:
        print("Menu Option 3")
    else:
        print("Invalid Input!")


#initialising empty student list
student_list =[]

#Creating a course object
course1=Course("Fund. of Data Science","TU257","Jon McCarthy",student_list)

# loop to continue until course is full
while len(student_list) <30:
    main_menu()
# else displays that course is full when list reaches 30
else:
    print("Course at Full Capacity!")