#FCFS(first come first serve)Scheduling Algorithm(1 sec 1 page)
def FCFS(jobs):
    current_time=0
    total_time=0
    for job in jobs:
        if(current_time<job["arrival_time"]):
            current_time=job["arrival_time"]
        current_time+=job["pages"]
        total_time=current_time
        print(current_time)
        print(total_time)
    return total_time
jobs=[]
for i in range(4):
    dict1={}
    dict1["name"]=input("Enter job name: ")
    dict1["arrival_time"]=int(input("Enter arrival_time: "))
    dict1["pages"]=int(input("Enter pages: "))
    jobs.append(dict1)
print(FCFS(jobs))


#SJF(shortest job first)Scheduling Algorithm
def cal_tot_time(execution_time):
    execution_time1=[]
    execution_time1=execution_time.sort()
    print(execution_time)
    total_time=0
    for i in execution_time:
        total_time+=i
    return total_time
execution_time=[3,5,7,4]
result=cal_tot_time(execution_time)
print(f"The total time required to complete all tasks is: {result} hours")

#Round Robin Scheduling Algorithm
from collections import deque
def calculate_total_time(orders, time_quantum):
    queue =deque(orders)
    print(queue)
    total_time = 0
    while queue:
        current_order = queue.popleft()
        if current_order <= time_quantum:
            total_time += current_order
        else:
            total_time += time_quantum
            queue.append(current_order - time_quantum)
    return total_time
orders = [5, 3, 8, 6]
time_quantum = 4
total_time = calculate_total_time(orders, time_quantum)
print(f"The total time required to complete all orders is: {total_time} minutes")

# Priority Scheduling algorithm
from queue import PriorityQueue
def calculate_total_time(patients):
    pq = PriorityQueue()
    for patient in patients:
        pq.put(patient)
    total_time = 0
    while not pq.empty():
        priority, treatment_time = pq.get()
        total_time += treatment_time
    return total_time
patients = [
    (1, 10),
    (2, 8),
    (3, 15),  
    (4, 5)    
]
total_time = calculate_total_time(patients)
print(f"The total time required to treat all patients is: {total_time} minutes")




