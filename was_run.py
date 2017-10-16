from test_case import TestCase

class WasRun(TestCase):
    def setUp(self):
        self.log = "setUp "

    def tearDown(self):
        self.log += "tearDown "

    def testMethod(self):
        self.log += "testMethod "
