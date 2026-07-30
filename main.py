
from student import Student
def main():
    while True:
        print("\n============================ Student management System ===============================")
        print("1, Add student")
        print("2, Update marks")
        print("3, Show all students")
        print("4, Exit")

        choice=int(input("Enter your choice from (1-4):"))
        if choice ==1:
            Student.add_student()
        elif choice ==2:
            Student.Update_student()
        elif choice ==3:
            Student.Show_all_Student_details()
        elif choice ==4:
            
            print("Thank you for using Student management System")
            
            break
        else:
            print("invalid choice please try again")
            
if __name__=="__main__":
    main()
