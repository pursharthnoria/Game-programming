import nltk
import random
from nltk.corpus import words

#nltk.download('words')
word_list = words.words()
word = random.choice(word_list)
word=word.lower()


print('*****************************************************************************************************************************************************************')
difficulty = int(input("Select a difficulty mode\n\nPress 1 for easy.\nPress 2 for intermediate\npress 3 for expert\nEnter your choice: "))
if difficulty==1:
    maxchances = 15
elif difficulty==2:
    maxchances = 10
elif difficulty==3:
    maxchances = 5

alphabets = 'abcdefghijklmnopqrstuvwxyz'
l = len(word)
print('*****************************************************************************************************************************************************************')
print('Hey! This is an english word with {} alphabets. Try to Guess it Within {} chances.'.format(l,maxchances))
chances = 1
status='Trying'
guessed=[]

for i in range(l):
    guessed.append('_')

wrong_guesses=[]


while (True):
    print('_______________________________________________________')
    
    if chances>maxchances:
        print()
        print('\n**********************************************************\nHey! You have used up your chances. Better luck next time.\n**********************************************************')
        print('The correct answer was '+word+'.\n')
        break
    
    if '_' not in guessed:
        status='won'
        print('\n'+' '.join(guessed))
        print('\n**********************\nHey! You won the game\n**********************')
        break
    
    print('_______________________________________________________')
    print('Chances: {}/{}'.format(chances,str(maxchances)))
    print(' '.join(guessed))
    guess = input("Enter a guess: ")
    
    if guess in wrong_guesses or guess in guessed:
        print('Hey! You have guessed that already. Try a different letter.\n')
        continue

    if guess not in alphabets:
        print('Hey enter a letter, not a number or a special character.\n')
        continue
    
    if guess in word:
        print('Hey! That was a correct guess.\n')
        for index,letter in enumerate(word):
            if letter==guess:
                guessed[index]=letter
    
    if guess not in word:
        chances = chances+1
        print('Not the right one man!\n')
        wrong_guesses.append(guess)
    
    
    print('Wrong guesses yet: '+' '.join(wrong_guesses))