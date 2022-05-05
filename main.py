import itertools
import tkinter as tk
from glob import glob
from PIL import ImageTk, Image
from random import random
from time import sleep

class DiceRoller (tk.Tk):
	def __init__(self, dices):
		tk.Tk.__init__(self)
		self.dices = dices
		self.geometry('600x600')
		self.title('Dice roller')
		self.colors = {'dark-brown':  "#cb997e", 
					   'brown': 	  "#ddbea9", 
					   'light-brown': "#ffe8d6",
					   'light-green': "#b7b7a4", 
					   'green': 	  "#a5a58d", 
					   'dark-green':  "#6b705c"}
		self.images = glob('images\\*.png')
		self.configure(background = 'white')
		self.resizable(0,0)
		self.dice_size = int(250 / self.dices * (self.dices/2))
		self.logos = [ImageTk.PhotoImage(Image.open(self.images[i]).resize((self.dice_size,self.dice_size),Image.ANTIALIAS)) for i in range(len(self.images))]
		self.result = 0
		self.widgets = self.get_widgets()

	def get_widgets(self):
		tk.Label(self, background=self.colors['light-green'], text='Welcome to the Dice Rolling App!', font=('Calibri', 30, 'bold')).pack(pady=30)
		self.dice_frame = tk.Frame(self, background = 'white')
		self.dice_frame.pack()
		for i in range(self.dices):
			tk.Label(self.dice_frame, image = self.logos[5], borderwidth=0).grid(row=int(i/4), column = i-int(i/4)*4, padx=10)

		tk.Button(self, text='Roll the dice(s)', bg=self.colors['light-green'], font=('Calibri', 15, 'bold'), command=lambda: self.roll_dice()).pack(pady=40)
		self.result_lbl = tk.Label(self, text='', font=('Calibri', 15, 'bold'))
		self.result_lbl.pack()
	
	def roll_dice(self):
		self.result = 0
		for label in self.dice_frame.winfo_children():
			random_index = int(random()*len(self.images))
			self.result += random_index + 1
			image = self.logos[random_index]
			label.configure(image=image)
			label.image = image
		
		self.result_lbl.configure(text='You got {}'.format(self.result))






root = DiceRoller(dices=8)
root.mainloop()