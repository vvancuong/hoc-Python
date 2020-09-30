import pygame

pygame.init()  # initialise khoi tao nhung thu pygame dung duoc

screen = pygame.display.set_mode((500, 600))  # hien thi man hinh game

GREY = (150, 150, 150)
WHITE = (255, 255, 255)
running = True
while running:
    screen.fill(GREY)  # thay doi mau nen
    mouse_x, mouse_y = pygame.mouse.get_pos()
    print(mouse_x)

    pygame.draw.rect(screen, WHITE, (100, 50, 50, 50))  # ve ra hcn mau white
    pygame.draw.rect(screen, WHITE, (100, 200, 50, 50))
    pygame.draw.rect(screen, WHITE, (200, 50, 50, 50))
    pygame.draw.rect(screen, WHITE, (200, 200, 50, 50))
    pygame.draw.rect(screen, WHITE, (300, 50, 150, 50))
    pygame.draw.rect(screen, WHITE, (300, 50, 150, 50))
    pygame.draw.rect(screen, WHITE, (300, 150, 150, 50))

    screen.blit(text_1, (100, 50))
    creen.blit(text_2, (100,200))

    for event in pygame.event.get():  # xet su kien
        if event.type == pygame.QUIT:  # su kien thoat man hinh
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("xxx")
    pygame.display.flip()  # flit: tat ca cac mau moi thay doi dc

pygame.quit()  # khi chay xong xoa toan bo ct, giam bo nho
