from Agents.BusAgent import BusAgent
import time
from Utils.MessageBuilder import get_server
import sys
from Classes.Bus import Bus
import threading


def exec_bus(agent):
    while agent.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            agent.stop()
            break
    print(f'Agent finished with code {agent.b.exit_code}')
    return 0

def createBuses(numberBuses):
    threadlist = []
    for id in range(numberBuses):
        agent = BusAgent(f"bus{id}@{get_server()}","password", Bus(id,50,None,None))
        future = agent.start()
        future.result()
        thread = threading.Thread(target=lambda: exec_bus(agent))
        thread.start()
        threadlist.append(thread)
    for t in threadlist:
        t.join()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        numberBuses = int(sys.argv[1])
        createBuses(numberBuses)
    else:
        print('You need to specify the number of buses')
