# --------------------------------------------------------

# 一定要把 from ultralytics import YOLO 下载 __main__ 函数中，否则会报错以下信息：
# > 错误信息： RuntimeError: An attempt has been made to start a new process before the current process has finished its bootstrapping phase. 
# > > 通常是由于多进程执行导致的问题。在 Windows 平台上,使用 Python 的 multiprocessing 模块时会遇到这种情况。

# 出现这个错误的原因是:
# Windows 平台的多进程启动机制:
# Windows 平台不支持 Unix 的 fork() 系统调用来创建子进程。相反,它需要使用 spawn() 方法来创建新进程,这需要在主模块中进行一些特殊的处理。
# YOLOv8 中的多进程操作:
# YOLOv8 使用 PyTorch 的多进程数据加载功能来加快训练过程。但是,如果没有正确地处理多进程的启动,就会出现这个错误。
# 为了解决这个问题,需要在主模块中写入以下代码:

# --------------------------------------------------------

if __name__ == '__main__':
    from ultralytics import YOLO

    model = YOLO('yolov8n.pt')
    model.train(data='./data/mario.yaml', epochs=100, imgsz=640, device='cuda:0')