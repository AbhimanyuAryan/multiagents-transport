from Agents.ManagerAgent import ManagerAgent
import time
import pygame
from pygame.locals import *
import time
from Utils.MessageBuilder import get_server
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bus and Passenger Visualization")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Function to draw buses
def draw_buses(buses):
    for bus_id, bus in buses.items():
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        pygame.draw.circle(screen, RED, (x,y), 10)

# Function to draw passengers
def draw_passengers(passengers):
    for passenger_id, passenger in passengers.items():
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        pygame.draw.circle(screen, BLUE, (x,y), 5)

# Function to get data from ManagerAgent
def get_data_from_agent(agent):
    # Get buses and passengers data from the agent
    buses = agent.manager.buses
    passengers = agent.manager.passengers
    return buses, passengers

# Main function to run the simulation and visualization
def main(server):
    # Create the manager agent
    agent = ManagerAgent(f"manager@{server}","password")
    future = agent.start()
    future.result()

    # Simulation and visualization loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Clear the screen
        screen.fill(WHITE)

        # Get buses and passengers data from the agent
        buses, passengers = get_data_from_agent(agent)

        # Draw buses
        draw_buses(buses)

        # Draw passengers
        draw_passengers(passengers)

        # Update the display
        pygame.display.flip()

        # Allow agent to continue running
        time.sleep(1)

    # Stop the agent when simulation ends
    agent.stop()
    print(f'Agent finished with code {agent.b.exit_code}')
    pygame.quit()

if __name__ == '__main__':
    main(get_server())



# from Agents.ManagerAgent import ManagerAgent
# import time
# from Utils.MessageBuilder import get_server
# import random

# def receiver(server):
#     agent = ManagerAgent(f"manager@{server}","password")
#     future = agent.start()
#     future.result()
#     while agent.is_alive():
#         try:
#             time.sleep(1)
#         except KeyboardInterrupt:
#             agent.stop()
#             break
#     print(f'Agent finished with code {agent.b.exit_code}')
#     return 0


# if __name__ == '__main__':
#     receiver(get_server())
