import tkinter
import tkinter.ttk

from code.constants.Root import ConstantsRoot as CONSTANTSROOT

from code.classes.presenters.Presenter import Presenter

# NewDictionaryDialog
from code.classes.presenters.PresenterNewDictionaryDialog \
	import PresenterNewDictionaryDialog
from code.classes.views.ViewNewDictionaryDialog \
	import ViewNewDictionaryDialog
from code.classes.models.ModelNewDictionaryDialog \
	import ModelNewDictionaryDialog


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
			CONSTANTSROOT.EXIT_BUTTON,
			command = self.view.master.destroy)

			
	def new(self):
		view_local = ViewNewDictionaryDialog(self.view)
		model_local = ModelNewDictionaryDialog(self.model.database)
		presenter_local = PresenterNewDictionaryDialog(
			view_local,
			model_local,
			self)
		presenter_local.run()
		#print("Új nyelv gombot.")

		
	def open(self):
		print("Nyit nyelv gombot.")