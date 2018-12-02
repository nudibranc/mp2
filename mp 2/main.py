import os, math, random, engine,pyglet,time,interface
from random import randint
from pyglet.window import key
from pyglet.window import mouse
from pyglet import font
from game_objects import Player
from game_objects import Display_input
from game_objects import Game

dictionary = open('dictionary.txt').read().splitlines() #

width,height = interface.width,interface.height

#Window popup display
window=pyglet.window.Window(width=width,height=height,caption='Hangman',resizable=False)  #creates window


condition=False #
name = Display_input('',width//2,(3*height)//4,40)
player = Player()
game = Game(engine.pick_word(), 10)


current_word=list(game.word) #holds list of all letters in the current word
print(current_word)#remove later

word=game.word #
word=Display_input('',width//2,(3*height)//4,50)#
correctguesses=[" "]#

guess=Display_input('',width//2,(3*height)//4,40)

score=player.score #verification and datafile purposes
finalscore=Display_input('',width//2,(3*height)//4,40)#for the display part

#mouse events
@window.event
def on_mouse_press(x,y,button,modifier):
	if button==mouse.LEFT:
		if player.state=='start_screen':
			player.state='name_input_screen' #gets player's name screen
		
#keyboard events
@window.event
def on_key_press(symbol, modifiers):
	score=0
	if player.state =='name_input_screen':
		if 97<=symbol<=122 and len(name.text)<=15:
			name.text+=chr(symbol)

		elif symbol==key.SPACE and 1<=len(name.text)<=15:
			name.text+=' '

		elif symbol==key.ENTER and 1<=len(name.text): #if enter is pressed move to game screen
			player.state = 'game_screen'
			player.name = name.text

	elif player.state=='game_screen': #displays gamescreen
		if 97<=symbol<=122 and len(guess.text)<=1:
			guess.text=chr(symbol)#
		elif symbol==key.ENTER and 1==len(guess.text) and len(current_word)>0 and game.tries>0:
			currentguess=guess.text 
			if engine.letterchecker(current_word,guess.text,player,game)==True:
				#correctguesses.append(guess.text)
				print(correctguesses)
				condition=True
			guess.text=''
		if game.tries==0:
			player.state='gameover_screen' #exits the screen to gameoverscreen
			print('You lose')
		elif len(current_word)==0:
			player.score+=10
			player.state='gameover_screen'

	if player.state=='gameover_screen':
		score+=player.score
		finalscore.text+=str(player.score)
		print(score)#
			

#keyboard events
@window.event
def on_text_motion(motion):
	if player.state =='name_input_screen':
		if motion == key.MOTION_BACKSPACE and len(name.text)>0:
			name.text=name.text[:-1]

	elif player.state=='game_screen': #player's guess letter
		if motion == key.MOTION_BACKSPACE and len(guess.text)>0:
			guess.text=guess.text[:-1]


@window.event #for displaying things in the window
def on_draw():
	window.clear()

	if player.state=='name_input_screen':
		interface.input_name_text.draw()
		name.draw()
		if len(name.text)>0:
			interface.enter_to_start_text.draw()

	elif player.state=='start_screen':
		interface.bg.blit(0,0)
		interface.home_batch.draw()


	elif player.state=='game_screen': 
		interface.bg.blit(0,0)
		interface.game_screen(game.tries,player.score,game.letters)

		guess.draw()

	elif player.state=='gameover_screen':
		interface.bg.blit(0,0)
		interface.gameover.draw()
		finalscore.draw()
		





@window.event
def update(dt):
	pass


if __name__ == "__main__":
	pyglet.clock.schedule_interval(update, 1/60)
	pyglet.app.run()