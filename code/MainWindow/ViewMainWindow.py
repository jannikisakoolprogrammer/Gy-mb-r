import tkinter
import tkinter.ttk

import code.MainWindow.ConstantsMainWindow as CONSTANTSMAINWINDOW


class ViewMainWindow(tkinter.Frame):
	def __init__(self,
		_master):
		super().__init__(_master)
		
		# Init instance members used throughout the entire class with a default
		# value.
		self.master = None
		
		
		# Menu
		self.tkinter_menu = None
		self.tkinter_menu_file = None
		
		# Frames
		self.tkinter_frame = None
		
		# Master
		self.master = _master		
		self.master.geometry("400x400")			
		
		# Ablakok
		self.tk_frame_create()
		
		self.configure_columns()
		#self.configure_rows()
		
		# Pack all controls.
		self.pack(
			expand = True,
			fill = tkinter.BOTH)
	
	
	def tk_frame_create(self):
		self.tk_frame = tkinter.Frame(
			self)
		self.tk_frame.pack()
		#self.tk_frame.grid(
		#	row = 0,
		#	column = 0,
		#	sticky = "nsew")
			
		# Gyömbér
		self.tk_label_heading = tkinter.Label(
			self.tk_frame,
			text = "Gyömbér",
			font = (
				"Font",
				20))
		self.tk_label_heading.pack()
		
		# Word to guess
		self.tk_label_word_to_guess = tkinter.Label(
			self.tk_frame)
		self.tk_label_word_to_guess.config(
			font = (
				"Arial",
				30))
		self.tk_label_word_to_guess.pack()
		
		# User input
		self.tk_entry_user_input = tkinter.Entry(
			self.tk_frame)
		self.tk_entry_user_input.config(
			font = (
				"Arial",
				20),
			justify = "center")
		self.tk_entry_user_input.pack()
		
		# Check
		self.tk_button_check = tkinter.Button(
			self.tk_frame,
			text = "Check")
		self.tk_button_check.pack()
				
			
			
	def configure_columns(self):
		self.grid_columnconfigure(0, weight = 1)	
		
		
	def configure_rows(self):	
		self.grid_rowconfigure(0, weight = 10)	