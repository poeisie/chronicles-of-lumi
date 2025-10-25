import pgzrun
from platformer import *

TILE_SIZE = 16
ROWS = 20
COLS = 30

WIDTH = COLS * TILE_SIZE
HEIGHT = ROWS * TILE_SIZE
TITLE = "Chronicles of Lumi"

game_state = "menu"
music_enabled = True
sounds_enabled = True

platforms = []
obstacles = []
plants = []
coins = []
enemies = []
player = None

gravity = 1
jump_velocity = -10
over = False
win = False

class Enemy:
    def __init__(self, x, y, patrol_distance=100):
        self.actor = Actor("enemy_idle")
        self.actor.x = x
        self.actor.y = y
        self.start_x = x
        self.patrol_distance = patrol_distance
        self.speed = 1
        self.direction = 1
        self.alive = True
        self.idle_images = ["enemy_idle"]
        self.walk_images = ["enemy_walk_left", "enemy_walk_right"]
        self.animation_frame = 0
        self.animation_speed = 10
        self.animation_counter = 0
        self.is_walking = True
    
    def update(self):
        if not self.alive:
            return
        
        self.actor.x += self.speed * self.direction
        
        if self.actor.x > self.start_x + self.patrol_distance:
            self.direction = -1
        elif self.actor.x < self.start_x - self.patrol_distance:
            self.direction = 1
        
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.animation_counter = 0
            if self.is_walking:
                if self.direction == -1:
                    self.actor.image = "enemy_walk_left"
                else:
                    self.actor.image = "enemy_walk_right"
    
    def draw(self):
        if self.alive:
            self.actor.draw()

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = Rect((x, y), (width, height))
        self.text = text
        self.is_hovered = False
    
    def draw(self):
        color = "white" if self.is_hovered else "gray"
        screen.draw.rect(self.rect, color)
        screen.draw.text(self.text, center=self.rect.center, fontsize=20, color=color)
    
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

