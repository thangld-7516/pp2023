ListStudent = {}
ListCourse = {}
ListMark = {}

class Student:
    def __init__(self, IDStudent, NameStudent, DOB):
        self.IDStudent = IDStudent
        self.NameStudent = NameStudent
        self.DOB = DOB

    def InputStudent(self):
        NumOfStudent = int(input("Enter number of students in a class:"))
        for i in range(NumOfStudent):
            IDStudent = input("Enter ID:")
            NameStudent = input("Enter name:")
            DOB = input("Enter date of birth:")
            student = Student(IDStudent, NameStudent, DOB)
            ListStudent[IDStudent] = student

    def Display(self):
        for student in ListStudent.values():
            print(f"ID: {student.IDStudent}  Name: {student.NameStudent}  DOB: {student.DOB}")

class Course:
    def __init__(self, IDCourse, NameCourse):
        self.IDCourse = IDCourse
        self.NameCourse = NameCourse

    def InputCourse(self):
        NumOfCourse = int(input("enter the number of course:"))
        for i in range (NumOfCourse):
            IDCourse = input("enter ID of the course:")
            NameCourse = input("enter name of the course:")
            course = Course(IDCourse, NameCourse)
            ListCourse[IDCourse] = course

    def Display(self):
        for course in ListCourse.values():
            print(f"ID: {course.IDCourse}  Name: {course.NameCourse}")

class Mark:
    def __init__(self, Mark):
        self.Mark = Mark

    def InputMark(self):
        NameCourse = input("Enter the course you want to enter marks for:")
        if NameCourse not in ListCourse:
            print("Course not found")
        else:
            for IDStudent, student in ListStudent.items():
                mark_value = input(f"Enter mark for {student.NameStudent}: ")
                if IDStudent not in ListMark:
                    ListMark[IDStudent] = {}
                ListMark[IDStudent][NameCourse] = mark_value

    def DisplayMark(self):
        NameCourse = input("Enter the course you want to find: ")
        if NameCourse not in ListCourse:
            print("Course not found")
        else:
            for IDStudent, student in ListStudent.items():
                if IDStudent in ListMark and NameCourse in ListMark[IDStudent]:
                    mark_value = ListMark[IDStudent][NameCourse]
                    print(f"IDStudent: {IDStudent}  Name: {student.NameStudent} Mark: {mark_value}")
                else:
                    print(f"IDStudent: {IDStudent}  Name: {student.NameStudent} Mark: Not entered")

while 0 == 0:
    print("-----------------------------------------------------")
    print("option 1: enter student info")
    print("option 2: enter course info")
    print("option 3: display student list")
    print("option 4: display course list")
    print("option 5: enter mark of student in the course")
    print("option 6: display the mark of student in the course")
    print("option 7: exit")
    print("-----------------------------------------------------")
    opt = input("enter your option") 
    match opt:    
        case "1":
            student = Student(0,0,0)
            student.InputStudent()
        case "2":
            course = Course(0,0)
            course.InputCourse()
        case "3":
            student.Display()
        case "4":
            course.Display()
        case "5":
            mark = Mark(0)
            mark.InputMark()
        case "6":
            mark.DisplayMark()
        case "7":
            exit()    