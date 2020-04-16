import configparser
from utilities import constant
from config.configuration import Configuration

class AssetConfiguration(Configuration):
    ''' Assset Configuration Class'''
    
    @property
    def cloud_name(self):
        return self.get_section(constant.CONFIG_SECTION_ASSET)[constant.ASSET_CLOUD_NAME]

    @property
    def api_key(self):
        return self.get_section(constant.CONFIG_SECTION_ASSET)[constant.ASSET_API_KEY]

    @property
    def api_secret(self):        
        return self.get_section(constant.CONFIG_SECTION_ASSET)[constant.ASSET_API_SECRET]