import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()


##python -m unittest executed the if __name__ == '__main__':
##unittest.main() to run the single file test.py in the command line

##python -m unittest -v test executed the test for interger sums in test.py

##python -m unittest discover searches the current directory and attempts to test it

##python -m unittest discover -s tests is used to run all tests in the directory

##python -m unittest discover -s tests -t src will run test in the src/ directory