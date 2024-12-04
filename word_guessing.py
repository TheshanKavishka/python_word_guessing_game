import random

words = ["python", "javascript", "typescript", "kotlin", "flutter", "reactjs"]

chosen_word = random.choice(words)

word_display = ['_' for _ in chosen_word]
attempt = 10

print("Welcome to word guessing")

while attempt > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
                    
    else:
        print("Letter is not in the word. You lost one attempt")
        attempt -=1


if '_' not in word_display:
    print("You guessed the word")
    print(' '.join(word_display))
    print("You Survived")
    

else:
    print("You ran out of attempts. The word was", chosen_word)
    print("You Lost!!!")
    