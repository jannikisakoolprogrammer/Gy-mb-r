import tkinter

from code.classes.presenters.PresenterDialog import PresenterDialog


class PresenterNewDictionaryDialog(PresenterDialog):	
	def __init__(
		self,
		_view,
		_model,
		_parent_presenter,
		_title = None):
		
		super(
			PresenterNewDictionaryDialog,
			self).__init__(
				_view,
				_model,
				_parent_presenter,
				_title)
				
				
	def validate_input(self):
		return True
	
	
	def apply(self):
		pass