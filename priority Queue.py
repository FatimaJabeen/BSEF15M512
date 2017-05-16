total = 0
priority=[]
processes={}
burst_time=[]
arrival_time=[]
#function for input
def input():
	n = int(input("Enter the number of processes:"))
	for i in range (n):
		priority_no=int(input("Priority number:"))
		priority.append(priority_no)
		a_time=int(input("Arrival Time:"))
		arrival_time.append(a_time)
        	b_time=int(input("Burst Time:"))
		burst_time.append(b_time)
		return;
#function for printing the table
def print():
	processes[priority[i]] = [i+1 , arrival_time[i] , burst_time[i]]
	print "Priorityno\tArrival Time\t Burst Time"
	for i in range (n):
		print priority[i] , "\t\t" , arrival_time[i], "\t\t" , burst_time[i] 
	priority.sort()
	total = processes.get(priority[0])[1]
	return;
#function for print result
def Result():	
	for i in range (n):
	total = total + processes.get(priority[i])[2]
	print  total
	return;
#calling fuctions/methods
input()
print()
Result()
