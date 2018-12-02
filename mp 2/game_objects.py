import pyglet, engine

class Player: #player's status
	def __init__(self):
		self.name = ''
		self.score = 0
		self.state = 'start_screen'

	def update(self):
		pass


class Game: #diko pa rin gets kung ano to pero kailangan siya iyak. update, medyo gets ko na. although not fluent
	def __init__(self, missing_word, num_of_tries):
		self.word = missing_word.lower()
		self.tries = num_of_tries
		self.letters = engine.generate_letters(self.word)


class Display_input: #easy shortcut for displaying stuffs
	def __init__(self,text,posx,posy,size,color=(255,255,255,255)):
		self.text = text
		self.posx = posx
		self.posy = posy
		self.size = size
		self.color = color

	def draw(self):
		pyglet.text.Label(self.text.upper(),
                          font_name='Times New Roman',
                          font_size=self.size,
                          x=self.posx, y=self.posy,
            	          anchor_x='center', anchor_y='center', color=self.color).draw()