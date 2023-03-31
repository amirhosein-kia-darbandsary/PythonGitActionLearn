import unittest
from source.main import read_logger_name
import os   
class TestEnv(unittest.TestCase):

    def test_env(self):
        name = read_logger_name()
        expected =  os.environ['USER_GIT']
        print(os.environ['TESTING_PACKAGE'])
        self.assertEqual(name,)


