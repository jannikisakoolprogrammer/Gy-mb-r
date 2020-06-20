import tkinter

from code.classes.models.Model import Model

class ModelNewDictionaryDialog(Model):
	def __init__(
		self,
		_database):
		super(
			ModelNewDictionaryDialog,
			self).__init__(_database)