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
				"Arial",
				30))
		self.tk_label_heading.pack()
		
		# Subheading
		self.tk_label_subheading = tkinter.Label(
			self.tk_frame,
			text = "Just a tool to learn Hungarian vocabulary =]",
			font = (
				"Arial",
				12),
			fg = "grey")
		self.tk_label_subheading.pack()
		
		# Show number of entries
		self.tk_label_number_of_entries = tkinter.Label(
			self.tk_frame)
		self.tk_label_number_of_entries.config(
			font = (
				"Arial",
				14))
		self.tk_label_number_of_entries.pack()
		
		# Show done entries.
		self.tk_label_current = tkinter.Label(
			self.tk_frame)
		self.tk_label_current.config(
			font = (
				"Arial",
				12))
		self.tk_label_current.pack(
			side = tkinter.TOP)		
		
		# Word to guess
		self.tk_label_word_to_guess = tkinter.Label(
			self.tk_frame)
		self.tk_label_word_to_guess.config(
			font = (
				"Arial",
				20))
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
		
		# Buttons for hungarian only letters
		self.tk_button_1 = tkinter.Button(
			self.tk_frame,
			text = "Á")
		self.tk_button_1.config(
			font = (
				"Courier New",
				14))
		self.tk_button_1.pack(
			side = tkinter.LEFT,
			expand = True)
		
		self.tk_button_2 = tkinter.Button(
			self.tk_frame,
			text = "Í")
		self.tk_button_2.config(
			font = (
				"Courier New",
				14))			
		self.tk_button_2.pack(
			side = tkinter.LEFT,
			expand = True)

		self.tk_button_3 = tkinter.Button(
			self.tk_frame,
			text = "Ó")
		self.tk_button_3.config(
			font = (
				"Courier New",
				14))			
		self.tk_button_3.pack(
			side = tkinter.LEFT,
			expand = True)
		
		self.tk_button_4 = tkinter.Button(
			self.tk_frame,
			text = "Ú")
		self.tk_button_4.config(
			font = (
				"Courier New",
				14))			
		self.tk_button_4.pack(
			side = tkinter.LEFT,
			expand = True)
		
		self.tk_button_5 = tkinter.Button(
			self.tk_frame,
			text = "É")
		self.tk_button_5.config(
			font = (
				"Courier New",
				14))			
		self.tk_button_5.pack(
			side = tkinter.LEFT,
			expand = True)	
		
		self.tk_button_6 = tkinter.Button(
			self.tk_frame,
			text = "Ö")
		self.tk_button_6.config(
			font = (
				"Courier New",
				14))			
		self.tk_button_6.pack(
			side = tkinter.LEFT,
			expand = True)
		
		self.tk_button_7 = tkinter.Button(
			self.tk_frame,
			text = "Ü")
		self.tk_button_7.config(
			font = (
				"Courier New",
				14))			
		self.tk_button_7.pack(
			side = tkinter.LEFT,
			expand = True)
		
		self.tk_button_8 = tkinter.Button(
			self.tk_frame,
			text = "Ő")
		self.tk_button_8.config(
			font = (
				"Courier New",
				14))			
		self.tk_button_8.pack(
			side = tkinter.LEFT,
			expand = True)
		
		self.tk_button_9 = tkinter.Button(
			self.tk_frame,
			text = "Ű")
		self.tk_button_9.config(
			font = (
				"Courier New",
				14))			
		self.tk_button_9.pack(
			side = tkinter.LEFT,
			expand = True)		

		
		# Show correct guesses
		#self.tk_label_correct_guesses = tkinter.Label(
	#		self.tk_frame)
	#	self.tk_label_correct_guesses.config(
	#		font = (
	#			"Arial",
	#			12),
	#		fg = "green")
	#	self.tk_label_correct_guesses.pack()
		
		# Show incorrect guesses
	#	self.tk_label_incorrect_guesses = tkinter.Label(
	#		self.tk_frame)
	#	self.tk_label_incorrect_guesses.config(
	#		font = (
	#			"Arial",
	#			12),
	#		fg = "red")
	#	self.tk_label_incorrect_guesses.pack()		
				
			
			
	def configure_columns(self):
		self.grid_columnconfigure(0, weight = 1)	
		
		
	def configure_rows(self):	
		self.grid_rowconfigure(0, weight = 10)	