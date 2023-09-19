"""EX02 - one_shot_wordle."""

__author__ = "730571715"

answer: str = "python"
answerlen: int = len(answer)
word: str = input(f"What's your {answerlen}-letter guess? ")

word_idx: int = 0
answer_idx: int = 0
yellow_count: int = 0
yellow_idx: int = 0


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(word) != answerlen:
    word = input(f"That was not {answerlen} letters! Try again: ")


while word_idx<answerlen:
    yellow_count = 0
    yellow_idx = 0
    answer_character: str = str (answer[answer_idx])
    word_character: str = str(word[word_idx])
    if answer_character == word_character:
        print(GREEN_BOX, end="")
    else:
        while yellow_idx < answerlen:
            if word_character == answer[yellow_idx]:
                yellow_count += 1
            yellow_idx += 1
        if yellow_count > 0:
            print(YELLOW_BOX, end="")
        else:
            print(WHITE_BOX, end="")
    answer_idx = answer_idx + 1
    word_idx = word_idx + 1

print("")

if len(word)==6:
    if word == answer:
        print("Woo! You got it! ")
    else:
        print("Not quite! Play again soon!")





