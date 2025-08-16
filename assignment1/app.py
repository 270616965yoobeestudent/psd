from data.database import init_database


class App:
    def __init__(self):
        init_database()

    def run(self):
        while True:
            cmd = input(">>> ")
            if cmd == "login":
                break
            if cmd == "exit":
                break
            if cmd == "help":
                break
            else:
                break


if __name__ == "__main__":
    app = App()
    app.run()
