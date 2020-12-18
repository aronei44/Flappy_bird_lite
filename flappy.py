import pygame, os, random

#deklarasi module
pygame.init()
pygame.font.init()

#warna
white = (255,255,255)
hitam = (0,0,0)


#lebar dan tinggi
x = 700
y = 500
midy = y/2
midx = x/2

#posisi awal
pos = [100,midy]
jump = False

#obstacle
l = 200
t = 200
t1 = y - t - l
ox=650
oy=0
oy1 = t + l
obs1 = [[ox, oy, 70, t]]
obs2 = [[ox, oy1, 70, t1]]

n1 = [ox, oy, 70, t]
n2 = [ox, oy1, 70, t1]

#game
gameover= False
score = 0
fps =50

#layar awal
screen = pygame.display.set_mode((x,y))
screen.fill((white))

#score
def show_score():
    score_font = pygame.font.SysFont('consolas', 20)
    score_surface = score_font.render('score: ' + str(int(score)), True, hitam)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (200, y+50)

    screen.blit(score_surface, score_rect)
    pygame.display.flip()


#mulai program
while not gameover:
	screen.fill(white)
	
	#border
	pygame.draw.rect(screen, hitam, pygame.Rect(0,0,x,5))	
	pygame.draw.rect(screen, hitam, pygame.Rect(0,0,5,y))		
	pygame.draw.rect(screen, hitam, pygame.Rect(0,y,x,5))		
	pygame.draw.rect(screen, hitam, pygame.Rect(x,0,5,y))	
	
	#bird	
	pygame.draw.rect(screen, hitam, pygame.Rect(pos[0],pos[1],80,40))
	
	#obstacle
	for o in obs1:
		pygame.draw.rect(screen, hitam,pygame.Rect(o))
		o[0]-=5
		if obs1[0][0]%400==0:
			obs1.insert(0,list(n1))
			obs2.insert(0,list(n2))
		if o[0]<=pos[0]+80 and o[0]+70>=pos[0] and o[1]+t >= pos[1]:
			gameover = True
	for o in obs2:
		pygame.draw.rect(screen, hitam,pygame.Rect(o))
		o[0]-=5
		if o[0]<=pos[0]+80 and  o[0]+70>=pos[0] and o[1] <= pos[1]+40:
			gameover = True
		if o[0]==pos[0]:
			score += 5
		
		
	#fungsi turun
	if pos[1]<y and jump == False:
		pos[1]+=5
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_SPACE:
				jump = True
				a = pos[1]-100
				
	#jump
	if jump == True:
		if pos[1] <= a:
			jump = False
		elif pos[1] <=a+20:
			pos[1]-= 4
		else:
			pos[1]-=10
	if score != 0 and score%100==0:
		fps +=5
			
	score+=0.05		
	show_score()		
	pygame.time.Clock().tick(fps)
	pygame.display.update()