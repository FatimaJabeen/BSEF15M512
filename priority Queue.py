#!usr/bin/env python

total = 0
priority=[]
processes={}
burst_time=[]
arrival_time=[]
n = input("Enter the number of processes:")

for i in range (0,n):
	prio_no=input("Priority number:")
	priority.append(prio_no)
	a_time=input("Arrival Time:")
	arrival_time.append(a_time)
        b_time=input("Burst Time:")
	burst_time.append(b_time)
	processes[priority[i]] = [i+1 , arrival_time[i] , burst_time[i]]
	print "Priorityno. "\t" Arrival Time "\t" Burst Time"

for i in range (0,n):
	print priority[i] , "\t\t\t" , arrival_time[i], "\t\t\t" , burst_time[i] 
	priority.sort()
	total = processes.get(priority[0])[1]
	min = total
        if(total>0):
	print  total
		 
for i in range (0,n):
	total = total + processes.get(priority[i])[2]
	print min , "\t" , total
	min = total

