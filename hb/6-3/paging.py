#paging.py
#-*-coding: utf-8-*-

def getTotalPage(m,n):
	total=1
	nPage=0
	total+=int(m/n)
	nPage=m%n
	if nPage == 0:
		total -=1
	print("총 게시물은 %s 개, 총페이지는 %s 페이지, 마지막페이지 게시물은 %s개입니다."%(m,total,nPage))
	return 
