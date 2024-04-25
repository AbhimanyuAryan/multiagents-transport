from spade.behaviour import OneShotBehaviour
from Classes.Passenger import Passenger
from Classes.Manager import Manager
from Utils.Requests import serializeRegisterPassenger

class NotifyPassengerRegisterBehaviour(OneShotBehaviour):
    def __init__(self, passenger : Passenger):
        super().__init__()
        self.passenger = passenger
    async def run(self):
        message = serializeRegisterPassenger("manager",self.passenger)
        await self.send(message)
        print(f"Manager was notified of the registry of passeger {self.passenger.idPassenger}.")