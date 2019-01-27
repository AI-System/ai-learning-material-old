import pygame
from pygame.locals import *
import time

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
  while True:
      # 绘制画面
      screen.blit(bg, (0,m))
      m += 2 # 不停向下移动
      if m >= -200: # 当移动完一张图片的位置之后，那么重新绘制 -968 + 768 = -200
        m = -968
      plane.display()
      # 键盘控制
      key_control(plane)
      # 更新显示
      pygame.display.update()
      # 定时显示
      time.sleep(0.03)

### 判断当前是否是主程序，如果是主程序则调用
if __name__ == '__main__':
  main()
