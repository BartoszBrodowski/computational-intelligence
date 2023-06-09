import pygame
from pygame.locals import *
from Box2D import *

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

# Create the Box2D world
world = b2World(gravity=(0, -10), doSleep=True)

# Create the ground body
ground_body = world.CreateStaticBody(
    position=(0, -10),
    shapes=b2PolygonShape(box=(50, 10)),
)

# Create a dynamic body
dynamic_body = world.CreateDynamicBody(position=(0, 20))
dynamic_body.CreatePolygonFixture(box=(1, 1), density=1, friction=0.3)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Step the simulation
    time_step = 1.0 / 60.0
    vel_iters, pos_iters = 6, 2
    world.Step(time_step, vel_iters, pos_iters)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the ground
    for fixture in ground_body.fixtures:
        vertices = [(ground_body.transform * v) * 10 for v in fixture.shape.vertices]
        vertices = [(v[0], 600 - v[1]) for v in vertices]
        pygame.draw.polygon(screen, (0, 0, 0), vertices)

    # Draw the dynamic body
