"""EX01 - Chardle - A cute step towards Wordle"""
__author__ = "730570153"


a: int = 0
word: str = (input("Enter a 5-character word: "))
if len(word) != 5:
    print("Error: Word must contain 5 characters")
else:
    guess: chr = input("Enter a single character: ")
    if len(guess) != 1:
        print("Error: Character must be a single character.")
    else:

        print("Searching for " + guess + " in " + word)
        if word[0] == guess:
            a = (a + 1)
            print( guess + " found at index 0")
        if word[1] == guess:
            a = (a + 1)
            print( guess + " found at index 1")
        if word[2] == guess:
            a = (a + 1)
            print( guess + " found at index 2")
        if word[3] == guess:
            a = (a + 1)
            print( guess + " found at index 3")
        if word[4] == guess:
            a = (a + 1)
            print( guess + " found at index 4")
        if a == 0:
            print("No instances of " + guess + " found in " + word)
        if a == 1:
            print("1 instance of " + guess + " found in " + word)
        if a == 2:
            print("2 instances of " + guess + " found in " + word)
        if a == 3:
            print("3 instances of " + guess + " found in " + word)
        if a == 4:
            print("4 instances of " + guess + " found in " + word)
        if a == 5:
            print("5 instances of " + guess + " found in " + word)