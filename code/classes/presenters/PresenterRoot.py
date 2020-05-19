class PresenterRoot(object):

	def __init__(self,
		_view,
		_model):
		
		self.view = _view
		self.model = _model
	
	
	def run(self):
		self.view.mainloop()