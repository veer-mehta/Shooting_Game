import pygame, time, random, math


def restart(type=0):

    #Colourz
    global blue, red, green, yellow, cyan, lime, orange, white, black, grey, night_blue

    def blue(): return 101, 119, 179
    def red(): return 255, 0, 0
    def green(): return 72, 161, 77
    def yellow(): return 210, 210, 50
    def cyan(): return 135, 206, 250
    def lime(): return 60, 200, 120
    def orange(): return 255, 69, 0
    def white(): return 253, 251, 249
    def black(): return 21, 23, 24
    def grey(): return 150, 150, 150
    def night_blue(): return 0, 0, 30

    #Classez
    global Enemy, Bullet

    class Enemy:
        def __init__(self, id, pos):
            self.id = id
            self.pos = pos
            self.type = ""

            if random.randrange(4) == 2:
                self.type = "gunner"
                self.health = 150
            else:
                self.type = "melee"
                self.health = 100


        def Move(self):
            d = math.isqrt((int(p_pos[0]-self.pos[0]))**2 + (int(p_pos[1]-self.pos[1]))**2)
            dist = d
            d_x, d_y = int(p_pos[0]-self.pos[0]), int(p_pos[1]-self.pos[1])
            d = [d_x/d, d_y/d]

            if d[0] > 1.0 or d[1] > 1.0:
                if d[0] > d[1]:
                    d[1]=(d[1]*1.0)/d[0]
                    d[0]=1.0
                elif d[0] > d[1]:
                    d[0]=(d[0]*1.0)/d[1]
                    d[1]=1.0

            if dist <= 10*i_rad and self.type == "melee":
                self.pos[0] -= d[0]
                self.pos[1] -= d[1]
                if random.randrange(100) == random.randrange(100):
                    self.Attack()

            elif int(dist) <= 80*i_rad and self.type == "gunner":
                if random.randrange(100) == random.randrange(200):
                    self.Attack()

            else:
                self.pos[0] += d[0]
                self.pos[1] += d[1]


        def Attack(self):
            global _enmy_blt_
            if self.type == "melee":
                d_stc['health']-=20
                d_stc['damage_dealt']+=20

            elif self.type == "gunner":

                d = math.isqrt((int(p_pos[0]-self.pos[0]))**2 + (int(p_pos[1]-self.pos[1]))**2)
                dist = d
                d_x, d_y = int(p_pos[0]-self.pos[0]), int(p_pos[1]-self.pos[1])
                d = [d_x/d, d_y/d]

                if d[0] > 1.0 or d[1] > 1.0:
                    if d[0] > d[1]:
                        d[1]=(d[1]*1.0)/d[0]
                        d[0]=1.0
                    elif d[0] > d[1]:
                        d[0]=(d[0]*1.0)/d[1]
                        d[1]=1.0
                ratio = d

                l_enmy_blt.append(Bullet(_enmy_blt_, self.pos, ratio))
                _enmy_blt_+=1


    class Bullet():

        def __init__(self, id, pos, ratio):
            self.id = id
            self.pos = pos
            self.ratio = ratio
            self.turn = 0


        def Move(self):
            if self.turn >= int(math.copysign(self.ratio[0], 1) + math.copysign(self.ratio[1], 1)):
                self.pos[0] += self.ratio[0]
                self.pos[1] += self.ratio[1]
                self.turn=0
            else:
                self.turn+=1

    #CONSTANTZ
    global UP, DOWN, LEFT, RIGHT, X, Y, STC_SZ, i_rad, i_side, p_pos, t_eph, P_SPD, CRT_SPD

    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    X, Y = 1156, 668 # You can change dimensions of the window here
    STC_SZ = 10 #Stats tab Size
    i_rad = 6 #Radius of bullet
    i_side = 30 #Length or Enemy's body
    p_pos = [(X-(i_side/2))/2, (Y*(STC_SZ-1)/STC_SZ)-(i_side/2)]
    P_SPD = 346.8/X
    CRT_SPD = 100.0



    #variablez
    global d_plr, d_stc, l_blt, l_enmy, l_enmy_blt, _blt_, _enmy_, _enmy_blt_, dir

    if type == 0:
        d_stc = {"health": 100, "lives": 3, "ammo":350, "total_kills": 0, "damage_dealt": 0, "score": 0}  #PLAYER INFO

    l_blt = []
    l_enmy = []
    l_enmy_blt = []
    _blt_ = 0
    _enmy_ = 0
    _enmy_blt_ = 0
    dir = 0 #DIRECTION OF PLAYER

    #INITIALIZATION
    global f_sz, SCREEN, font, i_time

    i_time = time.time()
    f_sz = 25

    pygame.init()
    pygame.font.init()

    srn = 1 # Change 1 to 2 to change the view to fullscreen mode or vice versa
    if srn == 1: SCREEN = pygame.display.set_mode((X, Y))
    if srn == 2: SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    if type == 0:
        try: font = pygame.font.Font("C:/Users/veera/AppData/Local/Microsoft/Windows/Fonts/visitor2.ttf", 80)
        except: font = pygame.font.SysFont("", 80)

        for i in range(3, 0, -1):
            pygame.draw.rect(SCREEN, night_blue(), pygame.Rect(0, 0, X, Y))
            prt(str(i), X/2, Y/2, white())
            pygame.display.flip()
            time.sleep(0.5)

        try: font = pygame.font.Font("C:/Users/veera/AppData/Local/Microsoft/Windows/Fonts/visitor2.ttf", 100)
        except: font = pygame.font.SysFont("", 100)

        pygame.draw.rect(SCREEN, night_blue(), pygame.Rect(0, 0, X, Y))
        prt("!!SHOOT!!", X/2, Y/2, white())
        pygame.display.flip()
        time.sleep(0.3)

        try: font = pygame.font.Font("C:/Users/veera/AppData/Local/Microsoft/Windows/Fonts/visitor2.ttf", f_sz)
        except: font = pygame.font.SysFont("", f_sz)


