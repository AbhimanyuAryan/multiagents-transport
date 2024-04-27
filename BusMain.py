from Agents.BusAgent import BusAgent
import time
from Utils.MessageBuilder import get_server
import sys
from Classes.Bus import Bus


def receiver(server,id):
    agent = BusAgent(f"bus{id}@{server}","password", Bus(id,50,None,None))
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
