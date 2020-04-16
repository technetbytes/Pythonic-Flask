import unittest
from assets import file_storage

def load_config():
    storage = file_storage.FileManager(None).load_config()
    if storage is None:
        return False
    else:
        return True

def upload_file():
    storage = file_storage.FileManager(None).load_config()
    if storage is None:        
        return False
    else:
        #storage.upload_file("/home/saqib/Pictures/ijmal.png","ijmalbhai")
        return True

def get_file():
    storage = file_storage.FileManager(None)
    if storage is None:        
        return False
    else:
        storage.get_image("https://res.cloudinary.com/dnbcbz9eu/image/upload/v1586115769/ijmalbhai.png")
        return True
    
class AssetTest(unittest.TestCase):
    '''This is Asset Test Class'''
    
    def test_loadconfig(self):
        self.assertFalse(load_config(), False)
    
    def test_uploadfile(self):
        self.assertFalse(upload_file(), False)
            
    def test_get_file(self):
        self.assertTrue(get_file(), True)
        

if __name__ == '__main__':
    unittest.main()