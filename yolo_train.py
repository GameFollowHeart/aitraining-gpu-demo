from ultralytics import YOLO

# Load a model
# model = YOLO('./data/fall.yaml')  # build a new model from YAML
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
# model = YOLO('./fall.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

# Train the model
# device='cuda:0' 表示使用 cuda 调用 GPU 进行训练，若不设置，默认使用 cpu 进行训练
model.train(data='./data/mario.yaml', epochs=100, imgsz=640, device='cpu')