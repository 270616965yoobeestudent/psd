from managers.student_manager import StudentManager
from managers.student_course_manager import StudentCourseManager
from managers.student_subject_manager import StudentSubjectManager
from managers.subject_manager import SubjectManager
from managers.course_manager import CourseManager

_manager = StudentManager()
_student_course_manager = StudentCourseManager()
_student_subject_manager = StudentSubjectManager()
_subject_manager = SubjectManager()
_course_manager = CourseManager()


def menu_student():
    while True:
        print("\n======================")
        print(" Student Management!")
        print("======================\n")

        print("0. back to main menu")
        print("1. view all students")
        print("2. add a student")
        print("3. delete a student")
        print("4. update a student")
        print("5. view student details")
        print("6. enroll a course")
        print("7. withdraw a course")
        print("8. withdraw a subject")

        choice = input("Select an option (0-4): ")
        if choice == "0":
            break
        elif choice == "1":
            items = _manager.list()
            _print_student_list(items)
        elif choice == "2":
            name = input("Enter student name: ")
            try:
                _manager.add(name)
                print("\nAdd new student successfully!")
            except Exception as e:
                print("\nOps! Something went wrong!")
        elif choice == "3":
            items = _manager.list()
            _print_student_list(items)
            id = input("Enter student id to delete: ")
            try:
                _manager.delete(id)
                print("\nDelete student successfully!")
            except Exception as e:
                print("\nOps! Something went wrong!")
        elif choice == "4":
            items = _manager.list()
            _print_student_list(items)
            id = input("Enter student id to edit: ")
            name = input("Enter new student name: ")
            try:
                _manager.update(id, name)
                print("\nUpdate student successfully!")
            except Exception as e:
                print("\nOps! Something went wrong!")
        elif choice == "5":
            items = _manager.list()
            _print_student_list(items)
            id = input("Enter student id to view: ")
            student = _manager.get(id)
            courses = _student_course_manager.list_of_student(id)
            _print_student_detail(student, courses)
        elif choice == "6":
            items = _manager.list()
            _print_student_list(items)
            id = input("Enter student id to enroll: ")
            courses = _course_manager.list()
            _print_course_list(courses)
            course_id = input("Enter course id to enroll: ")
            try:
                _student_course_manager.add(id, course_id)
                subjects = _subject_manager.list_of_course(course_id)
                for subject in subjects:
                    _student_subject_manager.add(id, subject[0])
                print("\nEnroll a course successfully!")
            except Exception as e:
                print("\nOps! Something went wrong!")
        elif choice == "7":
            items = _manager.list()
            _print_student_list(items)
            id = input("Enter student id to withdraw: ")
            courses = _student_course_manager.list_of_student(id)
            _print_student_course_list(courses)
            course_id = input("Enter course id to withdraw: ")
            try:
                _student_course_manager.delete(id, course_id)
                subjects = _student_subject_manager.list_of_course(id, course_id)
                for subject in subjects:
                    _student_subject_manager.delete(id, subject[1])
                print("\nWithdraw a course successfully!")
            except Exception as e:
                print("\nOps! Something went wrong!")
        elif choice == "8":
            items = _manager.list()
            _print_student_list(items)
            id = input("Enter student id to remove subject: ")
            subjects = _student_subject_manager.list_of_student(id)
            _print_student_subject_list(subjects)
            subject_id = input("Enter subject id to remove: ")
            try:
                _student_subject_manager.delete(id, subject_id)
                print("\nWithdraw a subject successfully!")
            except Exception as e:
                print("\nOps! Something went wrong!")
        else:
            print("\nInvalid choice. Please try again.")


def _print_student_list(items):
    print("\n======================")
    for item in items:
        print(f"ID: {item[0]}, Name: {item[1]}")
    print("======================")


def _print_course_list(items):
    print("\n=======Courses=========")
    for item in items:
        print(f"ID: {item[0]}, Name: {item[1]}")
    print("=======Courses=========")


def _print_student_subject_list(items):
    print("\n======================")
    for item in items:
        print(f"ID: {item[4]}, Name: {item[5]}, Course: {item[8]}")
    print("======================")


def _print_student_course_list(items):
    print("\n=======Courses=========")
    for item in items:
        print(f"ID: {item[4]}, Name: {item[5]}")
    print("=======Courses=========")


def _print_student_detail(student, items):
    print("\n=======Student========")
    print(f"Name: {student[1]}")
    print("=======Courses=========")
    for item in items:
        print(f"{item[5]}")
        subjects = _student_subject_manager.list_of_course(item[0], item[4])
        for subject in subjects:
            print(f"|--{subject[5]}")
    print("=======================")
