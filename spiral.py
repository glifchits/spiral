def spiral(rows, cols):
	pass



import unittest

class TestSpiral(unittest.TestCase):

	def test_54(self):
		expected = [
			[  1,  2,  3,  4],
			[ 14, 15, 16,  5],
			[ 13, 20, 17,  6],
			[ 12, 19, 18,  7],
			[ 11, 10,  9,  8]
		]
		result = spiral(5, 4)
		self.assertEqual(expected, result)

	def test_22(self):
		expected = [
			[1, 2],
			[4, 3]
		]
		result = spiral(2, 2)
		self.assertEqual(expected, result)


if __name__ == "__main__":
	unittest.main()