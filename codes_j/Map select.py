import pygame

# initialize
pygame.init()
screen_width, screen_height = 640, 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Move selected shape")

# repeat key
pygame.key.set_repeat(1000, 1)
    
# keyup
def keyup(key):
    pass

# keydown
def keydown(key):
    pass

# Start screen
def Start_screen():
    screen.fill("white")
    
    font1 = pygame.font.SysFont('arial',50)
    text1 = font1.render("Alkkagi",True, "blue")
    text1_rect = text1.get_rect(center=(screen.get_width() // 2, screen.get_height()*1/4))
    screen.blit(text1, text1_rect)

    font2 = pygame.font.SysFont('arial',50)
    text2 = font2.render("Press Enter to Start",True, "blue")
    text2_rect = text2.get_rect(center=(screen.get_width() // 2, screen.get_height()*3/4))
    screen.blit(text2, text2_rect)

# Map append
def Map_append():
    screen.fill('white')
    map1 = pygame.image.load("board.png")
    map1 = pygame.transform.scale(map1, (300,300))
    map_images.append(map1)
    map2 = pygame.image.load("bomb.png")
    map2 = pygame.transform.scale(map2, (300,300))
    map_images.append(map2)
    
    x = 10
    y = 100
    for i in range(len(map_images)):
        screen.blit(map_images[i],(x,y))
        x += 320

    font = pygame.font.SysFont('arial',50)
    text = font.render("< Vanila >",True, "blue")
    text_rect = text.get_rect(center=(screen.get_width()*1/4, 450))
    screen.blit(text, text_rect)

    font = pygame.font.SysFont('arial',50)
    text = font.render("< Bomb >",True, "blue")
    text_rect = text.get_rect(center=(screen.get_width()*3/4, 450))
    screen.blit(text, text_rect)

# Text 'select'
def text_Select():
    font = pygame.font.SysFont('arial',50)
    text = font.render("Map select",True, "blue")
    text_rect = text.get_rect(center=(screen.get_width() // 2, 50))
    screen.blit(text, text_rect)

# First screen
running = True
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            waiting = False

    Start_screen()
    pygame.display.flip()


# Second screen
selected_map_index = 0
while running:
    map_images = []
    map_rects = []
    Map_append()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                selected_map_index = (selected_map_index - 1) % 2
            elif event.key == pygame.K_RIGHT:
                selected_map_index = (selected_map_index + 1) % 2
            elif event.key == pygame.K_RETURN:
                map_selected = False

    # Highlight the selected map with a rectangle
    if selected_map_index == 0:
        pygame.draw.rect(screen, (255, 0, 0), ((10, 100),(300,300)),10)
    elif selected_map_index == 1:
        pygame.draw.rect(screen, (255, 0, 0), ((330, 100),(300,300)),10)
    else:
        pass

    text_Select()
    
    pygame.display.flip()

    

pygame.quit()
