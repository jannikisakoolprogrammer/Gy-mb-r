import abc
from code.Base.IView import IView


class IViewMainWindow(
	IView,
	abc.ABC):
	
	@abc.abstractmethod
	def set_number_of_entries(
		self,
		_number_of_entries):
		
		pass
	
	
	@abc.abstractmethod
	def set_current(
		self,
		_current):
		
		pass
	
	
	@abc.abstractmethod
	def set_word_to_guess(
		self,
		_word_to_guess):
		
		pass
	
	
	@abc.abstractmethod
	def get_user_input(self):
	
		pass
	
	
	@abc.abstractmethod
	def set_hint(
		self,
		_hint):
		
		pass