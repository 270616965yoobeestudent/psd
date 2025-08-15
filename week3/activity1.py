class DemoFile:
    def __init__(self, filename):
        self.filename = filename

    def write_file(self, text):
        with open(self.filename, 'w') as file:
            file.write(text)

    def read_file(self):
        with open(self.filename, 'r') as file:
            return file.read()

def main():
    demoFile = DemoFile('week3/demo_file_activity1.txt')
    print(demoFile.read_file())
    demoFile.write_file('Hello World')
    print(demoFile.read_file())


if __name__ == "__main__":
    main()