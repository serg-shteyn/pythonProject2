from unittest import TestCase, main

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
        
class TournamentTest(TestCase):
	
	@classmethod
	def setUpClass(cls):
		cls.all_results={}
		cls.key=1
		
	def setUp(self):
		self.run1 = Runner('Усэйн', 10)
		self.run2 = Runner('Андрей', 9)
		self.run3 = Runner('Ник', 3)
		
	def test_run1(self):
		running=Tournament(90,self.run1,self.run3)
		self.all_results[self.key]=running.start()
		max_res=max(self.all_results[self.key])
		self.assertTrue(self.run3.name==self.all_results[self.key][max_res])
		self.key+=1
		
	def test_run2(self):
		running=Tournament(90,self.run2,self.run3)
		self.all_results[self.key]=running.start()
		max_res=max(self.all_results[self.key])
		self.assertTrue(self.run3.name==self.all_results[self.key][max_res])
		self.key+=1
		
	def test_run3(self):
		running=Tournament(90,self.run2,self.run1,self.run3)
		self.all_results[self.key]=running.start()
		max_res=max(self.all_results[self.key])
		self.assertTrue(self.run3.name==self.all_results[self.key][max_res])
		self.key+=1
		
	@classmethod	
	def tearDownClass(cls):
		for res in cls.all_results:
			print(res)
			
			
if __name__ == '__main__':
	main()