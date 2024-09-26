#Multi-Level Queue Scheduling
#2.1--Managing System and user processes
from queue import Queue
def calculate_total_time(system_processes,user_processes):
    pq=Queue()
    for process,time in system_processes.items():
        pq.put((process,time))
    for process,time in user_processes.items():
        pq.put((process,time))
    total_time=0
    while not pq.empty():
        process,time=pq.get()
        total_time+=time
    return total_time
system_processes={'process A':5,'process B':3,'process C':7}
user_processes={'process D':4,'process E':2,'process F':6}
total_time=calculate_total_time(system_processes,user_processes)
print(f"The total time required to complete all processes is:{total_time} units")

#2.2--Managing Job Scheduling in a computer center
from queue import Queue
def calculate_total_time(high_priority_jobs,low_priority_jobs):
    pq=Queue()
    for prior,time in high_priority_jobs.items():
        pq.put((prior,time))
    for prior,time in low_priority_jobs.items():
        pq.put((prior,time))
    total_time=0
    while not pq.empty():
        prior,time=pq.get()
        total_time+=time
    return total_time
high_priority_jobs={'Job A':8,'Job B':5,'Job C':10}
low_priority_jobs={'Job D':6,'Job E':3,'Job F':7}
total_time=calculate_total_time(high_priority_jobs,low_priority_jobs)
print(f"The total time required to complete all jobs is:{total_time} units")

#2.3--Managing print jobs in a shared printing environment
from queue import Queue
def calculate_total_time(high_priority_jobs,low_priority_jobs):
    pq=Queue()
    for prior,time in high_priority_jobs.items():
        pq.put((prior,time))
    for prior,time in low_priority_jobs.items():
        pq.put((prior,time))
    total_time=0
    while not pq.empty():
        prior,time=pq.get()
        total_time+=time
    return total_time
high_priority_jobs={'Job A':15,'Job B':10,'Job C':20}
low_priority_jobs={'Job D':5,'Job E':8,'Job F':3}
total_time=calculate_total_time(high_priority_jobs,low_priority_jobs)
print(f"The total time required to complete all jobs is:{total_time} units")

#2.4--Task Schedulling in a Multi-User System
from queue import Queue
def calculate_total_time(high_priority_task,low_priority_task):
    pq=Queue()
    for task,time in high_priority_task.items():
        pq.put((task,time))
    for task,time in low_priority_task.items():
        pq.put((task,time))
    total_time=0
    while not pq.empty():
        task,time=pq.get()
        total_time+=time
    return total_time
high_priority_task={'task A':12,'task B':8,'task C':15}
low_priority_task={'task D':6,'task E':4,'task F':10}
total_time=calculate_total_time(high_priority_task,low_priority_task)
print(f"The total time required to complete all tasks is:{total_time} units")

#2.5--Jobs Sceduling in a Computer Cluster
from queue import Queue
def calculate_total_time(high_priority_jobs,medium_priority_jobs,low_priority_jobs):
    pq=Queue()
    for prior,time in high_priority_jobs.items():
        pq.put((prior,time))
    for prior,time in medium_priority_jobs.items():
        pq.put((prior,time))
    for prior,time in low_priority_jobs.items():
        pq.put((prior,time))
    total_time=0
    while not pq.empty():
        prior,time=pq.get()
        total_time+=time
    return total_time
high_priority_jobs={'Job A':20,'Job B':15,'Job C':25}
medium_priority_jobs={'Job D':10,'Job E':12,'Job F':8}
low_priority_jobs={'Job G':5,'Job H':4,'Job I':6}
total_time=calculate_total_time(high_priority_jobs,medium_priority_jobs,low_priority_jobs)
print(f"The total time required to complete all jobs is:{total_time} units")
