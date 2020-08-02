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

	
	def load_next_word_pair(self):
	
		self.model.next_word_pair()
		
		self.view.tk_label_word_to_guess.config(
			text = self.model.source_word)
	
	
	def check(self, _e = None):
		user_input = self.view.tk_entry_user_input.get()
		
		if user_input == self.model.target_word:
			
			self.view.tk_entry_user_input.delete(0, tkinter.END)
			self.view.tk_entry_user_input.insert(0, "")
			
			self.load_next_word_pair()

			
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