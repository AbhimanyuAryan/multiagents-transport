from Agents.PassengerAgent import PassengerAgent
import time
from Utils.MessageBuilder import get_server
from Classes.Route import Route, generateRoute
from Classes.Station import Station
from Classes.Passenger import Passenger
from Classes.Bus import Bus
import sys
import random
import time
import threading

def exec_passenger(agent):
    while agent.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            agent.stop()
            break
    print(f'Passenger {agent.passenger.idPassenger} finished')
    return 0

def createPassengers(numberPassengers):
    threadlist = []
    for id in range(numberPassengers):
        route = generateRoute()
        station = random.choice(route.stations[3:-1])
        agent = PassengerAgent(f"passenger{id}@{get_server()}","password",Passenger(id,route,None,station))
        future = agent.start()
        future.result()
        thread = threading.Thread(target=lambda: exec_passenger(agent))
        thread.start()
        threadlist.append(thread)
    for t in threadlist:
        t.join()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        numberPassengers = int(sys.argv[1])
        createPassengers(numberPassengers)
    else:
        print('You need to specify the number of passenger')
