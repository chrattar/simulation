import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Screen setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ball in Circle")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Circle properties
circle_radius = 200
circle_center = (screen_width // 2, screen_height // 2)

# Ball properties
ball_radius = 10
ball_position = np.array([circle_center[0], circle_center[1] - circle_radius + ball_radius], dtype=float)
initial_velocity_x = 2.0  # Initial x component
initial_velocity_y = 0.0  # Initial y component
ball_velocity = np.array([initial_velocity_x, initial_velocity_y], dtype=float)

# Constants
gravity = np.array([0, 9.81], dtype=float)
dt = 0.05  # Time step

def update_position(ball_position, ball_velocity, dt):
    ball_velocity += gravity * dt
    ball_position += ball_velocity * dt
    return ball_position, ball_velocity

def handle_collisions(ball_position, ball_velocity, circle_center, circle_radius, ball_radius):
    distance_from_center = np.linalg.norm(ball_position - np.array(circle_center))
    if distance_from_center + ball_radius > circle_radius:
        normal = (ball_position - np.array(circle_center)) / distance_from_center  # Normal vector at the collision point
        ball_velocity = ball_velocity - 2 * np.dot(ball_velocity, normal) * normal  # Reflect the velocity
        # Correct the position to be on the boundary
        ball_position = np.array(circle_center) + normal * (circle_radius - ball_radius)
    return ball_position, ball_velocity

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update ball position and velocity
    ball_position, ball_velocity = update_position(ball_position, ball_velocity, dt)
    ball_position, ball_velocity = handle_collisions(ball_position, ball_velocity, circle_center, circle_radius, ball_radius)

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, circle_center, circle_radius, 1)
    pygame.draw.circle(screen, BLUE, (int(ball_position[0]), int(ball_position[1])), ball_radius)
    pygame.display.flip()
    clock.tick(120)

pygame.quit()
