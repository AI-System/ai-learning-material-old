import pygame
from pygame.locals import *
import time

# 键盘控制函数
def key_control():
    ''' 键盘控制函数 '''
    # 执行退出操作
    for event in pygame.event.get():
      if event.type == QUIT:
        print('exit()')
        exit()
    
    # 获取按键信息
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_LEFT] or pressed_keys[K_a]:
      print('left ...')
    elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
      print('right ...')

    if pressed_keys[K_SPACE]:
      print('space ...')

def main():
  # 设置游戏主界面, 创建游戏窗口 512宽，568高 标志 0 深度 0
  screen = pygame.display.set_mode((512, 568), 0, 0)
  # 创建游戏背景
  bg = pygame.image.load("./images/bg2.jpg")
  m = -968 # 图片高 1536 , 画布高 568 , 将图片置地, -968是初始化时候的坐标位置 即从零点向上移动968像素, 最终底部对齐的效果
  # 注：因为涉及到无缝滚动, 所以画布是两张图片拼起来的, 一张图片的高度是 1536 / 2 = 768
  while True:
    # 绘制画面
    screen.blit(bg, (0, m))
    m += 2 # 不停向下移动
    if m >= -200: # 当移动完一张图片的位置之后，那么重新绘制 -968 + 768 = -200
      m = -968
      # 键盘控制
      key_control()
      # 更新显示
      pygame.display.update()
      # 定时显示
      time.sleep(0.033)

### 判断当前是否是主程序，如果是主程序则调用
if __name__ == '__main__':
  main()