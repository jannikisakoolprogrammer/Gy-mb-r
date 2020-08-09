import tkinter
import tkinter.ttk


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
		#self.master.minsize(600, 400)
		#self.master.geometry("800x300")	
		
		# Ablakok
		self.tk_frame_create()
		
		#self.configure_columns()
		#self.configure_rows()
		
		# Pack all controls.
		self.pack(
			expand = True,
			fill = tkinter.BOTH)
	
	
	def tk_frame_create(self):
		self.tk_frame = tkinter.Frame(
			self)
		self.tk_frame.grid(
			row = 0,
			column = 0,
			sticky = "nsew")
			
		# Gyömbér
		self.tk_label_heading = tkinter.Label(
			self.tk_frame,
			text = "Gyömbér",
			font = (
				"Arial",
				30))
		self.tk_label_heading.grid(
			row = 0,
			column = 0,
			columnspan = 9)
		
		# Subheading
		self.tk_label_subheading = tkinter.Label(
			self.tk_frame,
			text = "Just a tool to learn Hungarian vocabulary =]",
			font = (
				"Arial",
				10),
			fg = "grey")
		self.tk_label_subheading.grid(
			row = 1,
			column = 0,
			columnspan = 9,
			sticky = "n")
		
		# Show number of entries
		self.tk_label_number_of_entries = tkinter.Label(
			self.tk_frame)
		self.tk_label_number_of_entries.config(
			font = (
				"Arial",
				10))
		self.tk_label_number_of_entries.grid(
			row = 2,
			columnspan = 9,
			column = 0)
		
		# Show done entries.
		self.tk_label_current = tkinter.Label(
			self.tk_frame)
		self.tk_label_current.config(
			font = (
				"Arial",
				10))
		self.tk_label_current.grid(
			row = 3,
			columnspan = 9,
			column = 0)	
		
		# Word to guess
		self.tk_label_word_to_guess = tkinter.Label(
			self.tk_frame)
		self.tk_label_word_to_guess.config(
			font = (
				"Arial",
				20),
			wraplength="12cm")
		self.tk_label_word_to_guess.grid(
			row = 4,
			column = 0,
			columnspan = 9)	
		
		
		# User input
		self.tk_entry_user_input = tkinter.Entry(
			self.tk_frame)
		self.tk_entry_user_input.config(
			font = (
				"Courier New",
				20),
			justify = "center")
		self.tk_entry_user_input.grid(
			row = 5,
			column = 0,
			columnspan = 9,
			sticky="we")
		
		
		# Check
		self.tk_button_check = tkinter.Button(
			self.tk_frame,
			text = "Check")
		self.tk_button_check.grid(
			row = 6,
			column = 0,
			columnspan = 9,
			sticky="we")
			
					
		# Hint
		self.tk_label_hint = tkinter.Label(
			self.tk_frame)
		self.tk_label_hint.config(
			font = (
				"Courier New",
				20))
		self.tk_label_hint.grid(
			row = 7,
			column = 0,
			columnspan = 9,
			sticky = "we")				
	
		
		# Hint button
		self.tk_button_hint = tkinter.Button(
			self.tk_frame,
			text = "Hint")
		self.tk_button_hint.grid(
			row = 8,
			column = 0,
			columnspan = 9,
			sticky="we")
		
		
		# Buttons for hungarian only letters
		self.tk_button_1 = tkinter.Button(
			self.tk_frame,
			text = "Á")
		self.tk_button_1.config(
			font = (
				"Courier New",
				14))
		self.tk_button_1.grid(
			row = 9,
			column = 0,
			sticky="we")
		
		self.tk_button_2 = tkinter.Button(
			self.tk_frame,
			text = "Í")
		self.tk_button_2.config(
			font = (
				"Courier New",
				14))			
		self.tk_button_2.grid(
			row = 9,
			column = 1,
			sticky="we")

		self.tk_button_3 = tkinter.Button(
			self.tk_frame,
			text = "Ó")
		self.tk_button_3.config(
			font = (
				"Courier New",
				14))			
		self.tk_button_3.grid(
			row = 9,
			column = 2,
			sticky="we")
		
		self.tk_button_4 = tkinter.Button(
			self.tk_frame,
			text = "Ú")
		self.tk_button_4.config(
			font = (
				"Courier New",
				14))			
		self.tk_button_4.grid(
			row = 9,
			column = 3,
			sticky="we")
		
		self.tk_button_5 = tkinter.Button(
			self.tk_frame,
			text = "É")
		self.tk_button_5.config(
			font = (
				"Courier New",
				14))			
		self.tk_button_5.grid(
			row = 9,
			column = 4,
			sticky="we")	
		
		self.tk_button_6 = tkinter.Button(
			self.tk_frame,
			text = "Ö")
		self.tk_button_6.config(
			font = (
				"Courier New",
				14))			
		self.tk_button_6.grid(
			row = 9,
			column = 5,
			sticky="we")
		
		self.tk_button_7 = tkinter.Button(
			self.tk_frame,
			text = "Ü")
		self.tk_button_7.config(
			font = (
				"Courier New",
				14))			
		self.tk_button_7.grid(
			row = 9,
			column = 6,
			sticky="we")
		
		self.tk_button_8 = tkinter.Button(
			self.tk_frame,
			text = "Ő")
		self.tk_button_8.config(
			font = (
				"Courier New",
				14))			
		self.tk_button_8.grid(
			row = 9,
			column = 7,
			sticky="we")
		
		self.tk_button_9 = tkinter.Button(
			self.tk_frame,
			text = "Ű")
		self.tk_button_9.config(
			font = (
				"Courier New",
				14))			
		self.tk_button_9.grid(
			row = 9,
			column = 8,
			sticky="we")	

		
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
	
		self.tk_frame.grid_columnconfigure(0, weight = 0)
		
		
	def configure_rows(self):	
		self.grid_rowconfigure(0, weight = 1)	
		self.grid_rowconfigure(1, weight = 2)	