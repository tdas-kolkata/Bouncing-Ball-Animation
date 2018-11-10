import pygame as pg
import random
from math import sqrt

class make_ball:
	def __init__(self,x,y,speed_x,speed_y,color):
		self.x = x
		self.y = y
		self.speed_x = speed_x
		self.speed_y = speed_y
		self.color = color

	def show(self,screen):
		pg.draw.circle(screen,self.color,(self.x,self.y),4,0)

	def pos_update(self):
		self.x += self.speed_x
		self.y += self.speed_y

		if self.y > height or self.y <0 :
			self.speed_y = -self.speed_y
		if self.x > width or self.x <0 :
			self.speed_x = -self.speed_x

	@staticmethod
	def distance(ball1,ball2):
		dis =int(sqrt( (ball1.x - ball2.x)**2 + (ball1.y - ball2.y)**2 ))
		return dis


if __name__ == "__main__":
	red = (255,0,0)
	white = (255,255,255)
	green = (0,255,0)
	blue = (0,0,255)
	black = (0,0,0)
	dark_green = (0,100,0)

	pg.init()
	clock = pg.time.Clock()
	FPS = 40
	width,height = 600,600
	screen = pg.display.set_mode((width,height))


	ball_list = []
	TOTAL_NO_OF_BALLS = 100
	for _ in range(TOTAL_NO_OF_BALLS):
		b = make_ball(random.randint(0,width),random.randint(0,height),random.randint(-3,3),
			random.randint(-3,3),random.choice([green,red,blue,black,dark_green]))
		ball_list.append(b)

	end = False
	#screen.fill(white)
	while end==False:
		screen.fill(white)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				end = True
		
		for ball in ball_list:
			for another_ball in ball_list:
				if make_ball.distance(ball,another_ball) < 5:
					ball.speed_x,another_ball.speed_x = another_ball.speed_x,ball.speed_x
					ball.speed_y,another_ball.speed_y = another_ball.speed_y,ball.speed_y
			ball.pos_update()
			ball.show(screen)

		clock.tick(FPS)
		pg.display.update()

	pg.quit()
	quit()





