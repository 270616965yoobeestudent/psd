from database import create_tables, seed_data
from menus.menu_main import menu_main


def main():
    create_tables()
    seed_data()
    menu_main()


if __name__ == "__main__":
    main()
