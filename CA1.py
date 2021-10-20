class Student:
    #initialise Student Class, assigning the required parameters to attributes as per below
    def __init__(self,new_fname,new_lname,new_dob, new_address,new_email,new_mobilenum, new_studentnum, new_status):
        self.fname = new_fname
        self.lname = new_lname
        self.dob = new_dob
        self.address = new_address
        self.email = new_email
        self.mobile = new_mobilenum
        self.studentnumber = new_studentnum
        self.status = new_status