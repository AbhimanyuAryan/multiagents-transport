# Diagrams

This directory contains pictures of all the diagrams we made. Links to the diagrams can be accessed in the README.md at the root of the project.

In these diagrams, we color-coded elements according to the part of the system, which may or may not be an agent, in the following manner:

- Blue: Bus Agent
- Yellow: Manager Agent
- Green: Passenger Agent
- Red: Auxiliary classes

## Class Diagram

As the name suggests, this diagram showcases the classes and structures of our code. As we can see, we created classes to represent the three agent types (Bus, Passenger, and Manager), but we also have auxiliary classes that represent attributes of the agents in a structured manner.

We also have classes that are not represented on the diagram as they serve very specific generic purposes, such as helping build messages or defining performatives. There are also classes that represent the behaviors our agents act upon, but we chose not to include them because we have too many behaviors that would make the diagram overly complex.

## Sequence Diagram

The sequence diagram illustrates how the agents in the system interact with each other over time.

Arrows connecting the lifelines denote the performative utilized.

The system begins with agents initializing and registering on the manager. Subsequently, buses commence their routes, while passengers check if the bus has reached their station.

Buses then iterate over the stations of their route until completion. Passengers disembark either upon arrival at their station or when the bus completes its route.

## Activity Diagram

The activity diagram serves a similar purpose to the sequence diagram, illustrating the various steps involved in the interaction between agents in our program.

Since the diagram is self-explanatory, we'll refrain from describing it in depth, as the explanation of the steps mirrors the one provided earlier. We'll mention that this diagram does not display the performatives utilized.