def prt(v_nm, x_var, y_var, f_clr, tilt=0, bg_clr=None, f_sz=35, b_center=True):
    if bg_clr==None:
        text = font.render(v_nm, True, f_clr)
    else:
        text = font.render(v_nm, True, f_clr, bg_clr)
        textRect = text.get_rect()
        textRect = (int(x_var), int(y_var))
    if tilt != 0:
        text = pygame.transform.rotate(text, tilt)
    if b_center == True:
        textRect = text.get_rect()
        textRect.center = (int(x_var), int(y_var))
    SCREEN.blit(text, textRect)


def refresh():

    pygame.draw.rect(SCREEN, black(), pygame.Rect(0, 0, X, int(Y*(STC_SZ-1)/STC_SZ)))

    # Bullets
    for i in range(len(l_blt)):
        pygame.draw.circle(SCREEN, red(), l_blt[i].pos, i_rad)

    for i in range(len(l_enmy_blt)):
        pygame.draw.circle(SCREEN, yellow(), l_enmy_blt[i].pos, i_rad)

    # Enemies
    for i in range(len(l_enmy)):
        if l_enmy[i].type == "melee":
            pygame.draw.rect(SCREEN, white(), pygame.Rect(int(l_enmy[i].pos[0])-int(i_side/2), int(l_enmy[i].pos[1])-int(i_side/2), i_side, i_side))
            pygame.draw.rect(SCREEN, grey(), pygame.Rect(int(l_enmy[i].pos[0])-int(i_side/2), int(l_enmy[i].pos[1])-int(i_side/2), i_side, i_side), 3)
        elif l_enmy[i].type == "gunner":
            pygame.draw.rect(SCREEN, grey(), pygame.Rect(int(l_enmy[i].pos[0])-int(i_side/2), int(l_enmy[i].pos[1])-int(i_side/2), i_side, i_side))
            pygame.draw.rect(SCREEN, white(), pygame.Rect(int(l_enmy[i].pos[0])-int(i_side/2), int(l_enmy[i].pos[1])-int(i_side/2), i_side, i_side), 2)


    # PLAYER BODY
    pygame.draw.rect(SCREEN, blue(), pygame.Rect(int(p_pos[0]-i_side/2), int(p_pos[1]-i_side/2), i_side, i_side))
    pygame.draw.rect(SCREEN, white(), pygame.Rect(int(p_pos[0]-i_side/2), int(p_pos[1]-i_side/2), i_side, i_side), 2)

    # STATUS BAR
    pygame.draw.rect(SCREEN, white(), pygame.Rect(0, int(Y*(STC_SZ-1)/STC_SZ), X, int(Y/STC_SZ)))
    prt(f"Health: {d_stc['health']}", int(X/4), int(Y*((STC_SZ*4)-3)/(STC_SZ*4)), cyan())
    prt(f"Ammo: {d_stc['ammo']}", int(X*2/4), int(Y*((STC_SZ*4)-3)/(STC_SZ*4)), orange())
    prt(f"Score: {d_stc['score']}", int(X*3/4), int(Y*((STC_SZ*4)-3)/(STC_SZ*4)), lime())

    # WARNING
    if d_stc["ammo"] == 0:
        prt("!! No Ammo !!", int(X*2/5), int(Y*((STC_SZ*4)-1)/(STC_SZ*4)), red())
    elif d_stc["ammo"] <= 50:
        prt("!! Low Ammo !!", int(X*2/5), int(Y*((STC_SZ*4)-1)/(STC_SZ*4)), orange())
    if d_stc['health'] <= 50:
        prt("!! Low Health !!", int(X/5), int(Y*((STC_SZ*4)-1)/(STC_SZ*4)), red())


    pygame.display.flip()


