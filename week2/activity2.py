import random


class GuessingGame:
    life = 5
    choices = []
    answerWords = []
    blankWords = []

    def __init__(self, life, choices):
        self.choices = choices
        self.life = life
        self.answerWords = list(random.choice(self.choices))
        self.blankWords = list("_" * len(self.answerWords))

    def play(self):
        print("Game start")
        self._gameLoop()

    def _prompt(self):
        print(f"your life: {self.life}")
        print(f"Guess this: {' '.join(self.blankWords)}")

    def _guessWord(self, letter):
        if (letter) in self.answerWords:
            self.blankWords = [
                a if letter == a else self.blankWords[i]
                for i, a in enumerate(self.answerWords)
            ]
            return
        else:
            self.life -= 1
            return

    def _validate(self):
        if self.life == 0:
            # print(f"Answer is {''.join(self.answerWords)}")
            print("Game Over")
            return True
        elif self.answerWords == self.blankWords:
            # print(f"Answer is {''.join(self.answerWords)}")
            print("You win")
            return True
        else:
            return False

    def _gameLoop(self):
        while self.life > 0:
            self._prompt()
            letter = input("Enter letter: ")
            self._guessWord(letter)
            if self._validate():
                break


if __name__ == "__main__":
    game = GuessingGame(
        5,
        [
            "apple",
            "banana",
            "cherry",
            "date",
            "elderberry",
            "fig",
            "grape",
            "honeydew",
            "kiwi",
            "lemon",
        ],
    ).play()
