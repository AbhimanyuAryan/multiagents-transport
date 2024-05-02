from Agents.ManagerAgent import ManagerAgent
import time
import pygame
from pygame.locals import *
import time
from Utils.MessageBuilder import get_server
import random
import os

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

bus_image = pygame.image.load(os.path.join("assets", "bus", "bus.png"))
bus_image = pygame.transform.scale(bus_image, (50, 20))  # Adjust size as needed

pagsenger_image = pygame.image.load(os.path.join("assets", "passenger", "passenger.png"))
pagsenger_image = pygame.transform.scale(pagsenger_image, (20, 20))  # Adjust size as needed

station_positions = []

def initialize_station_positions(station_count):
    global station_positions
    if not station_positions:
        station_positions = [random.randint(110, screen_width - 110) for _ in range(station_count)]
        station_positions.sort()
        offset = 50
        for i in range(1, len(station_positions)):
            if station_positions[i] - station_positions[i-1] < offset:
                station_positions[i] = station_positions[i-1] + offset

def draw_route_stations_passengers(stations, passengers):
    pygame.draw.line(screen, BLUE, (0, 300), (800, 300), 5)

    keys_list = list(stations.keys())
    values_list = list(stations.values())

    for station_x in values_list:
        pygame.draw.circle(screen, BLACK, (station_x, 300), 10)

    #TODO: draw passengers
    for passenger in passengers:
        print(f"\033[1;32;40m{passenger.initialStation}\033[m")

    font = pygame.font.Font(None, 36)
    text = font.render("Linha 45", 1, BLACK)
    screen.blit(text, (350, 250))

def draw_buses(buses):
    start_y = 300
    distance_between_buses = 50
    x = screen_width - 30

    for i in range(len(buses)):
        y = start_y + i * distance_between_buses
        screen.blit(bus_image, (x, y))

#FIXME: Remove this logic later as it is moved to draw_route_stations_passengers
# def draw_passengers(passengers):
#     for passenger_id, passenger in passengers.items():
#         x = random.randint(0, screen_width)
#         y = random.randint(0, screen_height)
#         screen.blit(pagsenger_image, (x, y))

def get_data_from_agent(agent):
    # Get route, buses and passengers data from the agent
    station_ids = [station.idStation for station in agent.manager.routes[1].stations]
    
    global station_positions
    station_count = len(station_ids)

    initialize_station_positions(station_count)

    stations = dict(zip(station_ids, station_positions))
    
    buses = agent.manager.buses
    passengers = agent.manager.passengers
    return stations, buses, passengers

def draw_ui(passenger_count, bus_count):
    box_size = 100
    margin = 10
    box_x = screen_width - box_size - margin
    box_y = margin
    pygame.draw.rect(screen, BLACK, (box_x, box_y, box_size, box_size), 2)

    font = pygame.font.Font(None, 24)
    text_passenger = font.render(f"P: {passenger_count}", True, BLACK)
    text_bus = font.render(f"B: {bus_count}", True, BLACK)
    screen.blit(text_passenger, (box_x + margin, box_y + margin))
    screen.blit(text_bus, (box_x + margin, box_y + margin + 30))
    
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

        stations, buses, passengers = get_data_from_agent(agent)

        draw_buses(buses)
        draw_route_stations_passengers(stations, passengers)
        draw_ui(len(passengers), len(buses))

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