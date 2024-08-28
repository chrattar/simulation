import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy as sp

# Constants
circle_radius = 10
circle_center = (0, 0)
gravity = np.array([0, -9.81], dtype=float)
mass = 1.0
k = 0.1  # Drag Coefficient
dt = 0.05  # Time step

ball_radius = 0.5
ball_position = np.array([0, circle_radius - ball_radius], dtype=float)  # Start at the top of the circle

# Initial Velocity
initial_velocity_x = 2.0  # Initial x-component of velocity
initial_velocity_y = -5.0  # Initial y-component of velocity

# Initialize the velocity vector
ball_velocity = np.array([initial_velocity_x, initial_velocity_y], dtype=float)

def update_position(ball_position, ball_velocity, dt):
    # Calculate the drag force
    drag_force = (k/mass) * ball_velocity
    
    # Update velocity with gravity and drag force
    ball_velocity += (gravity - drag_force) * dt
    
    # Update position with velocity
    ball_position += ball_velocity * dt

    return ball_position, ball_velocity

def handle_collisions(ball_position, ball_velocity, circle_radius, ball_radius):
    distance_from_center = np.linalg.norm(ball_position)
    
    if distance_from_center + ball_radius > circle_radius:
        normal = ball_position / distance_from_center  # Normal vector at the collision point
        ball_velocity = ball_velocity - 2 * np.dot(ball_velocity, normal) * normal  # Reflect the velocity

        # Correct the position to be on the boundary
        ball_position = normal * (circle_radius - ball_radius)
    
    return ball_position, ball_velocity

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-circle_radius, circle_radius)
ax.set_ylim(-circle_radius, circle_radius)

circle = plt.Circle(circle_center, circle_radius, fill=False)
ax.add_patch(circle)

ball = plt.Circle(ball_position, ball_radius, color='blue')
ax.add_patch(ball)

def animate(i):
    global ball_position, ball_velocity
    ball_position, ball_velocity = update_position(ball_position, ball_velocity, dt)
    ball_position, ball_velocity = handle_collisions(ball_position, ball_velocity, circle_radius, ball_radius)
    
    ball.center = ball_position
    return ball,

ani = animation.FuncAnimation(fig, animate, frames=200, interval=dt*1000, blit=True)
plt.show()
