import pygame as pg
import random
import math

class Boid(pg.sprite.Sprite):
    def __init__(self, loc_init):
        super().__init__()
        self.image = pg.Surface((10, 10))
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        #initialize speed,heading location
        # Inside the Boid class, initialize speed with some randomness
        self.speed = random.uniform(3, 5)  # Adjust the range as needed
        self.heading = pg.Vector2(1,1)
        self.loc = loc_init
        self.rect.x = self.loc[0]
        self.rect.y = self.loc[1]   

    def update(self, boids):
        # 分別計算三個規則的向量
        separation_vector = self.calculate_separation(boids)
        alignment_vector = self.calculate_alignment(boids)
        cohesion_vector = self.calculate_cohesion(boids)

        # 調整速度和方向
        self.heading = self.heading + separation_vector + alignment_vector + cohesion_vector

        # 限制速度的最大值
        max_speed = 5
        if self.heading.length() > max_speed:
            self.heading = self.heading.normalize() * max_speed

        # 根據新的方向更新位置
        self.rect.x += self.heading.x
        self.rect.y += self.heading.y

        # 邊界處理， 讓鳥類在窗口內移動
        if self.rect.left > width:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = width
        if self.rect.top > height:
            self.rect.bottom = 0
        elif self.rect.bottom < 0:
            self.rect.top = height


    def calculate_separation(self, boids):
        # 計算分離向量
        separation_radius = 50
        separation_vector = pg.Vector2(0, 0)
        
        for boid in boids:
            if boid != self:
                distance = pg.Vector2(boid.rect.center) - pg.Vector2(self.rect.center)
                if 0 < distance.length() < separation_radius:
                    separation_vector -= distance.normalize()

        return separation_vector

    def calculate_alignment(self, boids):
        # 計算對齊向量
        alignment_radius = 100
        alignment_vector = pg.Vector2(0, 0)
        count = 0

        for boid in boids:
            #if boid != self:
                # 使用math.atan2()計算弧度值
            angle_rad = math.atan2(boid.heading.y, boid.heading.x)
            angle_deg = math.degrees(angle_rad)
            distance = pg.Vector2(boid.rect.center) - pg.Vector2(self.rect.center)
            if 0 < distance.length() < alignment_radius:
                alignment_vector += pg.Vector2(math.cos(math.radians(angle_deg)), math.sin(math.radians(angle_deg)))
                count += 1

        if count > 0:
            alignment_vector /= count

        return alignment_vector


    def calculate_cohesion(self, boids):
        # 計算聚集向量
        cohesion_radius = 150
        cohesion_center = pg.Vector2(0, 0)
        count = 0

        for boid in boids:
            if boid != self:
                distance = pg.Vector2(boid.rect.center) - pg.Vector2(self.rect.center)
                if 0 < distance.length() < cohesion_radius:
                    cohesion_center += pg.Vector2(boid.rect.center)
                    count += 1

        if count > 0:
            cohesion_center /= count
            cohesion_vector = cohesion_center - pg.Vector2(self.rect.center)
            epsilon = 1e-5
            if cohesion_vector.length() > epsilon:
                return cohesion_vector.normalize()
            else:
                return pg.Vector2(0, 0)

        else:
            return pg.Vector2(0, 0)
        


# # 初始化Pygame
# pg.init()

# # 設置窗口尺寸和顯示
# width, height = 800, 600
# screen = pg.display.set_mode((width, height))
# pg.display.set_caption("Boids Simulation")


# Initialize Pygame
pg.init()

# Get the current screen display mode
screen_info = pg.display.Info()
width, height = screen_info.current_w, screen_info.current_h

# Set the display mode to fullscreen
fullscreen = True
screen = pg.display.set_mode((width, height), pg.FULLSCREEN)
pg.display.set_caption("Boids Simulation")



# 創建一個鳥類群集
boids_group = pg.sprite.Group()
for i in range(100):
    boids_group.add(Boid([random.randint(0, width), random.randint(0, height)]))


clock = pg.time.Clock()

# 主循環
running = True
while running:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            if fullscreen:
                # Switch back to windowed mode
                screen = pg.display.set_mode((width, height))
            running = False  # Exit the program

    # 清空
    screen.fill((0,0,0))
    

    # 移動和繪製每個鳥類
    boids_group.update(boids_group)

    boids_group.draw(screen)

    # 更新畫面
    pg.display.flip()


pg.quit()






