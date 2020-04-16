import configparser
from utilities import constant
from config.configuration import Configuration

class CacheConfiguration(Configuration):
    '''Using this class we load cache configuration parameters'''
    
    @property
    def host(self):
        return self.get_section(constant.CONFIG_SECTION_CACHE)[constant.CACHE_HOST]

    @property
    def port(self):
        return self.get_section(constant.CONFIG_SECTION_CACHE)[constant.CACHE_PORT]

    @property
    def password(self):
        return self.get_section(constant.CONFIG_SECTION_CACHE)[constant.CACHE_PASSWORD]