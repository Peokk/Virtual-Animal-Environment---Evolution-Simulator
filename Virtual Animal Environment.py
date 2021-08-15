import pygame, sys , random , math
pygame.init()
#OPTIONS________________________________________________________________________________________________________________
#JUNGLE
settings = input('own / default')

if settings == 'default' or settings == 'd':
    jx = 250
    jy = 1300
    a_count = 10
    food_time = 10
    food_j = 2
    food_p = 1
    energy_time = 20
    energy_take = 2
    energy_start = 30
    energy_add = 10
    energy_to_copulation = 60
    speed = 20

if settings == 'own':
    jy = int(input("jungle height"))
    jx = int(input('jungle width'))
    if int(jy) > 900:
        while int(jy) > 900:
            jy = int(input("jungle height value is too big max = 900"))

    if int(jx) > 1300:
        while int(jx) > 1300:
            jx = int(input("jungle width value is too big max = 1300"))

    #ANIMALS
    a_count = int(input('How many animals at the beginning'))
    speed = int(input('Animal Speed'))

    #FOOD
    food_time = int(input("Create food in seconds"))
    food_j = int(input('How many food in jungle'))
    food_p = int(input('How many food in plains'))

    #ENERGY
    energy_time = int(input('How many seconds to take energy'))
    energy_take = int(input('How many energy to take'))
    energy_start = int(input('How much energy at the beginning'))
    energy_add = int(input('How much energy to add by eating the plant'))
    energy_to_copulation= int(input('Please give me energy to copulation'))
#VARIABLE_______________________________________________________________________________________________________________
#FPS
max_fps = 1
clock = pygame.time.Clock()
delta = 0.0

#ANIMALS
anim = []

#FOOD
food_jun = []
food_pla = []

#SCREEN
screen = pygame.display.set_mode((1600,900))

#POINT JUNLE

pj_x = (1900 - (jx))/2
pj_y = (900 - (jy))/2

#Time
time = 0
time_energy = 0


#FUNCTIONS______________________________________________________________________________________________________________

#FOOD ADD
def food_add():
    for f in range(0,(food_j)):
        food_jun.append([random.randint ((pj_x), (pj_x) + (jx)), random.randint((pj_y), (pj_y) + (jy))])

    for f in range(0,(food_p)):
        food_pla.append([random.randint(330,1600),random.randint(0,900)])

def food_print():
    for i in range(0,len(food_jun)):
            pygame.draw.rect(screen, (184, 186, 86), (food_jun[i][0], food_jun[i][1], 12 , 12))
    for f in range(0,len(food_pla)):
        pygame.draw.rect(screen, (10, 171, 131), (food_pla[f][0], food_pla[f][1], 12, 12))


#ANIM ADD
for a in range(0,int(a_count)):
    anim.append([random.randint(320, 1580),random.randint(20, 880),(energy_start),0])

def anim_print():
    for a in anim:

        if a[2] < energy_start*0.5:
            pygame.draw.rect(screen, (222, 64, 64), (a[0], a[1], 20, 20))
        elif a[2] < energy_start:
            pygame.draw.rect(screen, (173, 23, 23), (a[0], a[1], 20, 20))
        elif a[2] < energy_start * 1.5:
            pygame.draw.rect(screen, (112, 8, 8), (a[0], a[1], 20, 20))
        elif a[2] < energy_start * 2:
            pygame.draw.rect(screen, (82, 2, 2), (a[0], a[1], 20, 20))
        else:
            pygame.draw.rect(screen, (140, 13, 13), (a[0], a[1], 20, 20))

def anim_move():
    for i in range(len(anim)):
        move = random.randint(0,3)
        if anim[i][1] >= 860:
            anim[i][1] -= 20
        if anim[i][1] <= 40:
            anim[i][1] += 20
        if anim[i][0] <= 340:
            anim[i][0] += 20
        if anim[i][0] >= 1560:
            anim[i][0] -= 20

        if move == 0:
            anim[i][0] -=speed
        if move == 1:
            anim[i][0] +=speed
        if move == 2:
            anim[i][1] -=speed
        if move == 3:
            anim[i][1] +=speed