play_button = Button(WIDTH//2 - 60, 100, 120, 35, "START")
music_button = Button(WIDTH//2 - 60, 145, 120, 35, "MUSIC: ON")
sound_button = Button(WIDTH//2 - 60, 190, 120, 35, "SOUNDS: ON")
exit_button = Button(WIDTH//2 - 60, 235, 120, 35, "EXIT")

if music_enabled:
    music.play("theme")

def init_game():
    global platforms, obstacles, plants, coins, enemies, player, over, win
    platforms = build("platformer_platforms.csv", TILE_SIZE)
    obstacles = build("platformer_obstacles.csv", TILE_SIZE)
    plants = build("platformer_plants.csv", TILE_SIZE)
    coins = build("platformer_coins.csv", TILE_SIZE)
    
    enemies = [
        Enemy(80, HEIGHT - TILE_SIZE * 19, 60),
        Enemy(296, HEIGHT - TILE_SIZE * 16, 60),
        Enemy(420, HEIGHT - TILE_SIZE * 11, 40),
        Enemy(150, HEIGHT - TILE_SIZE * 8, 70),
        Enemy(300, HEIGHT - TILE_SIZE * 2, 60),
    ]
    
    player = Actor("p_right")
    player.bottomleft = (0, HEIGHT - TILE_SIZE)
    player.velocity_x = 3
    player.velocity_y = 0
    player.jumping = False
    player.alive = True
    player.attacking = False
    player.attack_timer = 0
    player.attack_duration = 20
    player.idle_left_image = "p_left"
    player.idle_right_image = "p_right"
    player.walk_left_image = "p_walk_left"
    player.walk_right_image = "p_walk_right"
    player.attack_left_image = "p_attack_left"
    player.attack_right_image = "p_attack_right"
    player.jump_image = "p_jump"
    player.animation_frame = 0
    player.animation_counter = 0
    player.is_moving = False
    player.facing_right = True
    
    over = False
    win = False

def draw():
    screen.clear()
    screen.fill("black")
    
    if game_state == "menu":
        draw_menu()
    elif game_state == "playing":
        draw_game()

def draw_menu():
    screen.draw.text("CHRONICLES OF LUMI", center=(WIDTH//2, 50), fontsize=35, color="white")
    play_button.draw()
    music_button.draw()
    sound_button.draw()
    exit_button.draw()

def draw_game():
    for platform in platforms:
        platform.draw()
    for obstacle in obstacles:
        obstacle.draw()
    for plant in plants:
        plant.draw()
    for coin in coins:
        coin.draw()
    for enemy in enemies:
        enemy.draw()
    
    if player and player.alive:
        player.draw()
    
    if over:
        box = Rect(WIDTH//2 - 80, HEIGHT//2 - 40, 160, 80)
        screen.draw.filled_rect(box, "black")
        screen.draw.rect(box, "white")
        screen.draw.text("GAME OVER", center=(WIDTH/2, HEIGHT/2 - 10), fontsize=30, color="red")
        screen.draw.text("Press SPACE", center=(WIDTH/2, HEIGHT/2 + 20), fontsize=15, color="gray")
    if win:
        box = Rect(WIDTH//2 - 80, HEIGHT//2 - 40, 160, 80)
        screen.draw.filled_rect(box, "black")
        screen.draw.rect(box, "white")
        screen.draw.text("YOU WIN!", center=(WIDTH/2, HEIGHT/2 - 10), fontsize=30, color="green")
        screen.draw.text("Press SPACE", center=(WIDTH/2, HEIGHT/2 + 20), fontsize=15, color="gray")

def update():
    global over, win
    
    if game_state == "menu":
        pos = pygame.mouse.get_pos()
        play_button.check_hover(pos)
        music_button.check_hover(pos)
        sound_button.check_hover(pos)
        exit_button.check_hover(pos)
    
    elif game_state == "playing" and not over and not win:
        update_game()

def update_game():
    global over, win
    
    player.is_moving = False
    
    if player.attacking:
        player.attack_timer -= 1
        if player.facing_right:
            player.image = player.attack_right_image
        else:
            player.image = player.attack_left_image
        
        if player.attack_timer <= 0:
            player.attacking = False
            if player.facing_right:
                player.image = player.idle_right_image
            else:
                player.image = player.idle_left_image
        
        for enemy in enemies:
            if enemy.alive and player.distance_to(enemy.actor) < 40:
                enemy.alive = False
                if sounds_enabled:
                    sounds.attack.play()
    
    elif keyboard.LEFT and player.midleft[0] > 0:
        player.x -= player.velocity_x
        player.is_moving = True
        player.facing_right = False
        if player.collidelist(platforms) != -1:
            object = platforms[player.collidelist(platforms)]
            player.x = object.x + (object.width / 2 + player.width / 2)
    elif keyboard.RIGHT and player.midright[0] < WIDTH:
        player.x += player.velocity_x
        player.is_moving = True
        player.facing_right = True
        if player.collidelist(platforms) != -1:
            object = platforms[player.collidelist(platforms)]
            player.x = object.x - (object.width / 2 + player.width / 2)
    
    if player.is_moving and not player.attacking:
        if player.facing_right:
            player.image = player.walk_right_image
        else:
            player.image = player.walk_left_image
    elif not player.attacking and not player.jumping:
        if player.facing_right:
            player.image = player.idle_right_image
        else:
            player.image = player.idle_left_image

    player.y += player.velocity_y
    player.velocity_y += gravity
    if player.collidelist(platforms) != -1:
        object = platforms[player.collidelist(platforms)]
        
        if player.velocity_y >= 0:
            player.y = object.y - (object.height / 2 + player.height / 2)
            player.jumping = False
        else:
            player.y = object.y + (object.height / 2 + player.height / 2)
        player.velocity_y = 0
    
    for enemy in enemies:
        enemy.update()
        if enemy.alive and player.colliderect(enemy.actor):
            player.alive = False
            over = True
            if music_enabled:
                music.play("game_over")
        
    if player.collidelist(obstacles) != -1:
        player.alive = False
        over = True
        if music_enabled:
            music.play("game_over")
    
    for coin in coins:
        if player.colliderect(coin):
            coins.remove(coin)
            if sounds_enabled:
                sounds.coin.play()
    
    alive_enemies = sum(1 for enemy in enemies if enemy.alive)
    if len(coins) == 0 and alive_enemies == 0:
        win = True
        if music_enabled:
            music.play("win")

def on_key_down(key):
    global game_state
    
    if game_state == "playing":
        if key == keys.UP and not player.jumping:
            player.velocity_y = jump_velocity
            player.jumping = True
            if sounds_enabled:
                sounds.jump.play()
        
        if key == keys.D and not player.attacking:
            player.attacking = True
            player.attack_timer = player.attack_duration
            if player.facing_right:
                player.image = player.attack_right_image
            else:
                player.image = player.attack_left_image
        
        if (over or win) and key == keys.SPACE:
            game_state = "menu"
            if music_enabled:
                music.play("theme")

def on_mouse_down(pos):
    global game_state, music_enabled, sounds_enabled
    
    if game_state == "menu":
        if play_button.is_clicked(pos):
            init_game()
            game_state = "playing"
        
        elif music_button.is_clicked(pos):
            music_enabled = not music_enabled
            music_button.text = f"MUSIC: {'ON' if music_enabled else 'OFF'}"
            if music_enabled:
                music.play("theme")
            else:
                music.stop()
        
        elif sound_button.is_clicked(pos):
            sounds_enabled = not sounds_enabled
            sound_button.text = f"SOUNDS: {'ON' if sounds_enabled else 'OFF'}"
        
        elif exit_button.is_clicked(pos):
            exit()

pgzrun.go()