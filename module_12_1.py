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
    def __init__(self, tw: object, tr: object) -> object:
        super.__init__(tw,tr)
        self.test_walk(tw)
        self.test_run(tr)
        self.test_challenge(tw,tr)

    def test_walk(self,tw):
        for i in range(10):
            tw.walk()
        self.assertEqual(tw.distance,50)

    def test_run(self,tr):
        for i in range(10):
            tr.run()
        self.assertEqual(tr.distance,100)

    def test_challenge(self,tw,tr):
        for i in range(10):
            tw.walk()
            tr.run()
        self.assertNotEqual(tw.distance,tr.distance)

if __name__ == '__main__':
    t1=Runner('Sergey')
    t2 = Runner('Svetlana')
    RunnerTest(t1,t2)
