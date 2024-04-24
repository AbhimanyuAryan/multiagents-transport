from spade.behaviour import CyclicBehaviour
from spade.message import Message

class PassengerBehaviour(CyclicBehaviour):
    async def run(self):
        print("Passenger agent started.")
        while True:
            msg = await self.receive(timeout=10)
            if msg:
                await self.agent.recievedMessage(msg)

