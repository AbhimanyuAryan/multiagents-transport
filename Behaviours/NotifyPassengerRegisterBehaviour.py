from spade.behaviour import OneShotBehaviour
from Classes.Passenger import Passenger
from Utils.Requests import serializeRegisterPassenger

class NotifyPassengerRegisterBehaviour(OneShotBehaviour):
    def __init__(self, passenger : Passenger):
        super().__init__()
        self.passenger = passenger
    async def run(self):
        message = serializeRegisterPassenger("manager",self.passenger)
        await self.send(message)