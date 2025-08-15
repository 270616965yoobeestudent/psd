class DemoFile:
    def __init__(self, filename):
        self.filename = filename

    def count_words(self):
        with open(self.filename, "r") as file:
            count = 0
            for line in file:
                words = line.strip().split()
                count += len(words)
            return count


def main():
    demoFile = DemoFile("week3/demo_file_activity2.txt")
    print(f"total number of words in file: {demoFile.count_words()} words")


if __name__ == "__main__":
    main()
