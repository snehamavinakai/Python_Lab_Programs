def create_student_file():
    try:
        with open("student.txt", "w") as file:
            file.write("Roll_no,Name,Class,Section,Department\n")
            for i in range(1, 11):
                roll_no = input(f"Enter roll number of student {i}: ")
                name = input(f"Enter name of student {i}: ")
                class_name = input(f"Enter class of student {i}: ")
                section = input(f"Enter section of student {i}: ")
                department = input(f"Enter department of student {i}: ")
                file.write(f"{roll_no},{name},{class_name},{section},{department}\n")
        print("Student file created successfully.")
    except Exception as e:
        print(f"Error: {e}")

def print_student_details():
    try:
        with open("student.txt", "r") as file:
            print("\t\tKristu JAyanti College Autonomous Department of Computer Science(PG)\t\t\t")
            print("\t\t\t\t***Student Details***\t\t\t")
            print("\t\t\t\t_______________________\t\t\t")
            print("{:<10} {:<20} {:<10} {:<10} {:<10}".format("Roll No", "Name", "Class", "Section", "Department"))
            print("{:<10} {:<20} {:<10} {:<10} {:<10}".format("_______", "____", "_____", "_______", "__________"))
            for line in file.readlines()[1:]:
                roll_no, name, class_name, section, department = line.strip().split(",")
                print("{:<10} {:<20} {:<10} {:<10} {:<10}".format(roll_no, name, class_name, section, department))

    except FileNotFoundError:
        print("Student file not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_student_file()
    print_student_details()
