from managers.lecturer_manager import LecturerManager
from managers.lecturer_subject_manager import LecturerSubjectManager
from managers.subject_manager import SubjectManager


_manager = LecturerManager()
_lecturer_subject_manager = LecturerSubjectManager()
_subject_manager = SubjectManager()


def menu_lecturer():
    while True:
        print("\n======================")
        print(" Lecturer Management!")
        print("======================\n")

        print("0. back to main menu")
        print("1. view all lecturers")
        print("2. add a lecturer")
        print("3. delete a lecturer")
        print("4. update a lecturer")
        print("5. view a teacher details")
        print("6. add a subject")
        print("7. remove a subject")

        choice = input("Select an option (0-4): ")
        if choice == "0":
            break
        elif choice == "1":
            items = _manager.list()
            _print_lecturer_list(items)
        elif choice == "2":
            name = input("Enter lecturer name: ")
            try:
                _manager.add(name)
                print("\nAdd new lecturer successfully!")
            except Exception as e:
                print(e)
                print("\nOps! Something went wrong!")
        elif choice == "3":
            items = _manager.list()
            _print_lecturer_list(items)
            id = input("Enter lecturer id to delete: ")
            try:
                _manager.delete(id)
                print("\nDelete lecturer successfully!")
            except Exception as e:
                print("\nOps! Something went wrong!")
        elif choice == "4":
            items = _manager.list()
            _print_lecturer_list(items)
            id = input("Enter lecturer id to edit: ")
            name = input("Enter new lecturer name: ")
            try:
                _manager.update(id, name)
                print("\nUpdate lecturer successfully!")
            except Exception as e:
                print("\nOps! Something went wrong!")
        elif choice == "5":
            items = _manager.list()
            _print_lecturer_list(items)
            id = input("Enter lecturer id to view: ")
            lecturer = _manager.get(id)
            subjects = _lecturer_subject_manager.list_of_lecturer(id)
            _print_lecturer_detail(lecturer, subjects)
        elif choice == "6":
            items = _manager.list()
            _print_lecturer_list(items)
            id = input("Enter lecturer id to add subject: ")
            subjects = _subject_manager.list()
            _print_subject_list(subjects)
            subject_id = input("Enter subject id to add: ")
            try:
                _lecturer_subject_manager.add(id, subject_id)
                print("\nAdd a subject successfully!")
            except Exception as e:
                print("\nOps! Something went wrong!")
        elif choice == "7":
            items = _manager.list()
            _print_lecturer_list(items)
            id = input("Enter lecturer id to remove subject: ")
            subjects = _lecturer_subject_manager.list_of_lecturer(id)
            _print_lecturer_subject_list(subjects)
            subject_id = input("Enter subject id to remove: ")
            try:
                _lecturer_subject_manager.delete(id, subject_id)
                print("\nRemove a subject successfully!")
            except Exception as e:
                print("\nOps! Something went wrong!")

        else:
            print("\nInvalid choice. Please try again.")


def _print_lecturer_list(items):
    print("\n======================")
    for item in items:
        print(f"ID: {item[0]}, Name: {item[1]}")
    print("======================")


def _print_subject_list(items):
    print("\n======================")
    for item in items:
        print(f"ID: {item[0]}, Name: {item[1]}, Course: {item[4]}")
    print("======================")


def _print_lecturer_subject_list(items):
    print("\n======================")
    for item in items:
        print(f"ID: {item[4]}, Name: {item[5]}, Course: {item[8]}")
    print("======================")

def _print_lecturer_detail(lecturer, items):
    print("\n=======lecturer========")
    print(f"Name: {lecturer[1]}")
    print("=======Subjects=========")
    for item in items:
        print(f"{item[5]}")
    print("=======================")
