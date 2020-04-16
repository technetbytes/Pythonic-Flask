import redis
from config.cache import CacheConfiguration
from utilities import constant

class DataDeposit:
    '''This is cache class that provide a bridge for different type of caches'''
    
    def __init__(self,cache_type):
        if cache_type is None:
            self.cache_type = constant.CACHE_TYPE_REDIS
        elif cache_type:
            pass

    def load_config(self):
        if self.cache_type == constant.CACHE_TYPE_REDIS:
            config = CacheConfiguration(None)
            cache_host = config.host
            cache_password = config.password
            cache_port = config.port
            self.cache = redis.Redis(host=cache_host, port=cache_port, password=cache_password)
        elif self.cache_type == constant.CACHE_TYPE_MEMCACHED:
            pass

    def get_item(self, key):
        if self.cache is not None:
            return self.cache.get(key)
    
    def set_item(self, key, data):
        if self.cache is not None:
            self.cache.set(key, data)