import configparser

class Configuration:
	'''This is a Configuration Reader. This class read configure from config.ini '''
	
	__config_file = "./resources/config.ini"
	def __init__(self, config):
		if config is None:
			self.config = Configuration.__config_file
		else:
			self.config = config

	def get_config(self):
		config = configparser.ConfigParser()                                     
		config.read(self.config)
		return config

	def get_section(self,section):
		config = configparser.ConfigParser()                                     
		config.read(self.config)		
		return config[section]
    