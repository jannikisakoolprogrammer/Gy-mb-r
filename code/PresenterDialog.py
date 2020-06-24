import tkinter
from tkinter import messagebox

from code.Presenter import Presenter


class PresenterDialog(Presenter):
	def __init__(
		self,
		_view,
		_model,
		_parent_presenter,
		_title = None):
		
		super(
			PresenterDialog,
			self).__init__(
				_view,
				_model,
				_parent_presenter)
		
		# Előállítom az eventhandlereket.
		# Oké
		self.view.button_ok.bind(
			"<Button-1>",
			self.ok_clicked)
		
		# Megszakít
		self.view.button_cancel.bind(
			"<Button-1>",
			self.cancel_clicked)
		
		self.error_message = ""
		
		self.populate()		
		
		
	def populate(self):
		pass		
		
	
	def run(self):
		self.view.wait_window(self.view)

	
	def ok_clicked(
		self,
		_event = None):
		
		self.get_input()		
		self.prepare_input()
		
		if ((self.validate_input() == True)
		and (self.check_apply() == True)
		and (self.apply() == True)):	
			self.view.withdraw()
			self.cancel_clicked()
		else:
			tkinter.messagebox.showerror(
				"Error",
				self.error_message,
				parent = self.view)
	
	def get_input(self):
		pass
	
	
	def prepare_input(self):
		pass
	
	
	def validate_input(self):
		return True
	
	
	def check_apply(self):
		return True # Override this for db interactions.
	
	
	def apply(self):
		return True # Override this for db interactions.
	
	
	def cancel_clicked(
		self,
		_event = None):
		self.view.parent.focus_set()
		self.view.destroy()