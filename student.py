class Student:
    total_student=[]
    def __init__(self,name,marks,rollno):
        self.name=name
        self.marks=marks
        self.rollno=rollno
    def update_marks(self,new_marks):
        self.marks=new_marks
        print(f"Marks updated successfully for {self.name} to {self.marks}")
    @classmethod
    def find_student_details(cls,rollno):
        for student in cls.total_student:
            if student.rollno==rollno:
                return student
        return None
    @classmethod
    def add_student(cls):
        name=input("Enter your name: ")
        marks=int(input("Enter your marks:"))
        roll=input("Enter your roll no:")

        Student=cls(name,marks,roll)
        cls.total_student.append(Student)
        print(f"Student added {name} Successfully!")

    @classmethod
    def Update_student(cls):
        roll=input("Enter your roll_no:")
        Student=cls.find_student_details(roll)
        if Student:
            new_marks=int(input("Enter your marks:"))
            Student.update_marks(new_marks)
        else:
            print("Student not find!")
    @classmethod
    def Show_all_Student_details(cls):
        for student in cls.total_student:
            print(f"Name:{student.name}, Marks:{student.marks}, Roll_no:{student.rollno}")
