from pydantic import BaseSettings

class Settings(BaseSettings):
	login: str
	password: str
	
	accounts: str
	accounts_origin: str
	name_ru: str
	name_en: str
	price: str
	description: str
	discount_value: bool
	info_for_buyer: str
	
	path_to_accs: str
	path_to_chromedriver: str
	class Config():
		env_file = "cfg.env"
		env_file_encoding = "utf-8"
		
_settings = Settings()
