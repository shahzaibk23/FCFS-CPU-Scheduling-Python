# Write your processes here, in this dictionary format.
jobQueue = [
    {
        "Process":"P1",
        "BurstTime": 24,
        "ArrivalTime":0
    },
    {
        "Process":"P2",
        "BurstTime": 3,
        "ArrivalTime":0
    },
    {
        "Process":"P3",
        "BurstTime": 3,
        "ArrivalTime":0
    },

]

print("Job Queue initially")
for i in jobQueue:
    print(i)

readyQueue = []
waitingQueue = []

CPU_process_record = []

time = 0

while jobQueue != [] or readyQueue != [] or waitingQueue != []:
    lstOfDeletion = []
    for j, i in enumerate(jobQueue):

        if i["ArrivalTime"] <= time:

            readyQueue.append(i)
            lstOfDeletion.append(i)

    for i in lstOfDeletion:
        jobQueue.remove(i)

    lstOfDeletion = []

    for j in readyQueue:
        lstOfDeletion.append(j)
        startTime = time
        time += j["BurstTime"]
        CPU_process_record.append({"Process":j["Process"], "StartTime":startTime, "EndTime":time})
    for j in lstOfDeletion:
        readyQueue.remove(j)

print("\n \nFirst Come First Serve ")
SumOfStartTime = 0
for i in CPU_process_record:
    print(i)
    SumOfStartTime += i["StartTime"]

AvgTime = SumOfStartTime/len(CPU_process_record)
print("Average Time: ",AvgTime," Units")
