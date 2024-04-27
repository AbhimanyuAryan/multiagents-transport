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

def receiver(server,id):
    random.seed(20)
    route = generateRoute()
    station = random.choice(route.stations[:-1])
    agent = PassengerAgent(f"passenger{id}@{server}","password",Passenger(id,route,None,station))
    # agent.leftBus()
    future = agent.start()
    future.result()
    while agent.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            agent.stop()
            break
    print(f'Agent finished with code {agent.b.exit_code}')
    return 0


if __name__ == '__main__':
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
        receiver(get_server(),id)
    else:
        print('You need to specify an ID for the passenger')
