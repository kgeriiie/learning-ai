import unittest
import task_01

class MyTestCase(unittest.TestCase):
    def test_evaluate_failing(self):
        model = TestModel([0, 0, 0, 0])
        y_test = [3,4,0,0]
        X_test = [[0],[1],[2],[3]]
        result = task_01.evaluate(model, X_test, y_test)
        self.assertEqual(result, 2.5)

    def test_evaluate_success(self):
        model = TestModel([3, 4, 0, 0])
        y_test = [3,4,0,0]
        X_test = [[0],[1],[2],[3]]
        result = task_01.evaluate(model, X_test, y_test)
        self.assertEqual(result, 0)

class TestModel:
    def __init__(self, mocked):
        self.mocked = mocked

    def predict(self, X):
        return self.mocked

if __name__ == '__main__':
    unittest.main()
