"""Ex03 Structured Wordle."""

__author__ = "730571715"


def contains_char(word: str, character: str) -> bool:
    """Returns for single string found."""
    assert len(character) == 1
    v: int = 0
    while v < len(word):
        if word[v] == character:
            return True
        v = v + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Compare guess and secret."""
    """Colors and asserts the box the correct color."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji = ""
    v = 0
    while v < len(guess):
        if contains_char(secret, guess[v]):
            if guess[v] == secret[v]:
                emoji = emoji + GREEN_BOX
            else:
                emoji = emoji + YELLOW_BOX
        else: 
            emoji = emoji + WHITE_BOX
        v = v + 1
    return emoji


def input_guess(length: int) -> str:
    """Compare the length of guess and expected length."""
    guess: str = str(input(f"Enter a {length} character word: "))
    guess_length: int = len(guess)
    while guess_length != length:
        guess = str(input(f"That wasn't {length} chars! Try again: "))
        guess_length = len(guess)
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    win: bool = False
    answer: str = "codes"
    while turns <= 6 and win is False:
        print(f"=== Turn {turns}/6 ===") 
        guess_answer: str = input_guess(len("codes"))
        print(emojified(guess_answer, answer))
        if guess_answer == "codes":
            win = True
        else:
            turns += 1
    if win is True:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()