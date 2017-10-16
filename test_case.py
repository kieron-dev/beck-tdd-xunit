from test_result import TestResult

class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp();
        try:
            method = getattr(self, self.name)
            method()
        except Exception as e:
            print e
            result.testFailed()
        self.tearDown()
        return result
