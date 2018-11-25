import pyglet,engine


width,height=800,600

#Object for images
class Image:
	def __init__(self, image,scale=1,batch=None):
		self.image = pyglet.image.load('res/sprites/'+image)
		self.sprite = pyglet.sprite.Sprite(self.image,batch=batch)
		self.sprite.scale=scale

	def position(self,posx,posy):
		self.sprite.position=(posx,posy)

	def draw(self):
		self.sprite.draw()

class Text:
	def __init__(self, text,xpos,ypos,color=(0,0,0,255),anchor_x='left', anchor_y='bottom',font_size=25,batch=None ):
		self.text=text
		self.xpos=xpos
		self.ypos=ypos
		self.color=color
		self.font_size=font_size
		self.batch=batch
		self.anchor_x=anchor_x
		self.anchor_y=anchor_y

	def draw(self):
		pyglet.text.Label(self.text,
	                      font_size=self.font_size,
	                      x=self.xpos, y=self.ypos, anchor_x=self.anchor_x, anchor_y=self.anchor_y,
	        	          color=self.color, batch=self.batch).draw()

	def update(self):
		pass




#white background
bg = pyglet.image.SolidColorImagePattern((230,236,240,255)).create_image(width, height)

#---Start_screen---#
home_batch=pyglet.graphics.Batch()

#Hangman title
title = Image('title.png',batch=home_batch)
title.position(width//2-title.sprite.width//2,(2.5*height)//4)


#playbutton
playbutton = Image('play.png', scale=0.4, batch=home_batch)
playbutton.position(width//2-playbutton.sprite.width//2,height//6)





#---Name_input_screen---#

enter_to_start_text = Text("Press Enter to Start!", width//2, height//4, anchor_x='center', anchor_y='center', color=(255,144,0,255), font_size=40)
input_name_text = Text("Input Name", width//2, (7*height)//8, anchor_x='center', anchor_y='center', color=(255,144,0,255))


#---Start_screen---#


toolbox = pyglet.image.SolidColorImagePattern((255,255,255,255)).create_image(width, 70)
toolbox_shade = pyglet.image.SolidColorImagePattern((210,210,210,255)).create_image(width, 1)

letters_box = pyglet.image.SolidColorImagePattern((255,255,255,255)).create_image(width, 230)
letters_box_shade = pyglet.image.SolidColorImagePattern((210,210,210,255)).create_image(width, 1)
hangman_box = pyglet.image.SolidColorImagePattern((255,255,255,255)).create_image(250, height-(toolbox.height+letters_box.height+40)) #put the hangman animation here



def draw_letterboxes(word): #draws boxes
	n=len(word)
	between_length = 8
	box_width=44
	box_height=50
	start_x1=width//2-((n*box_width)//2+(between_length//2)*(n-1))

	if n>15:
		start_x1=14
		start_x2=width//2-(((n-15)*box_width)//2+(between_length//2)*(n-16))

	if n>30:
		start_x1=14
		start_x2=14
		start_x3=width//2-(((n-30)*box_width)//2+(between_length//2)*(n-31))


	for i in range(n):
		if i<=14:
			pyglet.image.SolidColorImagePattern((74,179,244,255)).create_image(box_width, box_height).blit(start_x1+i*(box_width+between_length),145)
			#pyglet.text.Label(word[i], font_size=25, x=start_x1+i*(box_width+between_length)+box_width//2, y=145+box_height//2, anchor_x='center', anchor_y='center', color=(255,255,255,255)).draw()
		elif i<=29:
			pyglet.image.SolidColorImagePattern((74,179,244,255)).create_image(box_width, box_height).blit(start_x2+(i-15)*(box_width+between_length),80)
			#pyglet.text.Label(word[i], font_size=25, x=start_x2+(i-15)*(box_width+between_length)+box_width//2, y=80+box_height//2, anchor_x='center', anchor_y='center', color=(255,255,255,255)).draw()

		else:
			pyglet.image.SolidColorImagePattern((74,179,244,255)).create_image(box_width, box_height).blit(start_x3+(i-30)*(box_width+between_length),15)
			#pyglet.text.Label(word[i], font_size=25, x=start_x3+(i-30)*(box_width+between_length)+box_width//2, y=15+box_height//2, anchor_x='center', anchor_y='center', color=(255,255,255,255)).draw()


#def letter_appending(letter):
	#letter_in_word=pyglet.text.Label(letter, font_size=25, x=start_x3+(i-30)*(box_width+between_length)+box_width//2, y=15+box_height//2, anchor_x='center', anchor_y='center', color=(255,255,255,255)).draw()


tries = Text("", 10, height-40)
score = Text("", width-300, height-40)

def game_screen(num_tries, num_score, letter_list):
	toolbox.blit(0,height-toolbox.height)
	toolbox_shade.blit(0,height-toolbox.height-toolbox_shade.height)
	hangman_box.blit(width-(hangman_box.width+20),letters_box.height+20)
	letters_box.blit(0,0)
	letters_box_shade.blit(0,letters_box.height)
	tries.text="Tries:{}".format(num_tries)
	score.text="Score:{}".format(num_score)
	tries.draw()
	score.draw()

	draw_letterboxes(letter_list)
