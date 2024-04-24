from spade.behaviour import OneShotBehaviour
from Classes.Passenger import Passenger
from Classes.Bus import Bus
from Utils.Requests import serializePassengerLeft

class LeftBusBehaviour(OneShotBehaviour):
    def __init__(self,passenger : Passenger, bus : Bus):
        super().__init__()
        self.passenger = passenger
        self.bus = bus
    async def run(self):
        sender = str(self.passenger.idPassenger)
        msg = serializePassengerLeft("manager",self.passenger,self.bus)
        await self.send(msg)
        print(f"Passenger {sender} notified manager of their intent to leave a bus.")
