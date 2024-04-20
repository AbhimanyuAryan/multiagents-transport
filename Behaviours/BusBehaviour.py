from spade.behaviour import OneShotBehaviour
from spade.message import Message

class BusBehaviour(OneShotBehaviour):
    async def run(self):
        print(f"{self.agent.jid}: Bus behavior is running!")

        # Example: Sending a message to the manager
        msg = Message(to="manager@localhost")  # Assuming the manager's JID is "manager@localhost"
        msg.body = "Hello from the bus!"
        await self.send(msg)
