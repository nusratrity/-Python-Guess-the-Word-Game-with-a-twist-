import random

def guess_the_word():
    words = ["python", "banana", "elephant", "guitar", "rainbow", "diamond", "pancake"]
    secret_word = random.choice(words)
    guessed_letters = []
    tries = 6

    print("🎮 Welcome to the Funny Guess-the-Word Game! 🎮")
    print("Try to guess the secret word, one letter at a time.")
    print(f"You only have {tries} chances!")

    while tries > 0:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word.strip())

        if "_" not in display_word:
            print(f"🎉 Congratulations! You guessed it right! The word was: {secret_word}")
            break

        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("😒 Hey! You already tried that letter.")
            continue

        if guess in secret_word:
            print("✅ Good job! That letter is in the word.")
        else:
            print("❌ Oops! Wrong guess.")
            print(random.choice([
                "😂 My grandma could guess better!",
                "😜 Are you even trying?",
                "🙄 Maybe try closing your eyes next time.",
                "😆 That was... creative. But wrong.",
                "🤓 Let's pretend that guess didn't happen."
            ]))
            tries -= 1

        guessed_letters.append(guess)

    if tries == 0:
        print(f"\n💀 Game Over! The word was: {secret_word}")
        print("Better luck next time! 😅")

guess_the_word()
