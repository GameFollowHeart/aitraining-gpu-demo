from ultralytics import YOLO
from PIL import Image
import cv2


model = YOLO("fcmario_last.pt")
# accepts all fonmats - image/dir/Path/URL/video/PIL/ndarray. 0 for webcamresults = model.predict(source="0")
# results = model.predict(source="0") # 用摄像头
# results = model.predict(source="folder",show=True)# Display preds. Accepts all YoLO predict argument


#from PIL
im1 = Image.open("1.png")
results = model.predict(source=im1, save=True) # save plotted images

#from ndarray
# im2 = cv2.imread("test.jpg")
# results = model.predict(source=im2,save=True,save_txt=True) # save predictions as labels
# #from list of PIL/ndancay
# results = model. predict(source=[im1, im2])
