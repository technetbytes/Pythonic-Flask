import configparser
from utilities import constant
from config.configuration import Configuration

class LogConfiguration(Configuration):
    '''This is logger configuration reader class'''
    
    @property
    def log(self):
        return self.get_section(constant.CONFIG_SECTION_LOG)[constant.LOG_INFO]

    @property
    def error(self):
        return self.get_section(constant.CONFIG_SECTION_LOG)[constant.LOG_ERRORS]
