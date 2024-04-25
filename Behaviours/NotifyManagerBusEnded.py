from spade.behaviour import OneShotBehaviour
from Classes.Bus import Bus
from Utils.Requests import serializeBusEnd

class NotifyManagerBusEnd(OneShotBehaviour):
    async def run(self):
        message = serializeBusEnd('manager',self.agent.bus, self.agent.bus.route)
        await self.send(message)
