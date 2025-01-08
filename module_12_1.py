import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
	
	def setUp(self):
		self.tr=Runner('Name1')
		self.tw=Runner('Name2')
	
	def test_walk(self):
		for i in range(10):
			self.tw.walk()
		self.assertEqual(self.tw.distance,50)

	def test_run(self):
	    for i in range(10):
	        self.tr.run()
	    self.assertEqual(self.tr.distance,100)

	def test_challenge(self):
		for i in range(10):
			self.tw.walk()
			self.tr.run()
		self.assertNotEqual(self.tw.distance,self.tr.distance)

if __name__ == '__main__':
    unittest.main()