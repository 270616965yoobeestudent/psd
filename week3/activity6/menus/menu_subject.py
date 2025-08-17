from managers.subject_manager import SubjectManager
from managers.course_manager import CourseManager

_manager = SubjectManager()
_course_manager = CourseManager()

def menu_subject():
    while True:
        print("\n======================")
        print(" Subject Management!")
        print("======================\n")

        print("0. back to main menu")
        print("1. view all subjects")
        print("2. add a subject")
        print("3. delete a subject")
        print("4. update a subject")

        choice = input("Select an option (0-4): ")
        if choice == "0":
            break
        elif choice == "1":
            items = _manager.list()
            _print_subject_list(items)
        elif choice == "2":
            name = input("Enter subject name: ")
            courses = _course_manager.list()
            _print_course_list(courses)
            course_id = input("Enter course id of subject: ")
            try:
                _manager.add(name, course_id)
                print("\nAdd new subject successfully!")
            except Exception as e:
                print("\nOps! Something went wrong!")
        elif choice == "3":
            items = _manager.list()
            _print_subject_list(items)
            id = input("Enter subject id to delete: ")
            try:
                _manager.delete(id)
                print("\nDelete subject successfully!")
            except Exception as e:
                print("\nOps! Something went wrong!")
        elif choice == "4":
            items = _manager.list()
            _print_subject_list(items)
            id = input("Enter subject id to edit: ")
            name = input("Enter new subject name: ")
            try:
                _manager.update(id, name)
                print("\nUpdate subject successfully!")
            except Exception as e:
                print("\nOps! Something went wrong!")
        else:
            print("\nInvalid choice. Please try again.")


def _print_subject_list(items):
    print("\n======================")
    for item in items:
        print(f"ID: {item[0]}, Name: {item[1]}, Course: {item[4]}")
    print("======================")

def _print_course_list(items):
    print("\n=======Courses=========")
    for item in items:
        print(f"ID: {item[0]}, Name: {item[1]}")
    print("=======Courses=========")

