import pygame,os,math
from random import*

from pygame.constants import MOUSEMOTION

pygame.init()

screen_width = 960
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# FPS
clock = pygame.time.Clock()

# 화면 타이틀 설정
pygame.display.set_caption("game")

# 이미지 폴더 찾기
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path,"images")
# 이미지 불러오기
    # 배경 이미지
background = pygame.image.load(os.path.join(image_path,"background.png"))

    # 캐릭터 이미지
character = pygame.image.load(os.path.join(image_path,"character.png"))
character_rect = character.get_rect().size
character_width = character_rect[0]
character_height = character_rect[1]
character_x_pos = (screen_width/2 - character_width/2)
character_y_pos = (screen_height/2 - character_height/2)

        # 캐릭터 이동 관련
character_speed = 10
to_x = 0
to_y = 0

    # 공격 이미지
attack = pygame.image.load(os.path.join(image_path,"attack.png"))
attack_reck = attack.get_rect().size
attack_width = attack_reck[0]
attack_height = attack_reck[1]
#+ character_height/2 - attack_height/2

    # 공격 속도
attack_speed = 10

    # 공격 피사체 속도
attack_subject_speed = 10

    # 공격's
attacks = []    

    # 공격 회전

attack_angles = []

    # 몬스터 이미지
monster = pygame.image.load(os.path.join(image_path,"monster.png"))
monster_reck = monster.get_rect().size
monster_width = monster_reck[0]
monster_height = monster_reck[1]
monster_x_pos =  randint(1,screen_width)
monster_y_pos =  randint(1,screen_height)

# 이벤트 루프
running = True
while running:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if event.type == pygame.MOUSEMOTION:
        #     character_x_pos = pygame.mouse.get_pos()[0]
        #     character_y_pos = pygame.mouse.get_pos()[1]

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                to_y -= character_speed
            elif event.key == pygame.K_s:
                to_y += character_speed
            elif event.key == pygame.K_a:
                to_x -= character_speed
            elif event.key == pygame.K_d:
                to_x += character_speed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            attack_x_pos = character_x_pos
            attack_y_pos = character_y_pos
            attack_position = pygame.mouse.get_pos()
            attack_angle = math.atan2(attack_position[1] \
                - attack_y_pos + attack_height/2, \
                    attack_position[0] - attack_x_pos + \
                        attack_width/2)
            attack_angles.append([attack_angle])
            attacks.append([attack_x_pos,attack_y_pos])

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                to_y = 0
            elif event.key == pygame.K_a or event.key == pygame.K_d:
                to_x = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # 어택 피사체 날라가게 & 벽에 닿으면 사라지게
    attacks = [[w[0],w[1] - attack_subject_speed]for w in attacks]
    attacks = [[w[0],w[1]]for w in attacks if w[1] > 0]

    # 위치 정보 다시 불러오기
        # 캐릭터    
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

        # 어택
    # attack_reck = attack.get_rect()
    # attack_reck.left = attack_x_pos
    # attack_reck.top = attack_y_pos
    # attack_x_pos = character_x_pos 
    # attack_y_pos = character_y_pos

    # 이미지 출력
        # 백그라운드 이미지
    screen.blit(background,(0,0))

    #     # 어택 이미지 및 회전
    # position = pygame.mouse.get_pos()
    # attack_angle = math.atan2(position[1] - attack_y_pos + attack_height/2, position[0] - attack_x_pos + attack_width/2)
    # attackrot = pygame.transform.rotate(attack, 276 - attack_angle*57.29)  
    # attackpos1 = (attack_x_pos -attackrot.get_rect().width//2, attack_y_pos - attackrot.get_rect().height//2)
    # screen.blit(attackrot,(attackpos1[0],attackpos1[1]))

        # 캐릭터 이미지 및 회전
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1] - character_y_pos + character_height/2, position[0] - character_x_pos + character_width/2)
    playerrot = pygame.transform.rotate(character, 276 - angle*57.29)  
    playerpos1 = (character_x_pos -playerrot.get_rect().width//2, character_y_pos - playerrot.get_rect().height//2)
    screen.blit(playerrot,(playerpos1[0],playerpos1[1]))

        # 어택 이미지 및 회전

    for attack_angle_index, attack_angle_val in enumerate(attack_angles):
        for w in len(attack_angles):
            attackrot = pygame.transform.rotate(attack, 276 - attack_angles[w]*57.29)  

    for attack_x_pos ,attack_y_pos in attacks:
        # attack_position = pygame.mouse.get_pos()
        # attack_angle = math.atan2(attack_position[1] - attack_y_pos + attack_height/2, attack_position[0] - attack_x_pos + attack_width/2)
        # for attack_angle_index, attack_angle_val in enumerate(balls):
        #     attackrot = pygame.transform.rotate(attack, 276 - attack_angle*57.29)  
        attackpos1 = (attack_x_pos -attackrot.get_rect().width//2, attack_y_pos - attackrot.get_rect().height//2)
        screen.blit(attackrot,(attackpos1[0],attackpos1[1]))

        # 몬스터 이미지
    screen.blit(monster,(monster_x_pos,monster_y_pos))
    pygame.display.flip()
    pygame.display.update()

pygame.quit()
