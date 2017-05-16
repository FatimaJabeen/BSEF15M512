total=0
process{}		
brust_time=[]
arrival_time=[]
turn_time=1
#functions/methods
def input():
	n =int(raw_input("Enter the number of processes:"))
	for i in range (n):
		priority_no=input("Priority number:")
		priority.append(priority_no)
		a_time=input("Arrival Time')
		arrival_time.append(a_time)
		b_time=input("Burst Time:")
		burst_time.append(b_time)
		processes[priority[i]] = [i+1 , arrival_time[i] , burst_time[i]]
  print ("Priority\tArrival Time\tBurst Time")	
  return;
def print():
  for index in range (n):
	  print "P" , index+1, "             " , process.get(index+1)[0] ,"            " , process.get(index+1)[1]	
  for index in range (0,n+1):
	  duration=process.get(n+1)[1]
	for i in range (0,duration):		
  	remaining= duration-turn_time			
	  arrival_next_process=process.get(n+1)[0]			
	if(turn_time==arrival_next_process):
	if(process.get(n+1)[1]<remaining):				
	  n=n+1					
  	process[n]=[process.get(index+1)[0],remaining,index+1]				
	total=total+turn_time	
	if(turn_time==duration):  	
	  print (total,"P" ,process.get(index+1)[2], "Completed ")
	elif(turn_time!=duration):
		print (total,"P" , process.get(index+1)[2])	
#calling functions/methods		
input()
print()
