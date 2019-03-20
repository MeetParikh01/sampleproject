class Clock(object):
	def __init__(self, hour, minute):
		self.hour,self.minute=hour,minute
		
	def myfun(self):
		a,self.minute=divmod(self.minute,60)
		self.hour=(self.hour+a)%24
		return str(self.hour).zfill(2)+":"+str(self.minute).zfill(2)
		

	def __repr__(self):
		return self.myfun()
	
	def __eq__(self, other):
		return True if self.myfun()==other.myfun() else False

	def __add__(self, minutes):
		self.minute+=minutes
		return self.myfun()

	def __sub__(self, minutes):
		self.minute-=minutes
		return self.myfun()

#print("15:36"=="15:37")
#print(str(Clock(11, 9))== '11:09')
