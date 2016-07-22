 #-*- coding: utf-8 -*-
class HousePark:
	lastname ="박"
	def __init__(self,name):
		self.fullname=self.lastname + name
	def setname(self,name):
		self.fullname = self.lastname + name
	def travel(self,where):
		print("%s, %s여행을 떠나다!" %(self.fullname,where))
	def love(self,other):
		print("%s, %s 사랑에 빠지다!" %(self.fullname, other.fullname))
	def fight(self,other):
		print("%s, %s... 사랑과전쟁이 시작되다!!" %(self.fullname, other.fullname))
	def __add__(self, other):
		print("%s, %s 결혼했네?" %(self.fullname, other.fullname))
	def __sub__(self,other):
		print("%s, %s 이혼했데!!!"%(self.fullname, other.fullname))
class HouseKim(HousePark):
	lastname="김"
	def travel(self,where,day):
		print("%s, %s여행을 %s동안 떠나다!!" % (self.fullname,where,day))

