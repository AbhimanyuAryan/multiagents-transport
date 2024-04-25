from spade.behaviour import OneShotBehaviour
from Classes.Bus import Bus
from Utils.Requests import serializeBusNewLocation

class CurrentBusLocationUpdate(OneShotBehaviour):
    async def run(self):
        message = serializeBusNewLocation('manager',self.agent.bus)
        await self.send(message)