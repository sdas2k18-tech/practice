import threading
import time
 
# Shared Memory variables
CAPACITY = 2
buffer = [-1 for i in range(CAPACITY)]
in_index = 0
out_index = 0
 
# Declaring Semaphores
mutex = threading.Semaphore()
empty = threading.Semaphore(CAPACITY)
full = threading.Semaphore(0)
 
# Producer Thread Class
class Producer(threading.Thread):
  def run(self):
     
    global CAPACITY, buffer, in_index, out_index
    global mutex, empty, full
    #print(["inside producer","mutex: "+ str(mutex._value),"empty: " + str(empty._value),"full: " + str(full._value)])

    print(["inside producer",mutex._value,empty._value,full._value])

    items_produced = 0
    counter = 0
     
    while items_produced < 3:
      print(["inside producer",mutex._value,empty._value,full._value])
      empty.acquire()
      print(["inside producer",mutex._value,empty._value,full._value])
      mutex.acquire()
      print(["inside producer",mutex._value,empty._value,full._value])
      
      counter += 1
      buffer[in_index] = counter
      in_index = (in_index + 1)%CAPACITY
      print("Producer produced : ", counter)
       
      print(["inside producer",mutex._value,empty._value,full._value])
      mutex.release()
      print(["inside producer",mutex._value,empty._value,full._value])
      full.release()
      print(["inside producer",mutex._value,empty._value,full._value]) 
      time.sleep(1)
       
      items_produced += 1
 
# Consumer Thread Class
class Consumer(threading.Thread):
  def run(self):
     
    global CAPACITY, buffer, in_index, out_index, counter
    global mutex, empty, full
    print(["inside consumer", mutex._value,empty._value, full._value ])
    items_consumed = 0
     
    while items_consumed < 3:
      print(["inside consumer", mutex._value,empty._value, full._value ])
      full.acquire()
      print(["inside consumer", mutex._value,empty._value, full._value ])
      mutex.acquire()
      print(["inside consumer", mutex._value,empty._value, full._value ])
       
      item = buffer[out_index]
      out_index = (out_index + 1)%CAPACITY
      print("Consumer consumed item : ", item)
       
      print(["inside consumer", mutex._value,empty._value, full._value ])
      mutex.release()
      print(["inside consumer", mutex._value,empty._value, full._value ])
      empty.release()
      print(["inside consumer", mutex._value,empty._value, full._value ])      
       
      time.sleep(2.5)
       
      items_consumed += 1
 
# Creating Threads
producer = Producer()
consumer = Consumer()
 
# Starting Threads
consumer.start()
producer.start()
 
# Waiting for threads to complete
producer.join()
consumer.join()