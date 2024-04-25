from spade.behaviour import CyclicBehaviour

class ManagerBehaviour(CyclicBehaviour):
    async def run(self):
        print("Manager Cycle Behaviour up")
        while True:
            msg = await self.receive(timeout=10)
            if msg:
                await self.agent.receivedMessage(msg)