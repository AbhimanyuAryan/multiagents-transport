from Agents.PassengerAgent import PassengerAgent
import time
from Utils import Requests
from Classes.Route import Route
from Classes.Station import Station
from Classes.Passenger import Passenger
import sys
import random

def receiver(server,id):
    route = Route(1,[Station(0,11.458813384984436,3.387561742511398), Station(1,8.230461240819134,19.876760255546593), Station(2,2.0649559982235988,6.382782976985794), Station(3,19.000782159070006,8.988015117046508), Station(4,4.173051446648859,6.338079664911859), Station(5,18.172716897922253,6.711376209369478), Station(6,8.547435863722008,12.553676741994856), Station(7,16.111701405293296,9.842271716137676), Station(8,1.6293196687613865,11.464198863900062), Station(9,0.7019430699670526,1.89049945529572), Station(10,3.8067508121464977,13.868764454786515), Station(11,5.669448421159899,13.804996200916598), Station(12,3.266988936656272,2.353937760843001), Station(13,0.4668945472766972,14.115674232536502), Station(14,17.182252830440667,4.393312271525129), Station(15,4.7513873958606245,0.25960174189042284), Station(16,12.897168936978682,6.014921557813597), Station(17,2.73744608384074,12.937471171596325), Station(18,11.994671035005638,8.94777102865348), Station(19,3.060265767936443,12.773413251907023)])
    station = random.choice(route.stations)
    agent = PassengerAgent(f"passenger{id}@{server}","password",Passenger(id,route,None,station))
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
        print(id)
        receiver(Requests.get_server(),id)
    else:
        print('You need to specify an ID for the passenger')
