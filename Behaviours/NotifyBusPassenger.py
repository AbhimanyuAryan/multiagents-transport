from spade.behaviour import OneShotBehaviour
from Classes.Bus import Bus
from Utils.Requests import serializeNotifyBusNewPassenger, serializeNotifyBusPassengerLeft

class NotifyBusPassengerBehaviour(OneShotBehaviour):
    def __init__(self,bus : Bus,passenger_new : bool):
        super().__init__()
        self.bus = bus
        self.passenger_new = passenger_new
    async def run(self):
        receiver = f'bus{self.bus.idBus}'
        if(self.passenger_new):
            msg = serializeNotifyBusNewPassenger(receiver,self.bus)
        else:
            msg = serializeNotifyBusPassengerLeft(receiver,self.bus)
        await self.send(msg)
