import sys

import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Responses to keypresse and ouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets)
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not yet reached"""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the screen"""
    # Redraw the screen on the screen and flip to the new screen.
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprite():
        bullet.draw_bullet()
    ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(bullets):
    """Update the position of bullets and get rid of the old bullets."""
    # Update bullets position.
    bullets.update()

    # Get rid of bullets that has dissappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)