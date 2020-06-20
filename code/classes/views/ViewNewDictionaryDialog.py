import tkinter

from code.classes.views.ViewDialog import ViewDialog


class ViewNewDictionaryDialog(ViewDialog):
	def __init__(
		self,
		_parent,
		_title = None):
		
		super(
			ViewNewDictionaryDialog,
			self).__init__(
				_parent,
				_title)
			