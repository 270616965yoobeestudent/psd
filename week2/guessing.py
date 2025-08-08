import random


def _guessing_game():
    choices = [
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
    ]

    global life
    life = 5
    answer = random.choice(choices)
    blankWord = "_" * len(answer)

    while life > 0:
        print(f"your life: {life}")
        print(f"Guess this: {blankWord}")
        letter = input("Enter letter: ")
        blankWord = _guessWord(answer, blankWord, letter)
        if answer == blankWord:
            print("You win")
            break
        if life == 0:
            print("Game Over")
            break


def _guessWord(answer, blankWord, letter):
    correct = False
    blankList = list(blankWord)
    for i, aLetter in enumerate(answer):
        if (letter) == aLetter:
            blankList[i] = letter
            correct = True
    if correct == False:
        global life
        life -= 1
    return ''.join(blankList)


if __name__ == "__main__":
    _guessing_game()
