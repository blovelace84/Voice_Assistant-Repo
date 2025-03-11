import pygame

def handle_input(events, game_state):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game_state.space.gravity = (-980, 0)
            if event.key == pygame.K_RIGHT:
                game_state.space.gravity = (980, 0)
            if event.key == pygame.K_UP:
                game_state.space.gravity = (0, -980)
            if event.key == pygame.K_DOWN:
                game_state.space.gravity = (0, 980)
        if event.type == pygame.KEYUP:
            game_state.space.gravity = (0, 980)