def create_blt():
    global _blt_
    d_stc["ammo"]-=1
    if click[0] == int(p_pos[0]) and click[0]-int(p_pos[0]) < 0:
        l_blt.append(Bullet(_blt_, [int(p_pos[0]-ratio[0]), int(p_pos[1]-ratio[1])], [-1.0, 0.0]))
    elif click[0] == int(p_pos[0]) and click[0]-int(p_pos[0]) > 0:
        l_blt.append(Bullet(_blt_, [int(p_pos[0]-ratio[0]), int(p_pos[1]-ratio[1])], [1.0, 0.0]))
    elif click[1] == int(p_pos[1]) and click[1]-int(p_pos[1]) < 0:
        l_blt.append(Bullet(_blt_, [int(p_pos[0]-ratio[0]), int(p_pos[1]-ratio[1])], [0.0, -1.0]))
    elif click[1] == int(p_pos[1]) and click[1]-int(p_pos[1]) > 0:
        l_blt.append(Bullet(_blt_, [int(p_pos[0]-ratio[0]), int(p_pos[1]-ratio[1])], [0.0, 1.0]))

    else:

        d = math.isqrt((click[0]-int(p_pos[0]))**2 + (click[1]-int(p_pos[1]))**2)
        d_x, d_y = [click[0]-int(p_pos[0]), click[1]-int(p_pos[1])]
        d = [d_x/d, d_y/d]

        if d[0] > 10.0 or d[1] > 10.0:
            if d[0] > d[1]:
                d[1]=(d[1]*10.0)/d[0]
                d[0]=10.0
            elif d[0] > d[1]:
                d[0]=(d[0]*10.0)/d[1]
                d[1]=10.0

        ratio = d
        l_blt.append(Bullet(_blt_, [int(p_pos[0]-ratio[0]), int(p_pos[1]-ratio[1])], ratio)) #id pos ratio
        _blt_ += 1


def create_enmy():
    global _enmy_

    rdm  = random.choice(["x", "yl", "yr"])
    if rdm == "x":
        l_enmy.append(Enemy(_enmy_, [random.randrange(X), -i_side]))
    elif rdm == "yl":
        l_enmy.append(Enemy(_enmy_, [-i_side, random.randrange(int(Y/2))]))
    else:
        l_enmy.append(Enemy(_enmy_, [X+i_side, random.randrange(int(Y/2))]))
    _enmy_ += 1


