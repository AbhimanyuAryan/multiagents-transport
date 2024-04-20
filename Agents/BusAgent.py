from spade.agent import agent
from Behaviours.BusBehaviour import BusBehaviour

class BusAgent(agent.Agent):
    async def setup(self):
        print(f"Bus agent {self.jid} is starting...")

        # Add behaviors here
        self.add_behaviour(BusBehaviour())
