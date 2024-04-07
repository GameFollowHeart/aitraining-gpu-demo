import time,os,dlib
from ultralytics import YOLO
import pyautogui
import pygetwindow

def window_xywh(title):
  matchingWindows = pygetwindow.getWindowsWithTitle(title)
  if len(matchingWindows) == 0:
    raise Exception("Window not found %s " % title)
  win = matchingWindows[0]
  return win.left, win.top, win.width, win.height

def window_screen_shot_1(region):
  return pyautogui.screenshot(region=region)

time.sleep(1)
# save_dir = os.path.join(os.getcwd(), 'ai_traning_for_game/first-demo/yolo_model_images')
# print(f'save_dir: {save_dir}')
model = YOLO('fcmario.pt') # YOLO("yolov8n.pt")
title = "VirtuaNES - Super Mario Bros (J)" # 游戏窗口的名称
region = window_xywh(title) # 根据游戏窗口名称获取窗口尺寸信息

def start_training():
# while True:
  start_time = time.time()
  image = window_screen_shot_1(region)
  results = model(source=image, save=True)
  print(results)

start_training()