import sqlalchemy
#from model import Base, Student
#from sqlalchemy import create_engine
#from sqlalchemy.orm import  sess
#Base=declarative_base()
userlist=[]
passwordlist=[]
posts=[]
comments=[]
posts_list=[]
class post():
	def __init__(self,text,list4,name):
		self.text=text
		self.list=list4
		self.name=name
		self.list.append(self.text)
		print(self.name,"has posted",self.text)
		posts_list.append(self.text)
class User():
	def __init__(self,name,email,password):
		#__tablename__='datatable'
		#name=column(String,primary_key=True)
		#email=column(email)
		#password=column(password)
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		userlist.append(self.name)
		passwordlist.append(self.password)
	def addfriend(self,email1,friends_list):
		self.email1=email1
		self.friends_list.append(self.email1)
		print(self.name,"has added",self.email1,"as a friend")
	def removefriend(self,email2,friends_list):
		self.email2=email2
		self.friends_list.remove(email2)
		print(self.name,"has removed",self.email1,"as a friend")
	def get_userinfo(self):
		print("name:",self.name)
		print("email:",self.email)
		print("password:",self.password)
		print("friends list:",self.friends_list)
		print("posts:",posts)
	def addmessage(self,message):
		self.message=message
		messagelist=[]
		messagelist.append(self.message)
	def post1(self,text1,list1):
		self.list1=list1
		self.text1=text1
		a=post(self.text1,self.list1,self.name)
		print(a)
	def recievemessage(self,fromwho):
		self.fromwho=fromwho
		print(self.name," has recieved the message ",self.fromwho.message)
	def addusertolist(self):
		userlist.append(self.User)
		password.append(self.password)
	def comment(self,post3,comment1):
		self.post=post3
		self.comment1=comment1
		print(self.name,"has commented on",self.post,self.comment1)
		comments.append(self.comment1)
	def like(self,post4,):
		self.post1=post4
		print(self.name,"has liked",self.post)

user1=User("loai","loai17@meet.mit.edu","myhiddenpassword123")
user2=User("anas","aabbassi@js-bethlehem.com","123456")
user1.addfriend(user2.email,user1.friends_list)
user1.post1("hi my name is loai",posts)
user1.get_userinfo()
user1.removefriend(user2.email,user1.friends_list)
user1.addmessage("hello i am mark")
user2.recievemessage(user1)
user1.comment(posts[0],"hi loai")
user1.like(posts[0])
print(userlist,passwordlist)
print("enter ur username")
f=open('facebookbase.txt','a')
f.write(userlist)
f.close()

a=input()
if a in userlist:
	print("enter ur password")
	b=input()
	if b in passwordlist:
		print("u got in")
		print(user1)
else:
	print("username not in")