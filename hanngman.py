#to start this new project we have to first create a new python project where 
#we can create a list with the words we are gonna use in our hangman game.


#1. import radom.
#2. import the list we created in the other project.
import random
from wordPythonHangman import words
import string

#3. Define a function so the pc can choose a valid word from the list that \
#we can guess while playing the game.
#4.Create a variable with the random.choice option.
#5. Create a while loop that determines when the pc select a word from the list\
#this word cannot have a '-' dash or a ' ' space in it.
def getValidWord(words):
    word = random.choice(words) #what this does is randomly choose a word from the list of words.
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

#To create a way to determine which letter we've guessed and which letters we correctly guess, and\
# a way to tell what are wrong letters:
#6. Create a function.
#7. Define variable that can represent every letter of the word the cpu has chosen.
#8. Import a pyhton predetermine list of uppercase characters. we do this writing 'import' "strings" at the top...
#9. Create a variable, inside of set write "ascii_uppercase" is a pre-initialized string used as string constant.\
# ascii_uppercase will give the uppercase letters ‘ABCDEFGHIJKLMNOPQRSTUVWXYZ’."
#10. Another variable to archive the letters the user has guessed.
#11. Getting user input.
#13. Determine the rules of the game using if statements.
#14. Create a "while loop" to determine when the user has guessed all the letters of the word.
#15. Inside the while loop create a output so the user can track and see the letters they'd used.

def hangman():
    word = getValidWord(words)
    wordLetters = set(word) #we are gonna use set as a way to determine what are the letter of the word the pc has chosen.
    alphabet = set(string.ascii_uppercase) #
    usedLetters = set() #This one is gonna be used to keep track of the letter the user has guessed.
    #game rules:
    lives = 10
    while len(wordLetters) > 0 and lives > 0: #this condition is gonna execute till the user has guessed all the letters or they has used or their lives.
        #15. letter used:
        #What join does is 
        print("You have", lives, "lives left and you've used this letters: ", " ".join(usedLetters))
        #16. How to show the user what the current word is but using dashes in the space\
        #where the user have not guessed the letter that correspond to that space?:
        #Create a list.
        wordList = [letter if letter in usedLetters else "-" for letter in word]
        print("Current word: ", " ".join(wordList))

        userGuessLetter = input("Guess a letter: ").upper()
        if userGuessLetter in alphabet - usedLetters: #if our guess is in the alphabet then...
           usedLetters.add(userGuessLetter) #We are gonna add that letter to the set we made 'usedLetters'
           if userGuessLetter in wordLetters: #in addition to that if our guess is in wordLetters.
               wordLetters.remove(userGuessLetter) #We are gonna remove that letter from that list.
           else:
                lives = lives - 1 #17. This variable is gonna take a life if the letter is not in the word.
                print(userGuessLetter, "is not in the word")

        elif userGuessLetter in usedLetters:
            print("You've already used this letter. Try again")
        else: #in this case this message it's gonna appera if we use a character that it is not in the alphabet.
            print("Invalid character! Try again.")

   #18. Gets here when this condition is gonna execute till the user has guessed all the letters or they has used or their lives.
    if lives == 0:
        print("Sorry, You died. Run the game one more time and good luck. the word was", word )
    else:
        print("You guessed the ", word,"!! CONGRATULATIONS!" )


hangman()



