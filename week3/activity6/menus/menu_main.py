from .menu_student import menu_student
from .menu_course import menu_course
from .menu_lecturer import menu_lecturer
from .menu_subject import menu_subject


def menu_main():
    while True:
        print("\n==========================")
        print("Welcome to Yoobee Colleges!")
        print("==========================\n")
        
        print("0. Exit")
        print("1. Student management")
        print("2. Course management")
        print("3. Lecturer management")
        print("4. Subject management")

        choice = input("Select an option (0-4): ")
        if choice == "0":
            break
        elif choice == "1":
            choice = menu_student()
        elif choice == "2":
            choice = menu_course()
        elif choice == "3":
            choice = menu_lecturer()
        elif choice == "4":
            choice = menu_subject()
        else:
            print("\nInvalid choice. Please try again.")

    print("\n======================")
    print("       Goodbye!")
    print("======================")
