from managers.course_manager import CourseManager

_manager = CourseManager()

def menu_course():
    while True:
        print("\n======================")
        print("  Course Management!")
        print("======================\n")

        print("0. back to main menu")
        print("1. view all courses")
        print("2. add a course")
        print("3. delete a course")
        print("4. update a course")

        choice = input("Select an option (0-4): ")
        if choice == "0":
            break
        elif choice == "1":
            items = _manager.list()
            _print_course_list(items)
        elif choice == "2":
            name = input("Enter course name: ")
            try:
                _manager.add(name)
                print("\nAdd new course successfully!")
            except Exception as e:
                print(e)
                print("\nOps! Something went wrong!")
        elif choice == "3":
            items = _manager.list()
            _print_course_list(items)
            id = input("Enter course id to delete: ")
            try:
                _manager.delete(id)
                print("\nDelete course successfully!")
            except Exception as e:
                print("\nOps! Something went wrong!")
        elif choice == "4":
            items = _manager.list()
            _print_course_list(items)
            id = input("Enter course id to edit: ")
            name = input("Enter new course name: ")
            try:
                _manager.update(id, name)
                print("\nUpdate course successfully!")
            except Exception as e:
                print("\nOps! Something went wrong!")
        else:
            print("\nInvalid choice. Please try again.")

def _print_course_list(items):
    print("\n======================")
    for item in items:
        print(f"ID: {item[0]}, Name: {item[1]}")
    print("======================")
