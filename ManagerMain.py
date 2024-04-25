from Agents.ManagerAgent import ManagerAgent
import time
from Utils import Requests
import random

def receiver(server):
    random.seed(20)
    agent = ManagerAgent(f"manager@{server}","password")
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
    receiver(Requests.get_server())
