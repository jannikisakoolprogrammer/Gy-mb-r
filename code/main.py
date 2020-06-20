import tkinter
import tkinter.ttk


from code.classes.Database import Database

from code.classes.presenters.PresenterRoot import PresenterRoot
from code.classes.views.ViewRoot import ViewRoot
from code.classes.models.ModelRoot import ModelRoot		



def main():
	database = Database()
	root_tk = tkinter.Tk()
	view_root = ViewRoot(root_tk);
	model_root = ModelRoot(database);	
	presenter_root = PresenterRoot(
		view_root,
		model_root)
		
	presenter_root.run()