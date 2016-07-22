#mulsum.py
def mulsum(n):
	i=1
	sum=0
	while i < n:
		if i%3 == 0:
			sum+=i
		if i%5 ==0:
			sum+=i
		if i%15==0:
			sum-=i
		i+=1
	print(sum)
			
