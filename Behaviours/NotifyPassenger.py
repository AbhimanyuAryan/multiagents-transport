from spade.behaviour import OneShotBehaviour
from Classes.Passenger import Passenger
from Classes.Bus import Bus
from Utils.Requests import serializeNotifyPassenger

class NotifyPassengerBehaviour(OneShotBehaviour):
    def __init__(self,passenger : Passenger, bus : Bus):
        super().__init__()
        self.passenger = passenger
        self.bus = bus
    async def run(self):
        receiver = str(self.passenger.idPassenger)
        msg = serializeNotifyPassenger(receiver,self.bus)
        await self.send(msg)
        print(f"Passenger {receiver} was notified with a new bus location")
