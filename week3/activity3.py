import pandas as pd

class DemoFile:
    def __init__(self, filename):
        self.filename = filename
    
    def caculate(self):
        reader = pd.read_csv(self.filename, sep=';')
        print(f"maximum: {reader['alcohol'].max():.2f}")
        print(f"minimum: {reader['alcohol'].min():.2f}")
        print(f"average: {reader['alcohol'].mean():.2f}")
        print("==================")
        print(reader['alcohol'].abs())
            


def main():
    demoFile = DemoFile("week3/winequality-red.csv")
    demoFile.caculate()


if __name__ == "__main__":
    main()
