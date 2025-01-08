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
	
	def test_walk(self):
		tw=Runner('Name1')
		for i in range(10):
			tw.walk()
		self.assertEqual(tw.distance,50)

	def test_run(self):
	    tr=Runner('Name2')
	    for i in range(10):
	        tr.run()
	    self.assertEqual(tr.distance,100)

	def test_challenge(self):
		tw=Runner('Name3')
		tr=Runner('Name4')
		for i in range(10):
			tw.walk()
			tr.run()
		self.assertNotEqual(tw.distance,tr.distance)

if __name__ == '__main__':
    unittest.main()