 #-*- coding: utf-8 -*-
class Service:
	secret="영구 배꼽은 2개"
	def __init__(self,name):
		self.name=name
	def sum(self,a,b):
		result=a+b
		print("%s님, %s + %s = %s 입니다." % (self.name,a,b,result))
