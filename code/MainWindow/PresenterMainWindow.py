import tkinter
import tkinter.ttk

import code.MainWindow.ConstantsMainWindow as CONSTANTSMAINWINDOW

from code.Presenter import Presenter

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


class PresenterMainWindow(Presenter):

	def __init__(self,
		_view,
		_model):
		
		super(
			PresenterMainWindow,
			self).__init__(
				_view,
				_model)

		
		# Előállítom az eventhandlereket.
		# Új nyelvnek:
		self.view.tkinter_menu_file.entryconfig(
			"Új nyelv",
			command = self.new)
		
		# Nyit nyelvnek:
		self.view.tkinter_menu_file.entryconfig(
			"Nyit nyelv",
			command = self.open)
			
		# Ment gyömbernek:
		self.view.tkinter_menu_file.entryconfig(
			CONSTANTSMAINWINDOW.EXIT_BUTTON,
			command = self.view.master.destroy)

			
	def new(self):
	
		view_local = ViewNewDictionaryDialog(self.view)
		model_local = ModelNewDictionaryDialog(self.model.database)
		presenter_local = PresenterNewDictionaryDialog(
			view_local,
			model_local,
			self)
			
		presenter_local.run()

		
	def open(self):
	
		view_local = ViewOpenDictionaryDialog(self.view)
		model_local = ModelOpenDictionaryDialog(self.model.database)
		presenter_local = PresenterOpenDictionaryDialog(
			view_local,
			model_local,
			self)
		
		presenter_local.run()