"""EX01 - Chardle - A cute step toward wordle."""

__author__ = "730571715"

word: str = input("Please enter a 5-character word: ")

if len(word) != 5:
    print ("Error: Word must contain 5 characters.")
    exit()

character: str = input("Enter a single character: ")

if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()

print(f"searching for {character} in {word}")
repetitions: int = 0
for index in range(len(word)):
    if word[index] == character:
        print(f"{character} found at index {index}")
        repetitions = repetitions + 1
if repetitions == 1:
    print(f"1 instance of {character} found in {word}")  
else:
    if repetitions == 0:
        print(f"No instances of {character} found in {word}")
    else:
        print(f"{repetitions} instances of {character} found in {word}")
    
    