def fast():
    global max_fps
    mx,my= pygame.mouse.get_pos()
    if mx >= 25 and mx <= 275 and my >= 835 and my <= 875:
        pygame.draw.rect(screen, (10, 10, 10), (mx, 850, 15, 15))
        max_fps = float(mx-24)

def pokrywaja_sie(box1,box2):

    srodek_1_x = box1.x + box1.width/2
    srodek_2_x = box2.x + box2.width / 2
    srodek_1_y = box1.y + box1.height / 2
    srodek_2_y = box2.y + box2.height / 2

    r_1 = box1.width/2
    r_2 = box2.width/2

    odleglos = math.sqrt((srodek_2_x - srodek_1_x)**2 + (srodek_1_y - srodek_2_y)**2)
    if odleglos > r_1 + r_2:
        return False
    return True

def anim_ded():
    for animal in anim:

        if animal[2] <= 0:
            anim.remove(animal)

def chart():
    pygame.draw.rect(screen, (55, 163, 16), (250, 10, 5, 5))

def click():
    mx, my = pygame.mouse.get_pos()
    for o in anim:
        if keys[pygame.K_r]:
            if pokrywaja_sie(pygame.Rect((o[0]), (o[1]), 40, 40), pygame.Rect(mx, my, 45, 45)):
                print(o)

for i in range(50):
    food_add()

#LOOP___________________________________________________________________________________________________________________
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit(0)
#before the loop--------------------------------------------------------------------------------------------------------
    anim_ded()
#FPS____________________________________________________________________________________________________________________
    delta += clock.tick() / 1000.0
    while delta > 1 / max_fps:
        delta -= 1 / max_fps

#VARIABLE IN LOOP_______________________________________________________________________________________________________
        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            print(len(anim))


        click()
        for i,o in enumerate(food_jun):
            for a in anim:
                if pokrywaja_sie(pygame.Rect((o[0]), (o[1]), 15,15), pygame.Rect(a[0], a[1], 20, 20)):
                    food_jun.pop(i)
                    a[2] = a[2] + energy_add
                    a[3] = a[3] + 1
                    food_jun.append([random.randint((pj_x), (pj_x) + (jx)),random.randint((pj_y), (pj_y) + (jy))])

        for i,o in enumerate(food_pla):
            for a in anim:
                if pokrywaja_sie(pygame.Rect((o[0]), (o[1]), 15,15), pygame.Rect(a[0], a[1], 20, 20)):
                    food_pla.pop(i)
                    a[2] = a[2] + energy_add
                    a[3] = a[3] + 1
                    food_pla.append([random.randint((pj_x), (pj_x) + (jx)),random.randint((pj_y), (pj_y) + (jy))])

        for o in anim:
            for o2 in anim:
                if o != o2:
                    if o[2] > energy_to_copulation and o2[2] > energy_to_copulation:
                        if pokrywaja_sie(pygame.Rect((o[0]), (o[1]), 20, 20), pygame.Rect(o2[0], o2[1], 20, 20)):
                            anim.append([random.randint(320, 1580), random.randint(20, 880), (energy_start), 0])
                            o[2] /= 2
                            o2[2] /= 2



#DRAWING________________________________________________________________________________________________________________
        pygame.display.flip()
        screen.fill((107, 191, 94))

        #TERRAIN
        pygame.draw.rect(screen, (77, 151, 74), ( int((1900 - jx)/2) , int((900 - jy)/2) ,int(jx) ,int(jy)))
        pygame.draw.rect(screen, (230,230,230), (0,0,300,900))

        #FPS
        pygame.draw.rect(screen, (100,100,100), (25,850,250,15))
        fast()

        time += 1
        #FOOD
        if time == int(food_time):
            food_add()
            time = 0
        food_print()

        time_energy += 1
        if time_energy == int(energy_time):
            time_energy = 0
            for a in range(0, int(len(anim))):
                anim[a][2] = anim[a][2] - int(energy_take)

        #ANIMALS
        anim_print()
        anim_move()