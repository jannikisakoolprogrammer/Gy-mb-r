import tkinter

from code.PresenterDialog import PresenterDialog


class PresenterOpenDictionaryDialog(PresenterDialog):	
	def __init__(
		self,
		_view,
		_model,
		_parent_presenter,
		_title = None):
		
		super(
			PresenterOpenDictionaryDialog,
			self).__init__(
				_view,
				_model,
				_parent_presenter,
				_title)
	
	
	def populate(self):
		rows = self.model.fetch_all()
		
		# Insert into view listbox.
		self.populate_tk_listbox_dictionaries(rows)
	
	
	def populate_tk_listbox_dictionaries(
		self,
		_rows):
		for row in _rows:
			self.view.tk_listbox_dictionaries.insert(
				tkinter.END,
				"%s <-> %s" % (
					row[1],
					row[2]))		