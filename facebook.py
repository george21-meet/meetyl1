class User():
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		self.posts=[]
	def addfriend(self,email1,friends_list):
		self.email1=email1
		self.friends_list.append(self.email1)
		print(self.name,"has added",self.email1,"as a friend")
	def removefriend(self,email2,friends_list):
		self.email2=email2
		self.friends_list.remove(email2)
		print(self.name,"has removed",self.email1,"as a friend")
	def post(self,text):
		self.text=text
		self.posts.append(self.text)
		print(self.name,"has posted",text)
	def get_userinfo(self):
		print("name:",self.name)
		print("email:",self.email)
		print("password:",self.password)
		print("friends list:",self.friends_list)
		print("posts:",self.posts)
	def addmessage(self,message):
		self.message=message
		messagelist=[]
		messagelist.append(self.message)
	def recievemessage(self,fromwho):
		self.fromwho=fromwho
		print(self.name," has recieved the message ",self.fromwho.message)

user1=User("loai","loai17@meet.mit.edu","myhiddenpassword123")
user2=User("anas","aabbassi@js-bethlehem.com","123456")
user1.addfriend(user2.email,user1.friends_list)
user1.post("hi my name is loai")
user1.get_userinfo()
user1.removefriend(user2.email,user1.friends_list)
user1.addmessage("hello i am mark")
user2.recievemessage(user1)