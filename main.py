import threading
import time
import os

class Client:
  def __init__(self, name, onworking, done):
    self.name = name
    self.onworking = onworking
    self.done = done

client1 = Client("Paolo", False, False)
client2 = Client("Giovanni", False, False)
client3 = Client("Marco", False, False)
client4 = Client("Piero", False, False)
client5 = Client("Michele", False, False)

clients = [client1, client2, client3, client4, client5]

worker1_free = True
worker2_free = True
clientsPresent = False
settingNewClients = False

def worker1():

  global clients
  global worker1_free
  global worker2_free
  global settingNewClients

  while True:
    if not settingNewClients:
      for x in clients:
        if not x.onworking and not x.done:
          worker1_free = False
          x.onworking = True
          print("\n" + "Worker1 is working: " + x.name)
          time.sleep(2)
          x.done = True
          print("\n" + x.name + " was done by Worker1")

      worker1_free = True
    else:
      while settingNewClients:
        time.sleep(0.5)





def worker2():
  global clients
  global worker1_free
  global worker2_free
  global settingNewClients

  while(worker1_free):      # Worker 2 always waits worker 1 before start to work
      time.sleep(1)

  while True:
    if not settingNewClients:
      for x in clients:
        if not x.onworking and not x.done:
          worker2_free = False
          x.onworking = True
          print("\n" + "Worker2 is working: " + x.name)
          time.sleep(2)
          x.done = True
          print("\n" + x.name + " was done by Worker2")

      worker2_free = True
    else:
      while settingNewClients:
        time.sleep(0.5)

def checkClients_End():

  global clients
  global clientsPresent
  global settingNewClients

  while True:

    if worker1_free and worker2_free:
      clientsPresent = False
      for x in clients:
        if(not x.done):
          clientsPresent = True;

      if not clientsPresent and worker1_free and worker2_free:
        settingNewClients = True
        print("\n**********************")
        print("\nEntering new clients\n")
        print("**********************")
        time.sleep(5)
        for x in clients:
          x.onworking = False
          x.done = False

      print("\n**********************")
      print("\nNew clients!\n")
      print("**********************\n")

      settingNewClients = False

      while worker1_free and worker2_free:
        time.sleep(1)



# Creating three sample threads
worker_1 = threading.Thread(target=worker1)
worker_2 = threading.Thread(target=worker2)
checkClientsEnd = threading.Thread(target=checkClients_End)

# Starting three threads
worker_1.start()
worker_2.start()
checkClientsEnd.start()


