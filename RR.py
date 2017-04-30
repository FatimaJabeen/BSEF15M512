#!usr/bin/env python

process= {}
waiting={}
arrival=[]
burst=[]
itera= input(" How many processes you want to enter : " )
quantum_t= input (" Enter quantum time for RR: ")

for i in range (0,itera):
	num=input("Enter arrival time of the process")
	if(i==0):
		min=num	
	elif(min>num):
		min=num	
	arrival.append(num)
	num1=input("Enter CPU time of the process")
	burst.append(num1)
	process[i+1]=[arrival[i],burst[i]]

print "A.T"  ,"   " , "B.T"
for index in range (1,itera+1):
	print process.get(index)[0] ,"       " , process.get(index)[1]	
total=min
if(total>0):
	print total, "idle time"
count=0
index=1
a=itera+1
while(count!=itera):
	rem=(process.get(index)[1])- quantum_t
	if(rem<0):
		total=total+process.get(index)[1]
		print min, "\t",total
		count=count+1
	if(rem==0):
		total=total+quantum_t
		print min, "\t",total
		count=count+1
	if(rem > 0):
		total=total+quantum_t
		print min, "\t",total
	if(process.get(index)[1]>quantum_t):
		process[a]=[process.get(index)[0],rem]
		a=a+1
	min=total
	index=index+1
