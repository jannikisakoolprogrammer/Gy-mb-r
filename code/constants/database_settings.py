import os.path

# A fájl útvonalok.
DATABASE_DIRECTORY = "database"

# Az adatbázis neve.
DATABASE_NAME = "ginger.db"

# A fájl útvonal a adatbázishoz.
DATABASE_FILEPATH = os.path.join(
	DATABASE_DIRECTORY,
	DATABASE_NAME)	

# Az táblázat a rendszeres beállításoknak.
TABLE_SYSTEM_SETTINGS = "system_settings"
TABLE_SYSTEM_SETTINGS_CREATE = """
CREATE TABLE IF NOT EXISTS %s (
	system_language TEXT,
	created_datetime TEXT,
	modified_datetime TEXT) """ % (TABLE_SYSTEM_SETTINGS)

