import tkinter
import tkinter.ttk

from code.constants.Root import ConstantsRoot as CONSTANTSROOT


class PresenterRoot(object):

	def __init__(self,
		_view,
		_model):
		
		self.view = _view
		self.model = _model
		
		# Előállítom az eventhandlereket.
		# Új nyelvnek:
		self.view.tkinter_menu_file.entryconfig(
			"Új nyelv",
			command = self.test)
		
		# Nyit nyelvnek:
		self.view.tkinter_menu_file.entryconfig(
			"Nyit nyelv",
			command = self.open)
			
		# Ment gyömbernek:
		self.view.tkinter_menu_file.entryconfig(
			CONSTANTSROOT.EXIT_BUTTON,
			command = self.view.master.destroy)

			
	def test(self):
		print("Új nyelv gombot.")

		
	def open(self):
		print("Nyit nyelv gombot.")
	
	def run(self):
		self.view.mainloop()