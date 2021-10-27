import time  # Time imported to add delays


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

    # Method to Search for email in registered students
    def email_search(self, email):
        for student in self.studentlist:
            # If parameter is equal to a email value within student list, return student
            if student.email == email:
                return student
            # returns tuple with one item only, helps keep else statement in menu cleaner
        return None,

    # Method to Search for ph2
    #one number in registered students
    def student_num_search(self, studentnumber):
        for student in self.studentlist:
            # If parameter is equal to a student number value within student list,
            # returns a tuple containing a Bool indicating if a match was found, and first and last name of the student
            if student.studentnumber == studentnumber:
                return student
            # returns tuple with one item only, helps keep else statement in menu cleaner
        return None,

    # Method to return full detailed list of registered students
    def student_full_list(self):
        return self.studentlist

    # Methond to return List of registered students, first/last name and status
    def student_status_list(self):
        statuslist = []
        for student in self.studentlist:
            statuslist.append(student.fname + " " + student.lname + " " + student.status)
        return statuslist

    #Method to update info on student list
    def update_student(self, student, choice, value):
        if choice == 1:
            student.fname = value
        if choice == 2:
            student.lname = value
        if choice == 3:
            student.dob = value
        if choice == 4:
            student.address = value
        if choice == 5:
            student.email = value
        if choice == 6:
            student.mobile = value
        if choice == 7:
            student.studentnumber = value
        if choice == 8:
            student.status = value



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
    clear_screen()
    print("Please enter the students info below, and hit enter\n")
    fname = input("First Name : ")
    lname = input("Last Name : ")
    dob = input("Date of Birth : ")
    address = input("Address : ")
    email = input("Email Address : ")
    phone = input("Phone Number : ")
    studentnum = input("Student Number : ")
    status = input("Registration Status (EL/RE only) : ")

    TU257.studentlist.append(Student(fname, lname, dob, address, email, phone, studentnum, status))

    print("*** Student Successfully Registered ***")
    time.sleep(2)


def menu_option2():
    clear_screen()
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
        result = TU257.email_search(email)
        if result == None:
            print("Match Not Found!")
            time.sleep(2)

        else:
            clear_screen()
            print(f"Match Found! - This Email belongs to : {result.fname} {result.lname}")
            time.sleep(2)
            print("Would you like to Update or Delete this entry? \n 1: Update\n 2: Delete")
            usrinput = int(input("Enter Choice: "))
            #Adding conditional choice based on user input
            if usrinput == 1:
                print("""Please select which attribute you would like to update:
                1. First Name
                2. Last Name
                3. DOB
                4. Address
                5. Email
                6. Mobile Number
                7. Student Number
                8. Registration Status
                """)
                usrchoice = int(input("Choice : "))
                updatedInfo = input("Please input replacement value for this field: ")
                #Calls Method to update the student attribute selected by user (usrchoice)
                #with the new info, inputted by user (updatedInfo)
                TU257.update_student(result,usrchoice,updatedInfo)

            elif usrinput == 2:
                TU257.studentlist.remove(result)
                print(f"{result.fname} {result.lname} - Has been Removed")
                time.sleep(2)
            else:
                print("Incorrect Choice - Returning to Menu")
                time.sleep(2)
                menu_option2()

    if userinput == 2:
        print("Student Number Search Selected")
        studentnum = input("Please enter Student Number: ")
        result = TU257.student_num_search(studentnum)

        if result == None:
            print("Match Not Found!")
            time.sleep(2)

        else:
            clear_screen()
            print(f"Match Found! - This Student Number belongs to : {result.fname} {result.lname}")
            time.sleep(2)
            print("Would you like to Update or Delete this entry? \n 1: Update\n 2: Delete")
            usrinput = int(input("Enter Choice: "))

            #Adding conditional choice based on user input
            if usrinput == 1:
                print("""Please select which attribute you would like to update:
                1. First Name
                2. Last Name
                3. DOB
                4. Address
                5. Email
                6. Mobile Number
                7. Student Number
                8. Registration Status
                """)
                usrchoice = int(input("Choice : "))
                updatedInfo = input("Please input replacement value for this field: ")

                TU257.update_student(result,usrchoice,updatedInfo)



            elif usrinput == 2:
                TU257.studentlist.remove(result)
                print(f"{result.fname} {result.lname} - Has been Removed")
                time.sleep(2)
            else:
                print("Incorrect Choice - Returning to Menu")
                time.sleep(2)
                menu_option2()


def menu_option3():
    clear_screen()
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
        print(f"Number of Students Registered is : {TU257.get_course_count()}")
        time.sleep(2)
        menu_option3()
    elif userinput == 2:
        print(f"Number of Students with RE status is : {TU257.get_re_count()}")
        time.sleep(2)
        menu_option3()
    elif userinput == 3:
        print(f"Number of Students with EL status is : {TU257.get_el_count()}")
        time.sleep(2)
        menu_option3()
    elif userinput == 4:
        print("First Name - Last Name - Status")
        for i in TU257.student_status_list():
            print(i)
        time.sleep(2)
        menu_option3()
    elif userinput == 5:
        print(
            "First Name - Last Name - DOB - Student Address - Student Email - Student Mobile - Student Number - Student Status")
        for student in TU257.student_full_list():
            print(student.fname, student.lname, student.dob, student.address, student.email,
                  student.mobile, student.studentnumber, student.status, sep="\t")
        time.sleep(2)
        menu_option3()


def clear_screen():
    for i in range(24):
        print()



# initialising empty student list
TU257_student_list = []

# TEST CODE BELOW
student1 = Student("Andrew", "Owens", "08/06/96", "Celbridge", "andrew.owens121@gmail.com", "0874556013", "C14363641",
                   "EL")
student2 = Student("MaryAnn", "Jones", "18/09/96", "Leixlip", "MJones55@gmail.com", "0873164013", "C15363641", "EL")
student3 = Student("Patrick", "Peterson", "14/07/95", "Lucan", "PPLucan@gmail.com", "0874553845", "C16363641", "EL")
student4 = Student("Janet", "O'Reilly", "15/10/84", "Blanch", "JOrielly@gmail.com", "0862232134", "C17363641", "RE")
TU257_student_list = [student1, student2, student3, student4]
# TEST CODE ABOVE

# Creating a course object
TU257 = Course("Fund. of Data Science", "TU257", "Jon McCarthy", TU257_student_list)

# loop to continue until course is full
while len(TU257.studentlist) < 30:
    clear_screen()
    main_menu()
# else displays that course is full when list reaches 30
else:
    print("Course at Full Capacity!")
