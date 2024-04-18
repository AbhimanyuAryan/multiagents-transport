import time
from spade import quit_spade

from Agents.manager import ManagerAgent
from Agents.bus import BusAgent
from Agents.passenger import PassengerAgent

XMPP_SERVER = 'localhost'  # Put your XMPP_SERVER
PASSWORD = 'NOPASSWORD'  # Put your password

if __name__ == '__main__':
    manager_jid = 'manager@' + XMPP_SERVER
    bus_jid = 'bus@' + XMPP_SERVER
    passenger_jid = 'passenger@' + XMPP_SERVER

    manager_agent = ManagerAgent(manager_jid, PASSWORD)
    bus_agent = BusAgent(bus_jid, PASSWORD)
    passenger_agent = PassengerAgent(passenger_jid, PASSWORD)


    # Start the agents
    res_manager = manager_agent.start()
    res_manager.result()  # Verify if Manager agent is active

    res_bus = bus_agent.start()
    res_bus.result()  # Verify if Bus agent is active

    res_passenger = passenger_agent.start()
    res_passenger.result()  # Verify if Passenger agent is active

    # Optionally, start any auxiliary services or behaviors (if needed)
    # For example, if the bus agent provides a web interface, you can start it here.

    # Main loop to keep the program running until interrupted
    while manager_agent.is_alive() and bus_agent.is_alive() and passenger_agent.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            manager_agent.stop()
            bus_agent.stop()
            passenger_agent.stop()
            break

    print('Agents finished')

    # Finish all agents and behaviors running in your process
    quit_spade()
