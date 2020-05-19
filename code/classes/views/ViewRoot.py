import tkinter


class ViewRoot(tkinter.Frame):
	def __init__(self,
		_master):
		
		super().__init__(_master)
		
		self.master = _master
		self.pack()