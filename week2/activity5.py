class SentenceCount:
    def __init__(self, text):
        self.text = text

    def count(self):
        return len(self.text.split(" "))


def main():
    sentence = input("Sentence: ")
    name = SentenceCount(sentence)
    print("Word count:", name.count())


if __name__ == "__main__":
    main()
