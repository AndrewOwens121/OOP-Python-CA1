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
    # initialise Course Class, assigning the required parameters to attributes as per below
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

    # Method to return number of registered on course
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

    # Method to Search for email in registered students, parameter is user inputted email address
    def email_search(self, email):
        for student in self.studentlist:
            # If parameter is equal to a email value within student list, return student
            if student.email == email:
                return student
        return None

    # Method to Search for phone number in registered students
    def student_num_search(self, studentnumber):
        for student in self.studentlist:
            # If parameter is equal to a student number value within student list, returns that student
            if student.studentnumber == studentnumber:
                return student
        return None

    # Method to return full detailed list of registered students
    def student_full_list(self):
        return self.studentlist

    # Method to return List of registered students, first/last name and status
    def student_status_list(self):
        statuslist = []
        for student in self.studentlist:
            statuslist.append(student.fname + " " + student.lname + " " + student.status)
        return statuslist

    # Method to update info on student list
    def set_update(self, student, choice, value):
        """
        Method to Update a particular attribute within a student from studentlist
        :param student: Accepts student found via search
        :param choice: Stores user choice, as to which attribute is to be changed
        :param value: Stores user input as to what the new value of the attribute is
        :return: None
        """
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
    """
    Function to help organise the Menu System
    :return: None
    """
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
    """
    Function to help organise the Menu System
    :return: None
    """
    clear_screen()  # Clears screen to make using program easier

    # Below prompts user for input to required student info
    print("Please enter the students info below, and hit enter\n")
    fname = input("First Name : ")
    lname = input("Last Name : ")
    dob = input("Date of Birth : ")
    address = input("Address : ")
    email = input("Email Address : ")
    phone = input("Phone Number : ")
    studentnum = input("Student Number : ")
    status = input("Registration Status (EL/RE only) : ")

    # Appends student to the list featuring info inputted by user above
    TU257.studentlist.append(Student(fname, lname, dob, address, email, phone, studentnum, status))

    print("*** Student Successfully Registered ***")
    time.sleep(2)  # pauses screen to help user read message


def menu_option2():
    """
    Function to help organise the Menu System
    :return: None
    """
    clear_screen()  # Clears screen to make using program easier
    print("Please Choose from one of the search options below\n"
          "1: Email Address\n"
          "2. Student Number\n"
          "0. Go Back to Main Menu\n")

    userinput = int(input(": "))

    if userinput == 0:
        print("Main Menu Selected")
        time.sleep(1)
        main_menu()

    if userinput == 1:
        print("Email Search Selected")
        email = input("Please enter email address: ")

        # passes the email inputted by user to the email_search method in Course class
        student = TU257.email_search(email)

        # None is returned by method if no match found
        if student == None:
            print("Match Not Found!")
            time.sleep(2)

        # if match is found
        else:
            clear_screen()
            print(f"Match Found! - This Email belongs to : {student.fname} {student.lname}")
            time.sleep(2)

            # prompting user if they want to choose between Update and Delete Methods
            print("Would you like to Update or Delete this entry? \n 1: Update\n 2: Delete")
            usrinput = int(input("Enter Choice: "))

            # Adding conditional choice based on user input
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

                # Calls Method to update the student attribute selected by user (usrchoice)
                # with the new info, inputted by user (updatedInfo) - 'result' is the student being updated
                TU257.set_update(student, usrchoice, updatedInfo)

            elif usrinput == 2:
                TU257.studentlist.remove(student)
                print(f"{student.fname} {student.lname} - Has been Removed")
                time.sleep(2)
            else:
                print("Incorrect Choice - Returning to Menu")
                time.sleep(2)
                menu_option2()

    if userinput == 2:
        print("Student Number Search Selected")
        studentnum = input("Please enter Student Number: ")
        student = TU257.student_num_search(studentnum)

        if student == None:
            print("Match Not Found!")
            time.sleep(2)

        else:
            clear_screen()
            print(f"Match Found! - This Student Number belongs to : {student.fname} {student.lname}")
            time.sleep(2)
            print("Would you like to Update or Delete this entry? \n 1: Update\n 2: Delete")
            usrinput = int(input("Enter Choice: "))

            # Adding conditional choice based on user input
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

                TU257.set_update(student, usrchoice, updatedInfo)



            elif usrinput == 2:
                TU257.studentlist.remove(student)
                print(f"{student.fname} {student.lname} - Has been Removed")
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
# student1 = Student("First", "Ireem", "08/05/96", "New York", "Catcher@gmail.com", "08776556013", "X14363641",
#                    "EL")
# student2 = Student("MaryAnn", "Jones", "18/09/96", "Boston", "MJones55@gmail.com", "0873164013", "R15363641", "EL")
# student3 = Student("Patrick", "Peterson", "14/07/95", "Abu Dhabi", "PPLucan@gmail.com", "0874553845", "D16363641", "EL")
# student4 = Student("Janet", "O'Reilly", "15/10/84", "Sydney", "JOrielly@gmail.com", "0862232134", "L17363641", "RE")
# TU257_student_list = [student1, student2, student3, student4]
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
