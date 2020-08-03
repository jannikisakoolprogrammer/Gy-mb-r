import tkinter
import tkinter.ttk

import code.MainWindow.ConstantsMainWindow as CONSTANTSMAINWINDOW

from code.Base.Presenter import Presenter

# NewDictionaryDialog
from code.NewDictionaryDialog.PresenterNewDictionaryDialog \
	import PresenterNewDictionaryDialog
from code.NewDictionaryDialog.ViewNewDictionaryDialog \
	import ViewNewDictionaryDialog
from code.NewDictionaryDialog.ModelNewDictionaryDialog \
	import ModelNewDictionaryDialog
	
# OpenDictionaryDialog
from code.OpenDictionaryDialog.PresenterOpenDictionaryDialog \
	import PresenterOpenDictionaryDialog
from code.OpenDictionaryDialog.ViewOpenDictionaryDialog \
	import ViewOpenDictionaryDialog
from code.OpenDictionaryDialog.ModelOpenDictionaryDialog \
	import ModelOpenDictionaryDialog
	
# DictionaryWindow
from code.DictionaryWindow.DictionaryWindowView \
	import DictionaryWindowView
from code.DictionaryWindow.DictionaryWindowPresenter \
	import DictionaryWindowPresenter
from code.DictionaryWindow.DictionaryWindowModel \
	import DictionaryWindowModel


