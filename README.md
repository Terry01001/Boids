# Boids Simulation

## Overview
Boids is a simulation of flocking behavior, which mimics the collective movement of birds, fish, or other animals. In this project, we implement the key principles of Boids: Separation, Alignment, and Cohesion.

## Project Description
This project is part of my learning journey in computer science, where I'm exploring AI concepts and practical coding. Boids provides a fascinating way to understand emergent behavior in a group of simple agents.

## Boid Behaviors
The Boid simulation consists of three main behaviors:

### Separation
Separation ensures that Boids avoid colliding with each other. Each Boid steers away from its nearby neighbors, preventing collisions and maintaining personal space.

### Alignment
Alignment focuses on Boids aligning their velocities with those of their neighbors. This behavior simulates the tendency of animals to match the direction and speed of their group.

### Cohesion
Cohesion encourages Boids to move towards the center of mass of their neighboring Boids. It creates a cohesive force that keeps the group together.

## Usage
To run the Boids simulation, follow these steps:

1. Clone the repository to your local machine.
2. Open the project in your preferred programming environment.
3. Execute the main simulation script.

```python
python Boids.py
