import random,os,math,interface

#imports the dictionary
dictionary = open('dictionary.txt').read().splitlines()


def pick_word(): #only picks words with 3-15 letters
	while True:
		word=random.choice(dictionary)
		if 3<=len(word)<=15:
			break
	print(word)#remove later
	return word

def generate_letters(word): #gets the letters of the random word
	list_letters = [letter for letter in word]
	#for i in range(len(word)*2):
		#list_letters.append(chr(random.randint(97,123)))
	return list_letters




def gameloop_engine(word):

	guesses=[] #holds all the guesses of the player
	guessed=False
	
	score=0
	tries=10

	while not guessed and tries>0:
		
		text='Please enter one letter or a ' +str(len(word))+ '-letter word.'
		guess=input(text).lower()

		if guess in guesses:
			print('You already guessed '+ guess)

		elif len(guess)==len(word):
			guesses.append(guess)

			if guess==word:
				guessed=True
				score+=10
			else:
				print('Sorry. That is incorrect.')

		elif len(guess)==1:
			guesses.append(guess)
			result=check(word,guesses,guess,score,tries)
			if result==word:
				guessed=True
				score+=10
			else:
				print(result)
				
		else:
			print('Invalid Entry!')
			tries-=1
		print (tries)
		if guessed==True:
			print('Yes, the word is ' +word +'! Your score is ' + str(score))
		elif guessed==False and tries<0:
			print('Game Over. Your score is ' + str(score))
			break



def check(word,guesses,guess,score,tries):
	score=0
	status=''
	matches=0
	for letter in word:
		if letter in guesses:
			status+=letter
			
		else:
			status+='*'

		if letter==guess:
			matches+=1

		else:
			tries-=1
			return tries

	if matches>1:
		print ('Yes! The word contains '+str(matches)+guess +'s')
		score+=1
	elif matches==1:
		print('Yes! The word contains '+str(matches)+guess)
		score+=1
	else:
		print('Sorry. The word does not contain the letter ' +guess)
	return status
	



#def letterchecker(word,guess):
	#for letter in word:
		#if guess==letter:
			#interface.letter_appending()
