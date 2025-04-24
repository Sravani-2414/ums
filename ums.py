from otp_module import send_otp
import pyttsx3
 
def speak(text):
     engine = pyttsx3.init()
     engine.say(text)
     engine.runAndWait()
 
 
colleges = []
 
class person:
     def __init__(self, rollno, name, email):
         self.rollno = rollno
         self.name = name
         self.email = email
 
class student(person):
     def __init__(self, rollno, name, branch, email):
         super().__init__(rollno, name, email)
         self.branch = branch
 
class teacher(person):
     def __init__(self, rollno, name, subject, email):
         super().__init__(rollno, name, email)
         self.subject = subject
 
class college:
     def __init__(self, clg_id, clg_name):
         self.clg_id = clg_id
         self.clg_name = clg_name
         self.students = []
         self.teachers = []
 
     def add_student(self, student):
         self.students.append(student)
 
     def add_teacher(self, teacher):
         self.teachers.append(teacher)
 
print("Welcome to College Management System!\n")
 
while True:
     print("1. Add College")
     print("2. Add Student")
     print("3. Add Teacher")
     print("4. Login as Student")
     print("5. Login as Teacher")
     print("6. Exit")
 
     x = int(input("Enter Your Choice: "))
 
     if x == 1:
         clg_id = int(input("Enter College Id: "))
         if not any(c.clg_id == clg_id for c in colleges):
             clg_name = input("Enter College Name: ")
             speak("Enter College Name")
             colleges.append(college(clg_id, clg_name))
             print("College Added Successfully!\n")
             speak("College Added Successfully")
         else:
             print("College Already Exists!\n")
 
     elif x == 2:
         clg_id = int(input("Enter College Id: "))
         college_obj = next((c for c in colleges if c.clg_id == clg_id), None)
         if college_obj:
             roll = int(input("Enter Student Roll No: "))
             name = input("Enter Student Name: ")
             branch = input("Enter Branch: ")
             email = input("Enter Email: ")
             s = student(roll, name, branch, email)
             college_obj.add_student(s)
             print("Student Added Successfully!\n")
             speak("Added successfully")
         else:
             print("College Not Found!\n")
             speak(" Please Reenter college ID correctly") 
 
     elif x == 3:
         clg_id = int(input("Enter College Id: "))
         college_obj = next((c for c in colleges if c.clg_id == clg_id), None)
         if college_obj:
             roll = int(input("Enter Teacher Roll No: "))
             name = input("Enter Teacher Name: ")
             subject = input("Enter Subject: ")
             email = input("Enter Email: ")
             t = teacher(roll, name, subject, email)
             college_obj.add_teacher(t)
             print("Teacher Added Successfully!\n")
             speak("Added successfully")
         else:
             print("College Not Found!\n")
             speak("Please enter college ID correctly") 
 
     elif x == 4:
         email = input("Enter Student Email: ")
         if send_otp(email):
             print("Login Successful!\n")
             speak("Login successful")
         else:
             print("Login Failed!\n")
             speak("Login failed")
 
     elif x == 5:
         email = input("Enter Teacher Email: ")
         if send_otp(email):
             print("Login Successful!\n")
             speak("Login successful")
         else:
             print("Login Failed!\n")
             speak("Login failed")
 
     elif x == 6:
         print("\nThank you, Visit Again!")
         speak(" Thank you, Visit Again!")
         break
 
     else:
         print("Invalid Choice!\n")