if __name__ == "__main__":

    restart()

    while True:

        _j_=0
        for i in range(len(l_blt)):
            l_blt[i-_j_].Move()

        _j_=0
        if random.randrange(5) == random.randrange(5):
            for i in range(len(l_enmy_blt)):
                l_enmy_blt[i].pos = [l_enmy_blt[i].pos[0]+l_enmy_blt[i].ratio[0], l_enmy_blt[i].pos[1]+l_enmy_blt[i].ratio[1]]

        if random.randrange(10) == random.randrange(10):
            for i in range(len(l_enmy)):
                l_enmy[i].Move()

        if dir == UP:
            p_pos[1]-=P_SPD
        elif dir == DOWN:
            p_pos[1]+=P_SPD
        elif dir == LEFT:
            p_pos[0]-=P_SPD
        elif dir == RIGHT:
            p_pos[0]+=P_SPD


        # Collision

        brk=False
        for i in range(len(l_enmy)):
            for j in range(len(l_blt)):
                j-=_j_
                if len(l_blt) == 0 or len(l_enmy) == 0:
                    brk=True
                    break

                try:
                    if int(i_side/2)+i_rad >= math.isqrt(int((l_blt[j].pos[0]-l_enmy[i].pos[0])**2 + (l_blt[j].pos[1]-l_enmy[i].pos[1])**2)):

                        try: l_enmy[i].health-=50
                        except:
                            brk=True
                            break
                        l_blt.pop(j)
                        if l_enmy[i].health <= 0:
                            l_enmy.pop(i)
                            d_stc["total_kills"]+=1
                            if l_enmy[i].type=="gunner":
                                d_stc["ammo"]+=5
                                d_stc["score"]+=6
                            else:
                                d_stc["score"]+=4
                            i-=1
                        _j_+=1
                except:
                    brk=True
                    break


            if brk == True:
                break
        _j_=0
        for i in range(len(l_enmy_blt)):
            i-=_j_
            for j in range(len(l_blt)):
                j-=_j_
                if math.isqrt(int((l_blt[j].pos[0]-l_enmy_blt[i].pos[0])**2 + (l_blt[j].pos[1]-l_enmy_blt[i].pos[1])**2)) <= 2*i_rad:
                    l_enmy_blt.pop(i)
                    l_blt.pop(j)
                    _j_+=1
                    break

        _j_=0
        for i in range(len(l_enmy_blt)):
            i-=_j_
            if int(i_side/2)+i_rad >= math.isqrt(int((l_enmy_blt[i].pos[0]-p_pos[0])**2 + (l_enmy_blt[i].pos[1]-p_pos[1])**2)):
                l_enmy_blt.pop(i)
                d_stc['health']-=15
                d_stc["damage_dealt"]+=15
                _j_+=1
            elif l_enmy_blt[i].pos[0]+i_rad > X or l_enmy_blt[i].pos[0]+i_rad < 0 or\
                 l_enmy_blt[i].pos[1]+i_rad > Y or l_enmy_blt[i].pos[1]+i_rad < 0:
                l_enmy_blt.pop(i)
                _j_+=1

        refresh()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                if d_stc["ammo"] > 0:
                    create_blt()
                else:
                    refresh()

            r1 = random.randrange(int(CRT_SPD))
            r2 = random.randrange(int(CRT_SPD))
            if r1 == r2 or len(l_enmy) == 0:
                create_enmy()
                if CRT_SPD <= 75.0:
                    CRT_SPD-=0.1


            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_w or event.key == pygame.K_UP) and dir!=UP:
                    dir=UP
                elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and dir!=DOWN:
                    dir=DOWN
                elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and dir!=LEFT:
                    dir=LEFT
                elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and dir!=RIGHT:
                    dir=RIGHT
                else:
                    dir=0

                if event.key == pygame.K_ESCAPE:
                    l = 12
                    f_big = 55
                    f_med = 40
                    f_sml = 30

                    pygame.draw.rect(SCREEN, black(), pygame.Rect(0, 0, X/2, Y))
                    pygame.draw.rect(SCREEN, white(), pygame.Rect(X/2, 0, X/2, Y))

                    try: font = pygame.font.Font("C:/Users/veera/AppData/Local/Microsoft/Windows/Fonts/visitor2.ttf", f_big)
                    except: font = pygame.font.SysFont("", f_big)
                    prt("Pause Menu", X/2, Y/l, grey())
                    prt("Controls", X/4, Y*3/l, white())
                    prt("Stats", X*3/4, Y*3/l, black())

                    try: font = pygame.font.Font("C:/Users/veera/AppData/Local/Microsoft/Windows/Fonts/visitor2.ttf", f_med)
                    except: font = pygame.font.SysFont("", f_med)
                    prt("Shooting", X/4, Y*5/l, white())
                    prt("Movement", X/4, Y*8/l, white())


                    try: font = pygame.font.Font("C:/Users/veera/AppData/Local/Microsoft/Windows/Fonts/visitor2.ttf", f_sml)
                    except: font = pygame.font.SysFont("", f_sml)
                    prt("Left Mouse Button", X/4, Y*6/l, white())
                    prt("W or UP", X/4, Y*9/l, white())
                    prt("A or LEFT and D or RIGHT", X/4, Y*10/l, white())
                    prt("S or DOWN", X/4, Y*11/l, white())

                    prt(f"Lives Left: {d_stc['lives']}", X*3/4, Y*5/l, black())
                    prt(f"Ammo Left: {d_stc['ammo']}", X*3/4, Y*6/l, black())
                    prt(f"Total Kills: {d_stc['total_kills']}", X*3/4, Y*7/l, black())
                    prt(f"Damage Dealt: {d_stc['damage_dealt']}", X*3/4, Y*8/l, black())
                    prt(f"Total Score: {d_stc['score']}", X*3/4, Y*9/l, black())

                    prt("Press any key to Continue", X*2/4, Y*2/l, grey())


                    pygame.display.flip()

                    brk=False
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    exit()
                                else:
                                    brk=True
                        if brk==True:
                            break


            if event.type == pygame.KEYUP:
                dir = 0

        if d_stc['health'] <= 0:
            d_stc['health']=100
            d_stc['lives']-=1
            d_stc['ammo']+=100
            if d_stc['lives'] <= 0:
                d_stc['lives']=0
                break
            restart(1)
            if d_stc['lives'] == 1:
                prt(f"You Died, {d_stc['lives']} life left", int(X/2), int(Y/2), white())
            else:
                prt(f"You Died, {d_stc['lives']} lives left", int(X/2), int(Y/2), white())
            pygame.display.flip()
            time.sleep(2.5)

        if i_time+0.75 <= time.time():
            d_stc['score']+=1
            i_time = time.time()
            if d_stc['score']%100==0:
                if d_stc['health'] < 90:
                    d_stc['health'] += 10
                elif d_stc['health'] < 100:
                    d_stc['health'] = 100
            if d_stc['score']%50==0:
                d_stc['ammo'] += 25

    while True:
        for event in pygame.event.get():
            l = 10
            f_big = 55
            f_med = 40
            f_sml = 30

            pygame.draw.rect(SCREEN, black(), pygame.Rect(0, 0, X, Y))
            try: font = pygame.font.Font("C:/Users/veera/AppData/Local/Microsoft/Windows/Fonts/visitor2.ttf", f_big)
            except: font = pygame.font.SysFont("", f_big)
            prt(f"Game Ended", X/2, Y/l, grey())

            try: font = pygame.font.Font("C:/Users/veera/AppData/Local/Microsoft/Windows/Fonts/visitor2.ttf", f_sml)
            except: font = pygame.font.SysFont("", f_sml)
            prt(f"Lives Left: {d_stc['lives']}", X/2, Y*3/l, white())
            prt(f"Ammo Left: {d_stc['ammo']}", X/2, Y*4/l, white())
            prt(f"Total Kills: {d_stc['total_kills']}", X/2, Y*5/l, white())
            prt(f"Damage Dealt: {d_stc['damage_dealt']}", X/2, Y*6/l, white())
            prt(f"Total Score: {d_stc['score']}", X/2, Y*7/l, white())

            try: font = pygame.font.Font("C:/Users/veera/AppData/Local/Microsoft/Windows/Fonts/visitor2.ttf", f_med)
            except: font = pygame.font.SysFont("", f_med)
            prt("Press any key to End", X/2, Y*9/l, grey())
            pygame.display.flip()

            if event.type == pygame.KEYDOWN:
                exit()
