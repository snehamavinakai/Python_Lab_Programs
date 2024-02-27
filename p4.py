class Student:

    def s_info(self):
        self.name = input("Enter a Student name : ")
        self.reg_no = int(input("Enter reg_no : "))
        self.sem = int(input("Enter semester : "))
        self.section = input("Enter a section : ")
        
    def cal(self):
        self.m1 = int(input("Enter maths marks : "))
        self.m2 = int(input("Enter stat marks : "))
        self.m3 = int(input("Enter java marks : "))
        self.m4 = int(input("Enter python marks : "))

        self.total = self.m1+self.m2+self.m3+self.m4
        
        self.res = self.total/4
        
#displaying student information
    def display(self):
        self.s_info()
        self.cal()
        print("** STUDENT INFORMATION **")
        print("Name = ",self.name)
        print("Reg_No = ",self.reg_no)
        print("Semester = ",self.sem)
        print("Section = ",self.section)
        print("  Marks Scored in each subject :")
        print("Maths = ",self.m1)
        print("Stat = ",self.m2)
        print("Java = ",self.m3)
        print("Python = ",self.m4)
        print("Total marks = ",self.total)
        print("Percentage = ",self.res)
        if self.res >= 85:
            print("Grade : A")
        elif self.res >= 75:
            print("Grade :B")
        elif self.res >= 65:
            print("Grade :C")
        elif self.res >= 55:
            print("Grade :D") 
        elif self.res >= 45:
            print("Grade :E") 
        else:
            print("Grade :Failed") 

            

#creating objects
s1 = Student()
s2 = Student()
s1.display()
s2.display()
