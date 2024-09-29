import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
END_SCREEN_WIDTH = 1024
END_SCREEN_HEIGHT = 600

# Create the display window
end_screen = pygame.display.set_mode((END_SCREEN_WIDTH, END_SCREEN_HEIGHT))
pygame.display.set_caption("GAME OVER!")


class end_page:
    
    def __init__(self, won_or_lost):
        self.result = won_or_lost  # Accept either "Won" or "Lost"

        # Load background image
        self.background_image = pygame.image.load('assets/inside_castle.png')
        self.background_image = pygame.transform.scale(self.background_image, (END_SCREEN_WIDTH, END_SCREEN_HEIGHT))

        # Load exit button image 
        self.exit_image = pygame.image.load('assets/exit_button.png')

        # Scale the exit button 
        self.exit_image = pygame.transform.scale(self.exit_image, (300, 200))  # Exit button size

        # Position the exit button
        self.exit_button = self.exit_image.get_rect(center=(END_SCREEN_WIDTH // 2, END_SCREEN_HEIGHT // 2 + 90))  # Center the exit button

        # Font setup for displaying result text
        self.font = pygame.font.Font(None, 74)  # Default font and size
        self.text = self.font.render(f"You {self.result}!", True, (255, 255, 255))  # White text
        self.text_rect = self.text.get_rect(center=(END_SCREEN_WIDTH // 2, END_SCREEN_HEIGHT // 2))  # Position above buttons

    def draw_buttons(self):
        """Draw the exit button onto the window."""
        end_screen.blit(self.exit_image, self.exit_button.topleft)

    def draw_result_text(self):
        """Draw the result text onto the window."""
        end_screen.blit(self.text, self.text_rect)
    
    def exit_is_pressed(self):
        """Check if the exit button is pressed."""
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        # Check if the mouse is over the exit button and if it is pressed
        if self.exit_button.collidepoint(mouse_pos) and mouse_pressed:
            return True
        
        return False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Check if the exit button is pressed
            if self.exit_is_pressed():
                print("Quitting Game!")
                pygame.quit()
                sys.exit()

            # Draw the background image
            end_screen.blit(self.background_image, (0, 0))

            # Draw the result text
            self.draw_result_text()

            # Draw the exit button
            self.draw_buttons()

            # Update the display
            pygame.display.flip()


if __name__ == "__main__":
    # Create an instance of EndPage, passing either "Won" or "Lost" as the argument
    page = end_page("Won")  # Change "Won" to "Lost" if needed
    page.run()  # Run the end screen loop