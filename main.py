# Author: Joelene Hales, 2024
# Versions:
#  Python 3.12
#  OpenGL version 3.1.7
#  GLFW version 2.6.4

from OpenGL.GL import *
import glfw


glfw.init()  # Initialize library

# Open a window and create its OpenGL context
screen_width = 1200
screen_height = 800

window = glfw.create_window(screen_width, screen_height, "Hello World", None, None)
glfw.make_context_current(window)


# Render loop
while not glfw.window_should_close(window):  # Repeat until user closes window

    glfw.poll_events()  # Check for and process events (keyboard, mouse, ...)
    
    glClearColor(0, 0, 0, 0)      # Set background color to black (R, G, B, A)
    glClear(GL_COLOR_BUFFER_BIT)  # Apply background colour

	# Draw triangle in immediate mode
    glBegin(GL_TRIANGLES)

    glColor3ub(255, 0, 0)    # Red vertex (R, G, B)
    glVertex2f(0.0, 0.5)      

    glColor3ub(0, 255, 0)    # Green vertex (R, G, B)
    glVertex2f(0.5, -0.25)

    glColor3ub(0, 0, 255)    # Blue vertex (R, G, B)
    glVertex2f(-0.5, -0.25)
    
    glEnd()

    glfw.swap_buffers(window)  # Swap front and back buffers


glfw.terminate()  # Close OpenGL window and terminate GLFW