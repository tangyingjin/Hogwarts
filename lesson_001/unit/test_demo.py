import unittest
class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setupclass")

    def setUp(self) -> None:
        print("setup")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownclass")
    def test_sum(self):
        x=1+2
        print(x)
        self.assertEqual(4,x,f'x={x}  expection=3')
    def test_demo(self):
        self.assertEqual(False)

if __name__=='__main__':
    unittest.main()