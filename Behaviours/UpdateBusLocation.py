from spade.behaviour import PeriodicBehaviour

class UpdateBusLocation(PeriodicBehaviour):
    async def run(self):
        if not self.agent.updateLocation():
            self.kill()
