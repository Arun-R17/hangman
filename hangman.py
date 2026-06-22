import random
import string

name = input("what is your name? ")

print("Good luck", name)

# Dictionary containing words and their clues
words_with_clues = {
    "computer": "An electronic device for storing and processing data.",
    "laptop": "A portable computer suitable for use while traveling.",
    "windows": "A popular operating system developed by Microsoft.",
    "desktop": "A personal computer designed for regular use at a single location.",
    "keyboard": "An input device with keys to type text.",
    "mouse": "A hand-held pointing device that controls a cursor.",
    "monitor": "An output device that displays visual information.",
    "printer": "A machine that prints digital text or images on paper.",
    "scanner": "A device that scans documents and converts them into digital data.",
    "speaker": "An output device that produces sound."
}

word = random.choice(list(words_with_clues.keys()))
clue = words_with_clues[word]

print("\n--- Game Started! ---")
print("Guess the characters: ")
 
guesses = ""
turns = 6  # Increased turns to make the game fun and fair

while turns > 0:
    failed = 0
    display = ""
    for char in word:
        if char in guesses:
            display += char + " "
        else:
            display += "_ "
            failed += 1
            
    print("\nWord: ", display.strip())
    
    # Displaying remaining guesses and letters
    print(f"Guesses remaining: {turns}")
    
    guessed_list = sorted(list(guesses)) if guesses else []
    print(f"Guessed letters: {', '.join(guessed_list) if guessed_list else 'None'}")

    if failed == 0:
        print("\n★ Congratulations! You win! ★")
        print("The word is:", word)
        break
    
    guess = input("\nGuess a character (or type 'clue' to reveal the hint): ").lower().strip()
    
    if guess == 'clue' or guess == 'hint':
        print(f"\n💡 Hint: {clue}")
        continue
    
    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
    
    if guess in guesses:
        print("You already guessed that letter!")
        continue

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong guess!")
        if turns > 0:
            print(f"You have {turns} more guesses.")

if turns == 0:
    print(f"\nGame Over! Sorry {name}, you lost.")
    print("The secret word was:", word)