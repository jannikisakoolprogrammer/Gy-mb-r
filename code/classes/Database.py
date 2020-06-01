import sqlite3

from code.constants import database_settings


class Database(object):
	
	def __init__(self):
	
		# A tárgy az adatbázis kapcsolatnak.
		self.connection = None
		
		# A tárgy az cursornak.
		self.cursor = None
		
		# Itt, az adatbázist és a táblázatot előállítom.
		self.connection = sqlite3.connect(database_settings.DATABASE_FILEPATH)		
		self.init_system_settings_table()
		self.cursor = self.connection.cursor()
	
	
	def init_system_settings_table(self):
		self.connection.execute(database_settings.TABLE_SYSTEM_SETTINGS_CREATE)