import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import cos, sin

# Initialize Pygame and set up the display
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -15)

# Function to draw a cylinder (for the crucible and seed pulling rod)
def draw_cylinder(radius, height, segments):
    glBegin(GL_QUAD_STRIP)
    for i in range(segments + 1):
        angle = 2 * 3.1415926 * i / segments
        x = radius * cos(angle)
        y = radius * sin(angle)
        glVertex3f(x, y, 0)
        glVertex3f(x, y, height)
    glEnd()

# Function to draw a simple box (for furnace walls)
def draw_box(w, h, d):
    glBegin(GL_QUADS)
    # Front face
    glVertex3f(-w, -h, d)
    glVertex3f(w, -h, d)
    glVertex3f(w, h, d)
    glVertex3f(-w, h, d)
    # Back face
    glVertex3f(-w, -h, -d)
    glVertex3f(w, -h, -d)
    glVertex3f(w, h, -d)
    glVertex3f(-w, h, -d)
    # Left face
    glVertex3f(-w, -h, -d)
    glVertex3f(-w, -h, d)
    glVertex3f(-w, h, d)
    glVertex3f(-w, h, -d)
    # Right face
    glVertex3f(w, -h, -d)
    glVertex3f(w, -h, d)
    glVertex3f(w, h, d)
    glVertex3f(w, h, -d)
    # Top face
    glVertex3f(-w, h, -d)
    glVertex3f(w, h, -d)
    glVertex3f(w, h, d)
    glVertex3f(-w, h, d)
    # Bottom face
    glVertex3f(-w, -h, -d)
    glVertex3f(w, -h, -d)
    glVertex3f(w, -h, d)
    glVertex3f(-w, -h, d)
    glEnd()

# Function to draw the seed crystal
def draw_seed():
    glBegin(GL_QUADS)
    # Bottom face
    glVertex3f(-0.5, -0.5, 0)
    glVertex3f(0.5, -0.5, 0)
    glVertex3f(0.5, 0.5, 0)
    glVertex3f(-0.5, 0.5, 0)
    # Top face
    glVertex3f(-0.5, -0.5, 1)
    glVertex3f(0.5, -0.5, 1)
    glVertex3f(0.5, 0.5, 1)
    glVertex3f(-0.5, 0.5, 1)
    # Connecting faces
    glVertex3f(-0.5, -0.5, 0)
    glVertex3f(-0.5, -0.5, 1)
    glVertex3f(-0.5, 0.5, 1)
    glVertex3f(-0.5, 0.5, 0)

    glVertex3f(0.5, -0.5, 0)
    glVertex3f(0.5, -0.5, 1)
    glVertex3f(0.5, 0.5, 1)
    glVertex3f(0.5, 0.5, 0)

    glVertex3f(-0.5, -0.5, 0)
    glVertex3f(0.5, -0.5, 0)
    glVertex3f(0.5, -0.5, 1)
    glVertex3f(-0.5, -0.5, 1)

    glVertex3f(-0.5, 0.5, 0)
    glVertex3f(0.5, 0.5, 0)
    glVertex3f(0.5, 0.5, 1)
    glVertex3f(-0.5, 0.5, 1)
    glEnd()

# Main loop
seed_position = [0, 1.5, 0]
pull_rate = 0.01
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw crucible
    glPushMatrix()
    glTranslatef(0, -1, 0)
    draw_cylinder(1, 2, 32)
    glPopMatrix()

    # Draw furnace walls
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glColor3f(0.7, 0.7, 0.7)
    draw_box(2, 2.5, 2)
    glPopMatrix()

    # Update and draw seed crystal
    seed_position[1] -= pull_rate
    glPushMatrix()
    glTranslatef(seed_position[0], seed_position[1], seed_position[2])
    glColor3f(1, 0, 0)  # Red seed crystal
    draw_seed()
    glPopMatrix()

    pygame.display.flip()
    pygame.time.wait(10)
