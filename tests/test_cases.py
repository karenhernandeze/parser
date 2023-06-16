import unittest
import filecmp

# To run test cases. 1) Go to pars.py, run to produce the
# results.txt file. 2) run the tests 3) If true it passed if false it failed

class TestAssetions(unittest.TestCase):

	# Test Case for Test 1
	def test_1(self):
		test_num1 = 'expected_outputs/eo_test4.txt'
		result = filecmp.cmp('output_results/results4.txt', f"{test_num1}")
		self.assertTrue(result)

if __name__ == '__main__':
	unittest.main()