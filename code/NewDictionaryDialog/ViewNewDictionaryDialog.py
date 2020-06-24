import tkinter

from code.ViewDialog import ViewDialog


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
	
	
	def setup_body(self):
		# self.body
		
		# Forrás nyelv
		self.tk_label_source_language = tkinter.Label(
			self.body,
			text = "Forrás nyelv")
		self.tk_label_source_language.pack()
		
		self.tk_entry_source_language = tkinter.Entry(self.body)
		self.tk_entry_source_language.pack()
		
		# Cél nyelv
		self.tk_label_target_language = tkinter.Label(
			self.body,
			text = "Cél nyelv")
		self.tk_label_target_language.pack()
		
		self.tk_entry_target_language = tkinter.Entry(self.body)
		self.tk_entry_target_language.pack()
		
			