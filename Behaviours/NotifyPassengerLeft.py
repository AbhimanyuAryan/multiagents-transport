from spade.behaviour import OneShotBehaviour
from spade.message import Message
from Classes.Passenger import Passenger
from Utils import Requests

class NotifyPassengerLeftBehaviour(OneShotBehaviour):
    def __init__(self, passenger: Passenger):
        super().__init__()
        self.passenger = passenger

    async def run(self):
        print(f"Notifying passenger {self.passenger.idPassenger} that they have left the bus.")
        # Assuming you have a manager agent to send the notification to the passenger
        msg = Requests.serializePassengerLeft(str(self.passenger.idPassenger), self.passenger, self.agent.bus)
        await self.send(msg)
