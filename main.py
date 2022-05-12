from tkinter import ttk
import tkinter as tk
from glob import glob
from PIL import ImageTk, Image
from random import random

class DiceRoller (tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.dices = 6
		self.columns = 3
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
		self.dice_size = int(175 / self.dices * (self.dices/2))
		self.logos = [ImageTk.PhotoImage(Image.open(self.images[i]).resize((self.dice_size,self.dice_size),Image.ANTIALIAS)) for i in range(len(self.images))]
		self.result = 0
		self.widgets = self.get_widgets()

	def get_widgets(self):
		tk.Label(self, background=self.colors['light-green'], text='Welcome to the Dice Rolling App!', font=('Calibri', 30, 'bold')).pack(pady=30)
		self.dice_frame = tk.Frame(self, background = 'white')
		self.dice_frame.pack()
		
		if self.dices < 3:
			self.columns = self.dices
		elif self.dices % 3 == 0:
			self.columns = 3
		else:
			self.columns = 4

		for i in range(self.dices):
			tk.Label(self.dice_frame, image = self.logos[5], borderwidth=0).grid(row=int(i/self.columns), column = i-int(i/self.columns)*self.columns, padx=10)

		tk.Label(self, text='Select number of dices:', font=('Calibri', 15)).pack(pady=(40,10))
		self.dice_var = tk.StringVar(self)
		self.dice_var.trace('w', lambda name, index, mode: self.get_dices_num())
		
		self.dice_selection = ttk.Combobox(self, values=list(range(1,13)), state='readonly', textvariable=self.dice_var)
		self.dice_selection.current(self.dices-1)
		self.dice_selection.pack()
		tk.Button(self, text='Roll the dice(s)', bg=self.colors['light-green'], font=('Calibri', 15, 'bold'), command=lambda: self.roll_dice()).pack(pady=20)
		self.result_lbl = tk.Label(self, text='', font=('Calibri', 15, 'bold'))
		self.result_lbl.pack()
	
	def get_dices_num(self):
		selection = int(self.dice_selection.get())
		if selection != self.dices:
			for widget in self.winfo_children():
				widget.destroy()
			
			self.dices = selection
			self.get_widgets()


	def roll_dice(self):
		self.result = 0
		for label in self.dice_frame.winfo_children():
			random_index = int(random()*len(self.images))
			self.result += random_index + 1
			image = self.logos[random_index]
			label.configure(image=image)
			label.image = image
		
		self.result_lbl.configure(text='You got {}'.format(self.result))






root = DiceRoller()
root.mainloop()