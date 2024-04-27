from spade.behaviour import OneShotBehaviour
from Classes.Route import Route
from Classes.Bus import Bus
from Utils.Requests import serializeNotifyBusRoute

class NotifyBusRouteBehaviour(OneShotBehaviour):
    def __init__(self,bus : Bus, route : Route):
        super().__init__()
        self.bus = bus
        self.route = route
    async def run(self):
        receiver = f'bus{self.bus.idBus}'
        msg = serializeNotifyBusRoute(receiver,self.route)
        await self.send(msg)