class PresenterMainWindow(Presenter):

	def __init__(self,
		_view,
		_model):
		
		super(
			PresenterMainWindow,
			self).__init__(
				_view,
				_model)
		
		self.view.tk_button_check.bind(
			"<Button-1>",
			self.check)
			
		self.view.tk_entry_user_input.bind(
			"<Return>",
			self.check)
			
		self.view.tk_button_1.bind(
			"<Button-1>",
			self.add_letter_1)
			
		self.view.tk_button_2.bind(
			"<Button-1>",
			self.add_letter_2)

		self.view.tk_button_3.bind(
			"<Button-1>",
			self.add_letter_3)
			
		self.view.tk_button_4.bind(
			"<Button-1>",
			self.add_letter_4)	
			
		self.view.tk_button_5.bind(
			"<Button-1>",
			self.add_letter_5)
			
		self.view.tk_button_6.bind(
			"<Button-1>",
			self.add_letter_6)	

		self.view.tk_button_7.bind(
			"<Button-1>",
			self.add_letter_7)
			
		self.view.tk_button_8.bind(
			"<Button-1>",
			self.add_letter_8)	
			
		self.view.tk_button_9.bind(
			"<Button-1>",
			self.add_letter_9)			
			
		# Show number of entries of words
		self.view.tk_label_number_of_entries.config(
			text = "Number of entries: %s" % (self.model.get_number_of_entries()))
		
		# Show current word counter
		self.view_update_current_word_counter()
		
		# Update stats		
		#self.view_update_stats()

	
	def add_letter_1(
		self,
		_event):
	
		user_input = tkinter.StringVar()
		user_input.set(self.view.tk_entry_user_input.get() + "á")
		
		self.view.tk_entry_user_input.config(
			text = user_input)
			
		self.view.tk_entry_user_input.icursor(
			len(user_input.get()))
			
			
	def add_letter_2(
		self,
		_event):
	
		user_input = tkinter.StringVar()
		user_input.set(self.view.tk_entry_user_input.get() + "í")
		
		self.view.tk_entry_user_input.config(
			text = user_input)
			
		self.view.tk_entry_user_input.icursor(
			len(user_input.get()))
			
			
	def add_letter_3(
		self,
		_event):
	
		user_input = tkinter.StringVar()
		user_input.set(self.view.tk_entry_user_input.get() + "ó")
		
		self.view.tk_entry_user_input.config(
			text = user_input)
			
		self.view.tk_entry_user_input.icursor(
			len(user_input.get()))			


	def add_letter_4(
		self,
		_event):
	
		user_input = tkinter.StringVar()
		user_input.set(self.view.tk_entry_user_input.get() + "ú")
		
		self.view.tk_entry_user_input.config(
			text = user_input)
			
		self.view.tk_entry_user_input.icursor(
			len(user_input.get()))			


	def add_letter_5(
		self,
		_event):
	
		user_input = tkinter.StringVar()
		user_input.set(self.view.tk_entry_user_input.get() + "é")
		
		self.view.tk_entry_user_input.config(
			text = user_input)
			
		self.view.tk_entry_user_input.icursor(
			len(user_input.get()))			


	def add_letter_6(
		self,
		_event):
	
		user_input = tkinter.StringVar()
		user_input.set(self.view.tk_entry_user_input.get() + "ö")
		
		self.view.tk_entry_user_input.config(
			text = user_input)
			
		self.view.tk_entry_user_input.icursor(
			len(user_input.get()))			


	def add_letter_7(
		self,
		_event):
	
		user_input = tkinter.StringVar()
		user_input.set(self.view.tk_entry_user_input.get() + "ü")
		
		self.view.tk_entry_user_input.config(
			text = user_input)
			
		self.view.tk_entry_user_input.icursor(
			len(user_input.get()))			


	def add_letter_8(
		self,
		_event):
	
		user_input = tkinter.StringVar()
		user_input.set(self.view.tk_entry_user_input.get() + "ő")
		
		self.view.tk_entry_user_input.config(
			text = user_input)
			
		self.view.tk_entry_user_input.icursor(
			len(user_input.get()))			


	def add_letter_9(
		self,
		_event):
	
		user_input = tkinter.StringVar()
		user_input.set(self.view.tk_entry_user_input.get() + "ű")
		
		self.view.tk_entry_user_input.config(
			text = user_input)	

		self.view.tk_entry_user_input.icursor(
			len(user_input.get()))
	
	
	def view_update_current_word_counter(self):
	
		self.view.tk_label_current.config(
			text = "Entries done: %d" % (self.model.get_current_word_counter()))	
			

	
	def load_next_word_pair(self):
	
		self.model.next_word_pair()
		
		self.view_update_current_word_counter()
		
		self.view.tk_label_word_to_guess.config(
			text = self.model.source_word)
	
	
	def check(self, _e = None):
		user_input = self.view.tk_entry_user_input.get()
		
		if user_input.lower() == self.model.target_word.lower():
		#	self.model.increment_correct_guesses()
		#else:
		#	self.model.increment_incorrect_guesses()
		
		#	self.view_update_stats()
			
			self.view.tk_entry_user_input.delete(0, tkinter.END)
			self.view.tk_entry_user_input.insert(0, "")
		
			self.load_next_word_pair()
			
			self.view_update_current_word_counter()
	
	
	def view_update_stats(self):
	
		# Show number of correct guesses
		self.view.tk_label_correct_guesses.config(
			text = "Correct guesses: %s" % (self.model.get_correct_guesses()))
			
		# Show number of incorrect guesses
		self.view.tk_label_incorrect_guesses.config(
			text = "Incorrect guesses: %s" % (self.model.get_incorrect_guesses()))

			
	def new(self):
	
		view_local = ViewNewDictionaryDialog(self.view)
		model_local = ModelNewDictionaryDialog(self.model.database)
		presenter_local = PresenterNewDictionaryDialog(
			view_local,
			model_local,
			self)
			
		presenter_local.run()
		self.received_return_value = presenter_local.get_return_value()
		
		self.view_update_controls()

		
	def open(self):
	
		view_local = ViewOpenDictionaryDialog(self.view)
		model_local = ModelOpenDictionaryDialog(self.model.database)
		presenter_local = PresenterOpenDictionaryDialog(
			view_local,
			model_local,
			self)
		
		presenter_local.run()
		self.received_return_value = presenter_local.get_return_value()
		
		self.view_update_controls()
	
	
	def view_update_controls(self):
	
		if self.received_return_value == True:
			self.view.frame_center_button_dictionary.configure(state = "normal")
			self.view.frame_center_button_one_out_of_five.configure(state = "normal")
			self.view.tk_frame_buitton_one_after_the_other.configure(state = "normal")
			self.view.tk_frame_button_practice_makes_perfect.configure(state = "normal")
		
		else:
			self.view.frame_center_button_dictionary.configure(state = "disabled")
			self.view.frame_center_button_one_out_of_five.configure(state = "disabled")
			self.view.tk_frame_buitton_one_after_the_other.configure(state = "disabled")
			self.view.tk_frame_button_practice_makes_perfect.configure(state = "disabled")
	
	
	def tk_button_dictionary_clicked(
		self,
		_event = None):
		
		if self.view.frame_center_button_dictionary.cget("state") == "disabled":
			return
		
		view_local = DictionaryWindowView(
			self.view,
			"Szótár",
			"grid")
		model_local = DictionaryWindowModel(self.model.database)
		presenter_local = DictionaryWindowPresenter(
			view_local,
			model_local,
			self)
		
		presenter_local.run()
		self.received_return_value = self.presenter_local.get_return_value()