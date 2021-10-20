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



#initialising empty student list
student_list =[]

#Creating a course object
course1=Course("Fund. of Data Science","TU257","Jon McCarthy",student_list)

# loop to continue until course is full
while len(student_list) <30:
    print()
# else displays that course is full when list reaches 30
else:
    print("Course at Full Capacity!")