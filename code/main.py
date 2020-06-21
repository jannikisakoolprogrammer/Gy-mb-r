import tkinter
import tkinter.ttk


from code.classes.Database import Database

from code.classes.presenters.PresenterMainWindow import PresenterMainWindow
from code.classes.views.ViewMainWindow import ViewMainWindow
from code.classes.models.ModelMainWindow import ModelMainWindow		



def main():
	database = Database()
	root_tk = tkinter.Tk()
	view_main_window = ViewMainWindow(root_tk);
	model_main_window = ModelMainWindow(database);	
	presenter_main_window = PresenterMainWindow(
		view_main_window,
		model_main_window)
		
	presenter_main_window.run()