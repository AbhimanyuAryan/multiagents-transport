from spade.behaviour import OneShotBehaviour
from Classes.Bus import Bus
from Utils.Requests import serializeBusStart

class NotifyManagerBusStarted(OneShotBehaviour):
    async def run(self):
        message = serializeBusStart('manager',self.agent.bus, self.agent.bus.route)
        await self.send(message)
