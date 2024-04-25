from spade.behaviour import CyclicBehaviour
from spade.message import Message

from Utils.Requests import serializeRegisterBus

class BusBehaviour(CyclicBehaviour):
    async def run(self):
        print("Bus Cycle Behaviour up")
        message = serializeRegisterBus('manager',self.agent.bus)
        await self.send(message)
        while True:
            msg = await self.receive(timeout=10)
            if msg:
                await self.agent.receivedMessage(msg)