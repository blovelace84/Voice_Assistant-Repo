import pygame
from my_monkey_game.super_monkey_ball import graphics, input, game_state


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    game = game_state.GameState(screen) #create game state object

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        input.handle_input(events, game) #handle user inputs

        game.update()
        graphics.draw(screen, game) #draw everything

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()