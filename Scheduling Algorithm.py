import random
import sys
import matplotlib.pyplot as plt

#โค้ดมันจะชอบรัว ถ้าโค้ดเกิดอาการรันเรื่อยให้หยุดแล้ว รันใหม่ (often found when run RR algorithm)

process_List = []
process_List2 = []
process_List3 = []
wait_process = []
wait_process2 = []

bus_time = []
bus_time2 = []
burst_time3 = []
map_process2 = {}


def process1():
    for i in range(1, 43):  # 70% of total
        bus_time.append(random.randint(2, 8))
        process_List.append(i)
    for i in range(43, 55):  # 20% of total
        bus_time.append(random.randint(20, 30))
        process_List.append(i)
    for i in range(55, 61):  # 10% of total
        bus_time.append(random.randint(35, 40))
        process_List.append(i)
    random.shuffle(bus_time)  # random bus_time
    random.shuffle(process_List)  # random process
    return process_List, bus_time


def process2():
    for i in range(1, 21):  # 50% of total
        bus_time2.append(random.randint(2, 8))
        process_List2.append(i)
    for i in range(21, 33):  # 30% of total
        bus_time2.append(random.randint(20, 30))
        process_List2.append(i)
    for i in range(33, 41):  # 20% of total
        bus_time2.append(random.randint(35, 40))
        process_List2.append(i)
    random.shuffle(bus_time2)  # random bus time
    random.shuffle(process_List2)  # random process
    for i in range(0, 40):
        map_process2[process_List2[i]] = bus_time2[i]
    return map_process2


def process3():
    for i in range(1, 9):  # 40% of total
        burst_time3.append(random.randint(2, 8))
        process_List3.append(i)
    for i in range(9, 17):
        burst_time3.append(random.randint(20, 30))
        process_List3.append(i)
    for i in range(17, 21):
        burst_time3.append(random.randint(35, 40))
        process_List3.append(i)
    random.shuffle(burst_time3)  # random bus time
    random.shuffle(process_List3)  # random process
    return burst_time3, process_List3


def FCFS():
    waiting_time = 0
    count = 0
    x = []
    y = []
    total = 0
    process1()
    for i in range(0, 61):
        x.append(0)
        y.append(0)
    print(len(y))
    x[process_List[0]] = process_List[0]
    y[process_List[0]] = 0
    sys.stdout.write("{0}:{1}  ".format(x[process_List[0]], y[process_List[0]]))
    for i in range(1, 60):
        waiting_time += bus_time[i]
        y[process_List[i]] = waiting_time
        x[process_List[i]] = process_List[i]

        sys.stdout.write("{0}:{1}  ".format(x[process_List[i]], y[process_List[i]]))
    print()
    # plotting the points
    plt.plot(x, y, 'ro')

    # naming the x axis
    plt.xlabel('Process')
    # naming the y axis
    plt.ylabel('waiting_time')

    # giving a title to my graph
    plt.title('FCFS')

    # function to show the plot
    plt.show()


def SJF():
    map_sorted = {}
    x = []
    y = []
    list_sorted = {}
    list_value = {}
    sum = 0
    wait_time = []
    wait_time.append(0)
    for key, value in sorted(process2().items(), key=lambda item: item[1]):
        map_sorted[key] = value
    print(map_sorted)
    for x in map_sorted.values():
        sum = sum + x
        wait_time.append(sum)
    print(wait_time)


def RR():
    process3()
    sum = 0
    request_queue = []
    print(process_List3)
    print(burst_time3)
    for i in range(0, len(burst_time3)):
        sum += burst_time3[i]
    #print(sum)
    avg = sum / len(burst_time3)
    time_quantum = int(avg)
    #print(time_quantum)

    i = 0
    while sum > 0:
        if burst_time3[i] > 0:
            if (burst_time3[i] > time_quantum):
                request_queue.append(process_List3[i])
                sum -= time_quantum
                burst_time3[i] -= time_quantum
            elif (burst_time3[i] < time_quantum):
                request_queue.append(process_List3[i])
                sum -= burst_time3[i]
                burst_time3[i] = 0
        elif (burst_time3[i] == 0):
            print("go to next process")

        if sum ==0:  # stop when sum = 0
            break

        if(i<19):
            i += 1
        else:
            i=0

    return request_queue


print(RR())
