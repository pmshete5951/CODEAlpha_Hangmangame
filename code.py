import random


words = ["melon", "mango", "berry", "olive", "grape", "guava", "apple", "lemon", "peach", "citron"]

while True:
   
    word = random.choice(words)
    word_letters = set(word)  
    guessed_letters = set()   
    incorrect_guesses = 0    
    max_attempts = 6          

    print("Welcome to Hangman!")
    print("HINT 1: - It's a fruit")
    print("HINT 2: - 5 letter word")

    while incorrect_guesses < max_attempts:
       
        word_list = [letter if letter in guessed_letters else '_' for letter in word]
        print(' '.join(word_list))

       
        if set(word_list) == word_letters:
            print("Congratulations! You guessed the word:", word)
            break

        
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
        elif guess in word_letters:
            print("Good guess!")
            guessed_letters.add(guess)
        else:
            print("Oops! That letter is not in the word.")
            incorrect_guesses += 1
            print(f"You have {max_attempts - incorrect_guesses} attempts left.")

    else:
        print("Sorry, you ran out of attempts. The word was:", word)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing Hangman!")
        break
