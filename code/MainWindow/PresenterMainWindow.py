import tkinter
import tkinter.ttk

from code.Base.Presenter import Presenter

	
from constants import labels_en as labels


class PresenterMainWindow(Presenter):

	def __init__(
		self,
		_model):
		
		super(
			PresenterMainWindow,
			self).__init__(_model)	
	
	
	def set_view(
		self,
		_view):
		
		self.view = _view
	
	
	def init_view(self):
	
		# Show number of entries of words
		self.view.set_number_of_entries(
			self.model.get_number_of_entries())	
	
		# Load next word pair.
		self.load_next_word_pair()	
		
		# Show current word counter
		self.view_update_current_word_counter()
		
		# Set word to guess in view.
		self.view.set_word_to_guess(
			self.model.source_word)
		
		# Enable hint button.
		self.view.enable_hint_button()
		
		# Make hint blank.
		self.view.set_hint_blank()


	def add_special_letter(
		self,
		_event):
		
		"""Adds special letter to the text input field where the cursor is
		located.
		"""
		
		char = _event.widget["text"].lower()
		
		user_input = tkinter.StringVar()
		user_input.set(self.view.tk_entry_user_input.get() + char)
		
		self.view.tk_entry_user_input.config(
			text = user_input)
			
		self.view.tk_entry_user_input.icursor(
			len(user_input.get()))		
		
	
	def view_update_current_word_counter(self):
	
		self.view.set_current(self.model.get_current_word_counter())			

	
	def load_next_word_pair(self):
	
		self.model.next_word_pair()

	
	
	def check(self, _e = None):
	
		user_input = self.view.get_user_input()
		
		if user_input.lower() == self.model.target_word.lower():
			
			self.view.tk_entry_user_input.delete(0, tkinter.END)
			self.view.tk_entry_user_input.insert(0, "")
		
			self.load_next_word_pair()
			
			# Show current word counter
			self.view_update_current_word_counter()		
			
			# Set word to guess in view.
			self.view.set_word_to_guess(
				self.model.source_word)			
			
			# Enable hint button.
			self.view.enable_hint_button()
			
			# Make hint blank.
			self.view.set_hint_blank()			
	
	
	def hint(self, _E = None):
		# Hint 1: Convert printable chars to underscores
		# Other hints:  Turn one underscore into the printable char.
		# Do this until the word is displayed.
		
		# Check if any more hints can be made:
		if self.model.get_cur_hint() >= self.model.get_n_hints():	
			# No more hints possible.
			return
		else:
			if self.model.get_cur_hint() == 0:
				# Show masked word first.
				self.view.set_hint(self.model.get_hint_word())
			else:
				# Reveal one printable char.
				self.model.reveal_char()
				self.view.set_hint(self.model.get_hint_word())
				
			self.model.increment_cur_hint()
			
			if self.model.get_cur_hint() >= self.model.get_n_hints():
			
				# Deactivate Hint button.
				self.view.disable_hint_button()