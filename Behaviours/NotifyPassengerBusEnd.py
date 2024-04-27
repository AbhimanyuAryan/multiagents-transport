from spade.behaviour import OneShotBehaviour
from Classes.Passenger import Passenger
from Classes.Bus import Bus
from Utils.Requests import serializeNotifyPassengerBusEnd

class NotifyPassengerBusEndBehaviour(OneShotBehaviour):
    def __init__(self,passenger : Passenger, bus : Bus):
        super().__init__()
        self.passenger = passenger
        self.bus = bus
    async def run(self):
        receiver = f'passenger{self.passenger.idPassenger}'
        msg = serializeNotifyPassengerBusEnd(receiver,self.bus)
        await self.send(msg)
        print(f"Passenger {receiver} was notified with a that the {self.bus} has finished")
