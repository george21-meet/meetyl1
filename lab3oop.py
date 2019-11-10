class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound=sound
		self.name=name
		self.age=age
		self.favorite_color=favorite_color
	def eat(self,food):
		print("yummy!!"+self.name+"is eating"+food)
	def description(self):
		print(self.name+" is "+self.age+" years old and loves the color "+self.favorite_color)
	def make_Sound(self,sound):
		for i in range(3):
			print(sound)
#kyle=Animal("bark","dog","11","yellow")
#kyle.description()
#kyle.eat("pasta")
#kyle.make_Sound("woof")
class Person(object):
	def __init__(self,name,age,city,gender):
		self.name=name
		self.age=age
		self.city=city
		self.gender=gender
	def description(self):
		print(self.name+" is "+self.age+" "+self.name+" is from "+"and  their gender is "+self.gender)
	def eat(self,food):
		print(self.name+" is eating "+food)
	def sports(self,sport):
		print(self.name+" is playing "+sport)
	def sexuality(self,sexuality):	
		print(self.name+" is "+sexuality)
#adam=Person("adam","16","Jerusalem","male")
#adam.description()
#adam.eat("pasta")
#adam.sports("soccer")
#adam.sexuality("bi")
class bird(object):
	def __init__(self,name,color,speed):
		self.name=name
		self.color=color
		self.speed=speed
	def description(self):
		print(self.name+" is "+self.color+" and is "+self.speed)
	def getspeed(self):
		print(self.name+" is "+self.speed+" fast ")
	def race(self,bird1):
		a=int(self.speed)
		q=int(bird1.speed)
		if a>q:
			print(self.name+" is faster")
		if q>a:
			print(bird1.name+" is faster")
bob=bird("bob","green","45")
bob.description()
bob.getspeed()
bobby=bird("bobby","yellow","50")
bob.race(bobby)