import tkinter


class Presenter(object):

	def __init__(self,
		_view,
		_model,
		_parent_presenter = None):
		
		self.view = _view
		self.model = _model
		self.parent_presenter = _parent_presenter
	
	
	def run(self):
		self.view.mainloop()