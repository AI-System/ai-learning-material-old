import pygame
from pygame.locals import *
import time, random

# 创建飞机类
class Plane:
  # 初始化
  def __init__(self, screen):
    self.x = 200
    self.y = 400
    self.screen = screen
    self.image = pygame.image.load("./images/me.png")
    self.bullet_list = [] # 用于存放子弹的容器

  # 显示飞机和子弹
  def display(self):
    # 绘制子弹
    for b in self.bullet_list:
      b.display()
      if b.move():
        # 此处做一个优化, 如果子弹出了屏幕, 那么弹夹里面移除该子弹, 防止内存泄漏
        self.bullet_list.remove(b)

    # 绘制飞机功能
    self.screen.blit(self.image, (self.x, self.y))
  
  # 飞机移动
  def move(self, flag):
    # 移动控制：flag True 左, False 右
    if flag:
      self.x -= 12
    else:
      self.x += 12
    # 边界控制
    if self.x < -53:
      # 只让飞机出去一半位置
      self.x = -53
    if self.x > 459:
      # 512 - 106/2 = 459
      self.x = 459

  # 发射子弹
  def fire(self):
    # 子弹的位置是从飞机的零点 + 一半飞机的长度(106/2=53) 如果不准确可根据图片来微调
    self.bullet_list.append(Bullet(self.screen, self.x + 53, self.y))
    # print(len(self.bullet_list)) # test bullet number, prevent mem leak!

# 创建炮弹类
class Bullet:
  # 初始化
  def __init__(self, screen, x, y):
    self.x = x
    self.y = y
    self.screen = screen
    self.image = pygame.image.load("./images/pd.png")

  # 子弹显示
  def display(self):
    self.screen.blit(self.image, (self.x, self.y))

  # 移动功能 只在y轴y 子弹移动时优化处理
  def move(self):
    self.y -= 24 # 向上移动 24
    if self.y <= -17:
      # 子弹图片的高度是17，此时子弹出了屏幕
      return True

# 创建敌机类
class Enemy:
  # 初始化
  def __init__(self, screen):
    # 敌机x轴随机 0 ~ 408 px的范围内
    self.x = random.choice(range(409)) # 0 ~ 408 之间随机
    self.y = -75
    self.screen = screen
    self.image = pygame.image.load("./images/e2.png")

  # 子弹显示
  def display(self):
    self.screen.blit(self.image, (self.x, self.y))

  # 移动功能 敌机向下移动
  def move(self, plane):
    self.y += 5 # 向上移动 24
    # 循环飞机子弹，做碰撞检测
    for b in plane.bullet_list:
        if b.x > self.x + 12 and b.x < self.x + 92 and b.y > self.y + 20 and b.y < self.y + 60:
            plane.bullet_list.remove(b) # 当前敌机删除
            # 随即执行爆炸效果 此处能做异步操作吗?
            # 方案一：使用多线程
            # 方案二：像是 js中的定时器一样的异步延迟，不阻塞的方式
            # 待解决
            Blast(self.screen, self.x + 26, self.y).animate() # 执行动画时有卡顿 阻塞
            return True

    #判断敌机是否越界
    if self.y > 512:
        return True;

# 创建爆炸💥类
class Blast:
  def __init__(self, screen, x, y):
    self.x = x
    self.y = y
    self.screen = screen
    self.num = 1
    self.image = pygame.image.load("./images/bomb1.png")

  # 子弹显示
  def display(self):
    self.screen.blit(self.image, (self.x, self.y))

  # 爆炸动画
  def animate(self):
    while self.num <= 4:
      curImage = "./images/bomb" + str(self.num) + ".png"
      # print('curImage: ', curImage)
      self.image = pygame.image.load(curImage)
      # 显示自己
      self.display()
      self.num += 1
      time.sleep(0.03)
    
# 随机绘制敌机功能
def randomEnemy(enemyList, screen, plane):
  # 以一定的概率来随机输出敌机 0 ~ 49 
  if random.choice(range(50)) == 10: 
    enemyList.append(Enemy(screen))

  # 敌机批量绘制移动
  for em in enemyList:
    em.display() # 显示
    # 移动
    if em.move(plane):
      enemyList.remove(em)

# 键盘控制
def key_control(plane):
    # 执行退出操作
    for event in pygame.event.get():
      if event.type == QUIT: 
        # 匹配点击窗口的关闭按钮时触发
        exit()
    
    # 获取按键信息
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_LEFT] or pressed_keys[K_a]:
      plane.move(True)
    elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
      plane.move(False)

    # 空格键 发射功能
    if pressed_keys[K_SPACE]:
      plane.fire()

def main():
  # 设置游戏主界面, 创建游戏窗口 512宽，568高 标志 0 深度 0
  screen = pygame.display.set_mode((512, 568), 0, 0)
  # 创建游戏背景
  bg = pygame.image.load("./images/bg2.jpg")
  # 图片高 1536 , 画布高 568 , 将图片置底, 
  # -968是初始化时候的坐标位置 即从零点向上移动968像素, 最终底部对齐的效果
  m = -968 
  # 注：因为涉及到无缝滚动, 所以画布是两张图片拼起来的, 一张图片的高度是 1536 / 2 = 768
  # 创建飞机对象
  plane = Plane(screen)
  enemyList = [] # 存放敌机的数组
  blastList = [] # 存放爆炸的数组
  while True:
      # 绘制画面
      screen.blit(bg, (0,m))
      m += 2 # 不停向下移动
      if m >= -200: # 当移动完一张图片的位置之后，那么重新绘制 -968 + 768 = -200
        m = -968
      # 显示飞机
      plane.display()
      # 显示敌机
      randomEnemy(enemyList, screen, plane)
      # 键盘控制
      key_control(plane)
      # 更新显示
      pygame.display.update()
      # 定时显示
      time.sleep(0.03)

### 判断当前是否是主程序，如果是主程序则调用
if __name__ == '__main__':
  main()
