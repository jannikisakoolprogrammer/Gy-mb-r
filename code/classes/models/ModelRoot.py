from code.classes.models.Model import Model


class ModelRoot(Model):
	def __init__(
		self,
		_database):
		super(
			ModelRoot,
			self).__init__(_database)