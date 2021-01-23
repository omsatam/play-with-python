import random

with open("words.txt", "r") as f:
    words = f.readlines()
word = random.choice(words)[:-1]

mistakes = 8
guesses = []
done = False 

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end = " ")
        else:
            print("_", end =" ")
    print()

    guess = input(f"The number of attemts left are {mistakes}\nplease guess a character: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        mistakes -= 1
        if mistakes == 0:
            break
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"Congratulations you found the word. \nThe word was {word} ")
else:
    print(f"Game over. The word was {word}")