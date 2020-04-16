import configparser
from utilities import constant
from config.configuration import Configuration
 
class DatabaseConfiguration(Configuration):
    '''This is database configuration reader class'''
    
    @property
    def host(self):
        return self.get_section(constant.CONFIG_SECTION_DATABASE)[constant.DB_HOST]

    @property
    def port(self):
        return self.get_section(constant.CONFIG_SECTION_DATABASE)[constant.DB_PORT]

    @property
    def username(self):
        return self.get_section(constant.CONFIG_SECTION_DATABASE)[constant.DB_USERNAME]

    @property
    def db_name(self):
        return self.get_section(constant.CONFIG_SECTION_DATABASE)[constant.DB_NAME]

    @property
    def password(self):
        return self.get_section(constant.CONFIG_SECTION_DATABASE)[constant.DB_PASSWORD]
    
    @property
    def driver(self):
        return self.get_section(constant.CONFIG_SECTION_DATABASE)[constant.DB_DRIVER_NAME]