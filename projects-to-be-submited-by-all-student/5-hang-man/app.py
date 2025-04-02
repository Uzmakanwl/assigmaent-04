import random
print("Welcome to hangman game")
print("guess form this:","pythonhangmancodemuzamilimplekin")
words = ["python","hangman","code","game" ,"muzamil"]
word = random.choice(words)

guess = input(f"Guess the word({len(word)} letters): ") .lower()

if guess == word:
      print("congratulation! you guessed it right !")
else:
      print(f"Game over! The correct word was :{words}")