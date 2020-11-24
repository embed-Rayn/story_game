import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado game") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("D:\\PycharmProject\\pygame\\pygame_basic\\background.png")

# 캐릭터(스프라이트 불러오기)
character = pygame.image.load("D:\\PycharmProject\\pygame\\pygame_basic\\character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0]     # 캐릭터의 가로크기
character_height = character_size[1]    # 캐릭터의 세로 크기
character_x_pos = screen_width / 2  - character_width /2 # 화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
character_y_pos = screen_height - character_height        # 화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로)

to_x = 0
to_y = 0
game_speed = 1
# 이벤트 루프
running = True # 게임이 진행 중인가?
cnt = 0
while running:
    cnt += 1
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수를 설정

    print("fps : ", clock.get_fps())
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌렸는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= game_speed
            elif event.key == pygame.K_RIGHT:
                to_x += game_speed
            elif event.key == pygame.K_UP:
                to_y -= game_speed
            elif event.key == pygame.K_DOWN:
                to_y += game_speed
        if event.type == pygame.KEYUP: # 키가 눌렸는지 확인
            if event.key == pygame.K_UP or pygame.K_DOWN:
                to_y = 0
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                to_x = 0
    character_y_pos += to_y * dt
    character_x_pos += to_x * dt

    if character_x_pos<0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width-character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    #screen.fill((0,0,255))
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기

    pygame.display.update() # 게임화면을 다시 그리기

# pygame 종료
pygame.quit()