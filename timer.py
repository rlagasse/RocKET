import pygame
import time #needed for countdown

# Initialize Pygame
pygame.init()

# Create a timer object
time = pygame.time.Clock()

# Set the countdown time to 1 minute (60000 milliseconds)
countdown_time = 60000  # 1 minute

# Variables
timer_has_started = False
program_is_running = True

# displaying the time in new window
screen = pygame.display.set_mode((400, 200))  # Set window size
pygame.display.set_caption("Countdown Timer")

# Define font for the timer display
font = pygame.font.Font(None, 74)  # None uses the default font, size 74

while program_is_running:

    #if the user want to exit, this event is handled
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            program_is_running = False

    # If the timer hasn't started yet, start it
    if not timer_has_started:
        timer_has_started = True
        start_time = pygame.time.get_ticks()  # Get the current ticks when the timer starts

    # Calculate how much time has passed since the timer started
    time_elapsed = pygame.time.get_ticks() - start_time  # Elapsed time in milliseconds

    # Calculate the remaining time
    time_left = countdown_time - time_elapsed

    # Check if the countdown has reached zero
    if time_left <= 0:
        print("Time's up!")
        time_left = 0  # Set to zero to avoid negative time
        program_is_running = False  # Stop the loop for demonstration purposes

    # Convert remaining time to seconds and format it
    sec = (time_left // 1000) % 60
    min = (time_left // 60000) % 60
    display_time = f"{min:02}:{sec:02}"  # Format as MM:SS

    # Clear the screen
    screen.fill((0, 0, 0))  # Fill the screen with black

    # Render the timer text
    text_surface = font.render(display_time, True, (255, 255, 255))  # White color
    text_rect = text_surface.get_rect(center=(200, 100))  # Center the text

    # Draw the text on the screen
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

    # Control the frame rate to 60 FPS
    time.tick(60)

# Clean up and quit
pygame.quit()
