from ultralytics import YOLO
import pyautogui
import pygetwindow
import time

# 通过窗体标题，获取窗口位置和宽高
def window_sywh(window_title):
    macthing_windows = pygetwindow.getWindowsWithTitle(window_title)
    if len(macthing_windows) == 0:
        raise Exception("未找到窗口 %", window_title)
    win = macthing_windows[0]
    return win.left, win.top, win.width, win.height

# 对指定区域截图
def window_screenshot(region):
    return pyautogui.screenshot(region=region)

# 程序开始
def main(window_title):
    start_wait = 3
    print("程序在%d秒后开始运行", start_wait)
    model = YOLO("fcmario_last.pt")
    time.sleep(start_wait)

    region = window_sywh(window_title=window_title)
    # -- 循环
    while True:
        start_time = time.time()
        screenshot = window_screenshot(region=region)
        result = model(source=screenshot, save=True)
        print("识别结果：", result)
        print(result)



if __name__ == '__main__':
    # 游戏窗体的标题
    window_title = "NNNesterJ 0.23"
    main(window_title)