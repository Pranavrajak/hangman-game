import random


words = ["apple", "banana", "mango", "grapes", "orange"]


word = random.choice(words)

guessed_letters = []
attempts = 6


def display_word():
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

print("🎮 Welcome to Hangman Game!")

while attempts > 0:
    print("\nWord:", display_word())
    print("Guessed letters:", " ".join(guessed_letters))
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

   
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Enter a single valid letter!")
        continue

    if guess in guessed_letters:
        print("⚠️ Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
    else:
        print("❌ Wrong guess!")
        attempts -= 1

  
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 You WON! The word was:", word)
        break


else:
    print("\n💀 You LOST! The word was:", word)