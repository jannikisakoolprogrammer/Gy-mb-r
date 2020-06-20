import tkinter

from code.classes.presenters.Presenter import Presenter


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

	
	def run(self):
		self.view.wait_window(self.view)
	
	
	def ok_clicked(
		self,
		_event = None):
		if self.validate_input() == True:
			self.view.withdraw()
			self.apply()
			self.cancel_clicked()
		else:
			pass # Error msg.
	
	
	def validate_input(self):
		return True
	
	
	def apply(self):
		pass # Override this to send data to model and to handle the data there.
	
	
	def cancel_clicked(
		self,
		_event = None):
		self.view.parent.focus_set()
		self.view.destroy()