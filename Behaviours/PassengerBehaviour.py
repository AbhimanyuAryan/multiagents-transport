from spade.behaviour import CyclicBehaviour
from Utils.Requests import serializeRegisterPassenger

class PassengerBehaviour(CyclicBehaviour):
    async def run(self):
        print(f"Passenger {self.agent.passenger.idPassenger}: Passenger Cycle Behaviour up")
        message = serializeRegisterPassenger('manager',self.agent.passenger)
        await self.send(message)
        while True:
            msg = await self.receive(timeout=10)
            if msg:
                await self.agent.receivedMessage(msg)

