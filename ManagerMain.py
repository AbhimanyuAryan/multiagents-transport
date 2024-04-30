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

station_positions = []

def draw_route(station_count):
    pygame.draw.line(screen, BLUE, (0, 300), (800, 300), 5)

    for i, station_x in enumerate(station_positions):
        pygame.draw.circle(screen, BLACK, (station_x, 300), 10)

    font = pygame.font.Font(None, 36)
    text = font.render("Route 55", 1, BLACK)
    screen.blit(text, (350, 250))

def draw_buses(buses):
    for bus_id, bus in buses.items():
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        pygame.draw.circle(screen, RED, (x,y), 10)

def draw_passengers(passengers):
    for passenger_id, passenger in passengers.items():
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        pygame.draw.circle(screen, BLUE, (x,y), 5)

def get_data_from_agent(agent):
    # Get route, buses and passengers data from the agent
    station_count = len(agent.manager.routes[1].stations)
    
    global station_positions
    if len(station_positions) != station_count:
        station_positions = [random.randint(110, screen_width - 110) for _ in range(station_count)]
    
    print(f"\033[1;32;40m{station_positions}\033[m")

    buses = agent.manager.buses
    passengers = agent.manager.passengers
    return station_count, buses, passengers
    
def main(server):
    agent = ManagerAgent(f"manager@{server}","password")
    future = agent.start()
    future.result()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Clear the screen
        screen.fill(WHITE)

        station_count, buses, passengers = get_data_from_agent(agent)

        draw_buses(buses)
        draw_passengers(passengers)
        draw_route(station_count)

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