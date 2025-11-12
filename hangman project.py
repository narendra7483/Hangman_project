import random

# Step 1: Predefined list of 5 words
words = ["python", "hangman", "orange", "school", "keyboard"]

# Step 2: Randomly choose one word
secret_word = random.choice(words)

# Step 3: Game variables
attempts = 6
guessed_letters = []
display = ["_"] * len(secret_word)

print("🎯 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("Word:", " ".join(display))

# Step 4: Game Loop
while attempts > 0:
    guess = input("\nEnter a letter: ").lower()

    # Check valid input
    if len(guess) != 1 or not guess.isalpha():
        print("❗ Enter only a single alphabet letter!")
        continue

    # Check if letter already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Step 5: Check guess
    if guess in secret_word:
        print("✅ Correct!")

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess
    else:
        attempts -= 1
        print("❌ Wrong! Attempts left:", attempts)

    print("Word:", " ".join(display))

    # Step 6: Check win
    if "_" not in display:
        print("\n🎉 You win! The word was:", secret_word)
        break

# Step 7: If player loses
if "_" in display:
    print("\n💀 Game Over! The correct word was:", secret_word)
