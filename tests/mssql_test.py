import unittest
from db import mssql

def connect_mssql():
    obj_sql = mssql.MsSqlDb(None)
    conn = obj_sql.get_connection
    if conn is None:
        return False
    else:
        return True

class MyTest(unittest.TestCase):
    def test(self):
        self.assertTrue(connect_mssql(), True)
        
if __name__ == '__main__':
    unittest.main()