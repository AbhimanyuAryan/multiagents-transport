from spade.behaviour import OneShotBehaviour
from Classes.Passenger import Passenger
from Classes.Bus import Bus
from Utils.Requests import serializeNotifyBusNewPassenger, serializeNotifyBusPassengerLeft

class NotifyBusPassengerBehaviour(OneShotBehaviour):
    def __init__(self,bus : Bus,passenger_new : bool):
        super().__init__()
        self.bus = bus
        self.passenger_new = passenger_new
    async def run(self):
        receiver = str(self.bus.idBus)
        if(self.passenger_new):
            p = 'entered'
            msg = serializeNotifyBusNewPassenger(receiver,self.bus)
        else:
            p = 'left'
            msg = serializeNotifyBusPassengerLeft(receiver,self.bus)
        await self.send(msg)
        print(f"Bus {receiver} was notified that a passenger has {p}")
