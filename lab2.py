"""
def commonlist():
	print("hi")
	w=0
	int1=input()
	int2=input()
	accint1=sorted(int1)
	accint2=sorted(int2)
	q=len(accint1)
	for i in range(q):
		if accint1[i] in accint2 and accint1[i]!='[' and accint1[i]!=',' and accint1[i]!=']':
			print(accint1[i])
			r=accint1[i]
			e=int(r)
			w+=e
	print(w)
	return w




commonlist()

encoder_caesar = {'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j','h':'k','i':'l','j':'m','k':'n','l':'o','m':'p','n':'q','o':'r','p':'s','q':'t','r':'u','s':'v','t':'w','u':'x','v':'y','w':'z','x':'a','y':'b','z':'c'}
def cypher():
	cyphered=""
	normal=input()
	length=len(normal)
	for i in range(length):
		if normal[i] in encoder_caesar:
			a=normal[i]
			cyphered+=encoder_caesar[a]
	print(cyphered)
	return cyphered
cypher()
"""
def posnumber():
	pos=input()
	pos=int(pos)
	if int(pos)>0:
		for i in range(int(pos)):
			if int(pos)%i==0:
				listofdivisors+=i
			if listofdivisors==pos:
				print("perfect number")
				print("divisors are:",listofdivisors)
posnumber()