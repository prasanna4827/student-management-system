class Student_Management_System:
    def __init__(self):
        self.students = []

    def add_student(self):
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        marks = input("Enter Marks: ")

        student = {"roll": roll, "name": name, "age": age, "marks": marks}
        self.students.append(student)
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No records found??")
        else:
            print("--- Student List ---")
            for s in self.students:
                print(f"Roll: {s['roll']}, Name: {s['name']} , Age: {s['age']} , Marks: {s['marks']}")

    def search_student(self):
        roll = input("Enter Roll Number to search: ")
        for s in self.students:
            if s['roll'] == roll:
                print(f"Found: {s}")
                return
        print("Student not found.")

    def update_student(self):
        roll = input("Enter Roll Number to update: ")
        for s in self.students:
            if s['roll'] == roll:
                s['name'] = input("Enter new Name: ")
                s['age'] = input("Enter new Age: ")
                s['marks'] = input("Enter new Marks: ")
                print("Student updated successfully!")
                return
        print("Student not found.")

    def delete_student(self):
        roll = input("Enter Roll Number to delete: ")
        for s in self.students:
            if s['roll'] == roll:
                self.students.remove(s)
                print("Student deleted successfully!")
                return
        print("Student not found.")

def sms_main():
    sms = Student_Management_System()

    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter sms choice number: ")

        if choice == '1':
            sms.add_student()
        elif choice == '2':
            sms.view_students()
        elif choice == '3':
            sms.search_student()
        elif choice == '4':
            sms.update_student()
        elif choice == '5':
            sms.delete_student()
        elif choice == '6':
            print(" Exiting program")
            break
        else:
            print("Invalid choice, please try again!")



if __name__ == "__main__":
   sms_main()


