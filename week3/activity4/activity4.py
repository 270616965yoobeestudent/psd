from database import create_tables, seed_data


def main():
    create_tables()
    seed_data()


if __name__ == "__main__":
    main()
