"""EX03 - Structured_Wordle."""

__author__ = "730571715"

word : str
character : str

def contains_char(word , character) -> bool:
    """Returns for single string found."""
    assert len(character) == 1
    idx : int = 0
    while idx < len(word):
        if word[idx] == character:
            return True
        idx = idx + 1
    return False

guess : str
secret : str
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess, secret) -> str:
    """Compare guess and secret."""
    assert len(guess) == len(secret)
    round : int = 0
    output: str = ""
    while round < len(guess):
        if guess[round] == secret[round]:
            output = f"{GREEN_BOX}{output}" 
        else:
            if contains_char(guess, secret[round]) is True:
                output = f"{YELLOW_BOX}{output}"
            else:
                output = f"{WHITE_BOX}{output}"
        round = round + 1
    return output


length : int

def input_guess(length) -> str:
    """Compare the length of guess and expected length."""
    guess : str = str (input(f"Enter a {length} character word: "))
    guess_length : int = len(guess)
    while guess_length != length:
        guess = str(input(f"That wasn't {length} chars! Try again: "))
        guess_length = len(guess)
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    win: bool = False
    while turns <= 6 and win is False:
        print(f"=== Turn {turns}/6 ===") 
        guess: str = input_guess(len("codes"))
        emoji: str = emojified(guess, "codes")
        print(emoji)
        if guess == "codes":
            win = True
        else:
            turns += 1
    if win is True:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()